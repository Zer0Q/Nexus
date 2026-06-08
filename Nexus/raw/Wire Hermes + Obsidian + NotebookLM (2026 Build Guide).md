---
title: "Wire Hermes + Obsidian + NotebookLM (2026 Build Guide)"
source: "https://www.tonyreviewsthings.com/wire-hermes-agent-obsidian-notebooklm-stack/"
author:
  - "[[Tony Simons]]"
published: 2026-06-08
created: 2026-06-08
description: "A buildable Hermes + Obsidian + NotebookLM memory stack. Verified commands, MCP config, and the no-public-API gap, called out."
tags:
  - "clippings"
summary:
---
## Quick answer

A Hermes cron job can read your Obsidian vault, push new sources to a NotebookLM notebook, ask a grounded question, and write the answer back to a new note in your vault. Fully automated. Fully local-first where it counts. Re-runnable.

The three tools cover three different jobs that overlap only at the seams.

- **Obsidian** is the durable substrate, the local-first markdown vault you actually own.
- **NotebookLM** is the bounded-research sandbox, a source-grounded LLM that cannot leak beyond the sources you uploaded. The [TRT explainer on what NotebookLM does](https://www.tonyreviewsthings.com/what-does-notebooklm-do/) is a good refresher if you haven’t used it.
- **Hermes** is the operator that runs the loop on a schedule, moves bytes between the two, and keeps a memory of who you are across sessions.

The fastest path is the no-agent cron mode: a 10-line bash script that watches `Sources/` for new files, copies them to a staging dir, and calls the upload skill. It costs zero LLM tokens. As a result, the gathering step scales to thousands of files without ever touching a paid LLM endpoint. Most readers don’t realize this part of Hermes exists.

## Who this is for

- **Best for:** builders and operators who already use Obsidian (or any markdown vault) and want a real, working long-term memory + research loop, not a content calendar.
- **Not for:** someone who wants a set-and-forget SaaS. Someone who hasn’t set up Hermes Agent yet; start with the [docs](https://hermes-agent.nousresearch.com/docs) first, then come back.
- **Assumptions:** Mac or Linux, basic CLI comfort, Obsidian 1.13 or newer, Hermes Agent v0.16.0 or newer. You don’t need to be a Python expert, but you should be willing to paste a `pip install` line and a bash one-liner.

## Tools needed

| Tool | Why | Where |
| --- | --- | --- |
| Hermes Agent v0.16.0+ | the operator | [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| Obsidian v1.13.0+ | the substrate | [obsidian.md](https://obsidian.md/) |
| Local REST API plugin v4.1.3+ | the wire into the vault | [community listing](https://community.obsidian.md/plugins/obsidian-local-rest-api) |
| NotebookLM (any tier) | the bounded sandbox | [notebooklm.google.com](https://notebooklm.google.com/) |
| `notebooklm-py` v0.7.1+ | the missing NotebookLM API | [github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) |
| Python 3.10+ | for the wrapper | your OS package manager |

**Optional but recommended:**

- **Templater** ([community listing](https://community.obsidian.md/plugins/templater-obsidian)) for deterministic file naming in `Sources/` so a `find -newer` always returns the right files
- **Smart Connections** ([community listing](https://community.obsidian.md/plugins/smart-connections)) for local semantic search across the vault, the natural complement to Obsidian as substrate

**One thing to be honest about before we start:**

NotebookLM does not have a public API for the consumer product as of 2026-06-07. The Enterprise product does, but for the rest of us the answer is “no.”

The personal setup in this article drives the NotebookLM web UI via the `notebooklm-py` wrapper. Playwright under the hood. If Google changes an internal endpoint tomorrow, the wrapper can break. As a result, you should plan to have a fallback in your back pocket.

I’m calling this out up front because pretending otherwise would waste your afternoon.

![Three-card infographic showing Obsidian, Hermes, and NotebookLM as the stack for an automated research loop.](https://www.tonyreviewsthings.com/wp-content/uploads/2026/06/know-the-stack-obsidian-hermes-notebooklm.jpg.webp)

Three-card infographic showing Obsidian, Hermes, and NotebookLM as the stack for an automated research loop.

## Step-by-step guide

### Step 1: Install Hermes Agent and verify the CLI

**What to do:** follow the [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs) to install (pip or git clone + venv), then run:

```
hermes --version
hermes doctor
```

**Why it matters:** if `hermes doctor` doesn’t come back clean, every step below is going to fight you. Fix the runtime first. As a result, the rest of the build becomes a series of small additions rather than a debugging marathon.

**Watch out for:** Python version mismatch (Hermes wants 3.10+), `~/.hermes/.env` permissions, and the `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` you wired in. If you don’t have a key yet, pick a provider from the [providers integration docs](https://hermes-agent.nousresearch.com/docs/integrations/providers) and add the key to `~/.hermes/.env`.

### Step 2: Point Hermes at your Obsidian vault via the Local REST API plugin’s MCP server

**What to do:**

1. In Obsidian, install the **Local REST API** community plugin (Settings → Community plugins → search “Local REST API”, authored by coddingtonbear, 484k+ downloads).
2. In the plugin’s settings, copy the API key (it’s a long random string). Leave the port on the default `27124` (HTTPS) unless you have a reason to change it.
3. From the terminal:
```
hermes mcp add --url https://127.0.0.1:27124/mcp/ --auth header obsidian
```

When it prompts, paste the API key. Hermes strips the `Bearer ` prefix, saves the token to `~/.hermes/.env` as `MCP_OBSIDIAN_API_KEY`, and writes a `mcp_servers.obsidian` block to `~/.hermes/config.yaml`.

**Verify it works:**

```
hermes mcp list
hermes mcp test obsidian
```

The `mcp test` should return a list of available tools, file CRUD, active-file read/write, periodic notes, command palette, JsonLogic search, and tag queries. That’s the full wire.

**Why it matters:** this is the connection that lets any Hermes cron job or skill read and write your vault as if it were just another local REST client.

Once it’s wired, every other piece of the stack can ask “what’s in my Obsidian?” and “drop a new note in my Obsidian” through a single tool call.

The pattern is the same one Google Antigravity just shipped for [Skills + MCP](https://www.tonyreviewsthings.com/google-antigravity-skills-mcp-agentic-ide/). The Local REST API plugin is the Obsidian side of the same idea.

#### Security caveats

- The HTTPS endpoint uses a self-signed cert. Either trust the cert once (browser shows a warning you can accept for `127.0.0.1`) or enable the plain-HTTP fallback on `127.0.0.1:27123` in the plugin settings. Plain HTTP is fine on loopback, but don’t bind it to a public interface.
- The v4.1.3 release (2026-06-04) fixed a path-traversal vulnerability. Update before you go live.
- The plugin only listens on `127.0.0.1` by default, which is the right default. Don’t change that.

If you’d rather hand-edit the config (the YAML form is the same pattern other MCP servers use), drop this into `~/.hermes/config.yaml`:

```
mcp_servers:
  obsidian:
    url: https://127.0.0.1:27124/mcp/
    timeout: 120
    connect_timeout: 60
    headers:
      Authorization: Bearer ${MCP_OBSIDIAN_API_KEY}
```

…and put the token in `~/.hermes/.env`:

```
MCP_OBSIDIAN_API_KEY=<your-bearer-token-here>
```

### Step 3: Install the NotebookLM automation wrapper

**What to do:**

```
pip install notebooklm-py
notebooklm login
```

The `login` command opens a Chromium window, you sign into your Google account as usual, and it imports the cookies. No fresh OAuth dance. After that, you can drive NotebookLM from the CLI:

```
# Replace <notebook_id> with the ID from your NotebookLM URL bar.
# Example:  notebooklm ask "summarize the three sources in this notebook" --notebook abc123def4
notebooklm ask "summarize the three sources in this notebook" --notebook "$NOTEBOOK_ID"
notebooklm source add "$NOTEBOOK_ID" /path/to/note.md
notebooklm generate audio "$NOTEBOOK_ID" --format deep-dive
notebooklm download "$NOTEBOOK_ID" --output ~/Audio/
```

**Why it matters:** NotebookLM has no public consumer API. The community has been waiting on one for a year. Until Google ships one, this is the most reliable way to script it.

**Watch out for:** the wrapper’s own README warns: *“APIs may break. Google can change internal endpoints anytime.”* Treat it as a convenience layer, not a contract. If it breaks, the underlying engine is Playwright, so you can always roll a 50-line script that does the same thing.

### Step 4: Create a Hermes skill that pushes sources from Obsidian to a NotebookLM notebook

**What to do:** drop a `SKILL.md` into `~/.hermes/skills/obsidian-notebooklm-push/`:

```
# obsidian-notebooklm-push

## What I do
Push new files from \`Sources/\` in your Obsidian vault to a fixed NotebookLM
notebook so they're ready for the next ask call.

## Inputs
- \`NOTEBOOK_ID\` env var (or hardcoded constant in the script)

## Steps
1. Use the \`obsidian\` MCP server to list files in \`Sources/\` newer than the
   last-pushed timestamp (stored in \`Sources/.last-pushed\`).
2. For each new file, call:
   \`notebooklm source add "$NOTEBOOK_ID" /path/to/file.md\`
3. Update \`Sources/.last-pushed\` with the current timestamp.

## Failure modes
- If \`notebooklm source add\` errors, log the filename to \`Sources/.errors\`
  and continue. Do not abort the whole run.
- If the notebook ID is unset, fail fast with a clear message. Do not guess.
```

**Why it matters:** turns the integration from a one-off into a reusable building block. As a result, every other cron or skill in your stack can now call “push the new sources” without re-implementing the logic.

**Watch out for:** never put the Bearer token, the notebook ID, or any other secret in the skill file. The notebook ID is a constant you can commit; the Bearer token lives in `~/.hermes/.env` and is referenced by env var.

### Step 5: Create a Hermes skill that pulls grounded answers back into the vault

**What to do:** a second skill at `~/.hermes/skills/obsidian-notebooklm-pull/`:

```
# obsidian-notebooklm-pull

## What I do
Take a research question, ask the bound NotebookLM notebook, format the
grounded answer with inline citations, and write the result to
\`Research/YYYY-MM-DD-<slug>.md\` in your Obsidian vault.

## Inputs
- \`QUESTION\` (the research question)
- \`NOTEBOOK_ID\` (env var)

## Steps
1. Call \`notebooklm ask "$QUESTION" --notebook "$NOTEBOOK_ID" --format json\`
2. Parse the response. Extract the answer text and the citation list.
3. Format the result as a markdown file with YAML frontmatter that records
   the question, the timestamp, the notebook id, and the list of source
   citations NotebookLM used. Then render the answer body with inline
   \`[1]\`, \`[2]\` markers and a "## Sources" section at the bottom that
   resolves each marker to the source title. Use angle-bracket placeholders
   for any value the formatter doesn't have on hand.
4. Write the result to \`Research/<date>-<slug>.md\` via the \`obsidian\` MCP
   server. The slug is a kebab-case version of the first 6 words of the
   question.

## Failure modes
- If \`notebooklm ask\` returns no citations, abort. Do not write a note
  with an ungrounded answer. The whole point of using NotebookLM is
  the grounding.
```

**Why it matters:** closes the loop. Sources in, grounded answers out, vault as the source of truth. Future-you can grep the vault and find every research question you’ve ever asked, with the source list attached for re-verification.

**Watch out for:** include the source-list response from NotebookLM in the frontmatter of the result note, not just in the body. Future-you wants to re-verify the answer in 6 months without re-running the query.

### Step 6: Wire it to a no-agent cron job (the load-bearing cheap primitive)

**What to do:** this is the part most readers skip, and it’s the most important. Save this as `~/.hermes/scripts/vault_research_loop.sh`:

```
#!/usr/bin/env bash
set -euo pipefail

# vault_research_loop.sh
# Watches Sources/ in your Obsidian vault and pushes new files
# to the bound NotebookLM notebook. No LLM tokens burned.
#
# Schedule with: hermes cron create --name "vault-research-loop" \
#   --schedule "every 4h" --script ~/.hermes/scripts/vault_research_loop.sh

NOTEBOOK_ID="${NOTEBOOK_ID:?set NOTEBOOK_ID in ~/.hermes/.env}"
VAULT_SOURCES="$HOME/Documents/MainVault/Sources"
LAST_PUSHED="$VAULT_SOURCES/.last-pushed"
ERRORS="$VAULT_SOURCES/.errors"

mkdir -p "$VAULT_SOURCES"
touch "$LAST_PUSHED" "$ERRORS"

# Find markdown files newer than the last successful push.
find "$VAULT_SOURCES" -maxdepth 1 -name '*.md' -newer "$LAST_PUSHED" \
  | while read -r file; do
      if notebooklm source add "$NOTEBOOK_ID" "$file" >/dev/null 2>&1; then
        echo "$(date -u +%FT%TZ) ok $file" >> "$ERRORS".log
      else
        echo "$(date -u +%FT%TZ) FAIL $file" >> "$ERRORS"
      fi
    done

touch "$LAST_PUSHED"
```

Then:

```
chmod +x ~/.hermes/scripts/vault_research_loop.sh
hermes cron create \
  --name "vault-research-loop" \
  --schedule "every 4h" \
  --script ~/.hermes/scripts/vault_research_loop.sh
```
![Workflow diagram showing a cron job pushing new Obsidian notes into NotebookLM through Hermes automation.](https://www.tonyreviewsthings.com/wp-content/uploads/2026/06/cron-mode-cheap-primitive-hermes-notebooklm-automation.jpg)

Workflow diagram showing a cron job pushing new Obsidian notes into NotebookLM through Hermes automation.

**Why it matters:** this is the part that runs while you sleep, costs zero LLM tokens, and proves the wire works before you commit to the more expensive LLM-calling skills. Most stacks fail because the operator never gets scheduled, so schedule it.

**Watch out for:** make the script idempotent. A cron that runs twice in an hour should not double-upload. The `find -newer` pattern + the `.last-pushed` sentinel does this for you. The script should also fail gracefully, not abort the whole run on one bad file.

### Step 7: The 8am briefing (optional, but the payoff)

**What to do:** a second cron that reads the latest `Research/` notes, summarises them via Hermes’ chat, and drops a `Briefings/YYYY-MM-DD.md` into your vault:

```
hermes cron create \
  --name "morning-vault-briefing" \
  --schedule "0 8 * * *" \
  --prompt "Read the most recent Research/ notes in the bound Obsidian vault. Write a 5-bullet morning briefing to Briefings/$(date +%F).md. Keep it tight, no fluff, no preamble."
```
![Four-step infographic showing Obsidian capture, NotebookLM grounded answers, Hermes write-back, and a morning briefing.](https://www.tonyreviewsthings.com/wp-content/uploads/2026/06/question-to-morning-briefing-obsidian-notebooklm-hermes.jpg)

Four-step infographic showing Obsidian capture, NotebookLM grounded answers, Hermes write-back, and a morning briefing.

**Why it matters:** makes the loop visible. You wake up to a morning briefing in your own vault, written by your own operator, grounded in research that you asked yesterday. The loop is now closed and observable.

**Watch out for:** keep the LLM call small and the prompt deterministic. This is the “send the summary to Telegram” line, not a freeform essay. The prompt should specify output shape, length, and tone. Don’t let it get creative.

## Common mistakes (the four failure modes the source pack flagged)

The recipe above is the happy path. The unhappier paths are real and worth naming.

### 1\. Letting Hermes hallucinate the citation

The whole reason you’re routing through NotebookLM is the grounding. As a result, if you ever rephrase the answer through Hermes’ chat, you lose the citation chain.

**Mitigation:** always pull the answer directly from the `notebooklm ask` response, never from a Hermes-only rephrasing. If you want a tighter version, send the NotebookLM response back through NotebookLM with a reformat prompt. Don’t switch operators.

### 2\. Asking NotebookLM to summarize a notebook it doesn’t have

This sounds obvious, but it bites in practice. The cron job pushed sources yesterday, the notebook got reset, the cron pushed again to a different notebook ID, and now your `ask` call is hitting an empty notebook. As a result, the answer you get back is “I don’t have any sources.”

**Mitigation:** the cron job tracks the active `notebook_id` in `Sources/.notebook-id` and the pull skill asserts the same ID before asking. Treat the notebook ID as a first-class variable, not a magic string.

### 3\. Letting the Obsidian vault drift out of sync with the notebook sources

You renamed a file in Obsidian, the cron uploaded the old filename, the pull skill cites a name that no longer exists in your vault.

**Mitigation:** use Templater for deterministic file naming (`Sources/{{date}}-{{slug}}.md`) so a fresh `find -newer` always returns the right files. The pull skill can then resolve the citation back to the current vault path.

### 4\. Hardcoding secrets in skill files

This one is so common it has a name in the security community.

**Mitigation:** every credential lives in `~/.hermes/.env` and is referenced by env var. Keep secrets out of skill files, out of cron scripts, and out of any config that gets committed.

## FAQ

### On the loop

**Q: Do I really need all three tools?** A: No. If you just want durable notes, Obsidian alone is enough. If you just want a bounded-research tool, NotebookLM alone is enough (the [TRT NotebookLM + Gemini workflow guide](https://www.tonyreviewsthings.com/gemini-notebooklm-workflow-guide/) covers the two-tool case). The third tool, Hermes, is what turns two static tools into a loop, and I’m being honest about that: the loop is the product, not the notes.

**Q: Doesn’t NotebookLM have a public API?** A: No, not for the consumer product as of 2026-06-07. The Enterprise product does (it has a “Standalone API” for podcast generation), and Google Cloud customers can pay for it. For everyone else, the `notebooklm-py` wrapper drives the web UI via Playwright. It’s a wrapper, not a contract. Have a fallback.

### On the wiring

**Q: Why Hermes as the operator and not ChatGPT or Claude?** A: You can use either. The article’s stance is that the operator is a small, observable, scheduled job, and Hermes’ cron + skills + MCP shape is the most concrete of the bunch. The wiring pattern (cron → skill → MCP → vault) is what you’re learning here. Swap the operator and the rest still works.

**Q: Is the Local REST API plugin safe to expose?** A: It listens on `127.0.0.1` only by default, which is the right default. The v4.1.3 release (2026-06-04) fixed a path-traversal vulnerability, so update before you wire it. The Bearer token is the only auth. If you must expose it beyond loopback, put it behind a reverse proxy with TLS and a real auth layer; don’t.

### On the cost

**Q: How much does this cost to run?** A: Obsidian is free for personal use. Hermes is open source (MIT). The NotebookLM tier question is the real cost.

| Plan | Price | Storage | Cinematic Video Overviews/day |
| --- | --- | --- | --- |
| Google AI Free | $0 | 15 GB | n/a |
| Google AI Plus | $7.99/mo | 200 GB | 2 |
| Google AI Pro | $19.99/mo | 5 TB | 10 |
| Google AI Ultra 5x | $99.99/mo | 20 TB | 10 |
| Google AI Ultra 20x | $199.99/mo | 30 TB | 20 |

For most builder loops, the free tier is enough. Verify the current prices on the [Google AI plans page](https://one.google.com/about/google-ai-plans/) before you commit. Google labels the limits “Subject to Change.”

## Final recommendation

**Best approach:** start with the no-agent cron mode (Step 6). It’s the cheapest part of the loop, costs zero LLM tokens, and proves the wire works end to end before you commit to the LLM-calling skills in Steps 4, 5, and 7. If Step 6 is running cleanly and the right files are landing in the right notebook, the rest is a series of small additions, not a new architecture.

In other words, prove the cheap primitive first, then add cost.

**When to use it:** if you already use Obsidian and want research that survives you closing the laptop. The loop is a force multiplier on a vault you actually use; it’s not a replacement for using the vault.

**When to avoid it:** if you don’t yet have an Obsidian vault you actually use daily, fix that first. The loop is only as good as the substrate. If your `Sources/` folder is empty because you don’t capture things, no amount of cron magic will save you.

**Alternative if needed:** if Hermes is too much, the same wiring works with any MCP-aware agent. Claude Code, Cursor, and Claude Desktop all have first-class MCP support, and the Local REST API plugin’s community page ships snippets for all of them.

The plugin is the constant. Swap the operator and the rest of the loop carries over.

If you want a deeper read on why Hermes is the operator worth picking first, the [TRT Hermes Agent review](https://www.tonyreviewsthings.com/hermes-agent-by-nous-research-review/) is the long-form version of that argument.

## What’s next

If you build this and it works (or breaks in a new and interesting way), the part worth writing back is the failure mode.

NotebookLM endpoint drift. Cron double-fire. Vault-rename-desyncs-citation bug. Each of these is a real failure I expect someone to hit within a month of running this for real.

These are the parts that make a recipe a real recipe. Drop a comment or ping me on X. The next pass on this article should be a “what actually went wrong” addendum, not a feature list.