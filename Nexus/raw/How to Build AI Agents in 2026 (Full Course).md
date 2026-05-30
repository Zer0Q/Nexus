---
title: "How to Build AI Agents in 2026 (Full Course)"
source: "https://x.com/Av1dlive/status/2054238056090325492"
author:
  - "[[@Av1dlive]]"
published: 2026-05-02
created: 2026-05-31
description: "here is the truth nobody tells ai builders.    most of them are building demosall you need to build isa production level ai agent TLDR; if y..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HIIO-jBb0AAnoH-?format=jpg&name=large)

## here is the truth nobody tells ai builders.

## most of them are building demos

## all you need to build is

**a production level ai agent**

> **TLDR;** if you don't wanna read it, give this link to your agent and ask it questions: ➡️[https://github.com/codejunkie99/agentic-harness](https://github.com/codejunkie99/agentic-harness)

**here is the tweet that started it all**

> 2 de maig
> 
> The Harness is a Context Manager on Behalf of the Model What happens when the context window fills up and who decides? This decision is external to the model - The Harness designer must have some opinion here! Decisions like this are crucial in turning a model into a great

the problem is that most AI engineers have no clear idea what to actually build when they decide to get serious about agents.

some reach for LangChain because the multi-agent demos look clean on YouTube, and spend the next two weeks fighting Python interop and async runtime mismatches before scrapping the whole thing.

some try to build a custom orchestration layer from scratch : a loop, a session store, a context assembler and never finish the actual agent because the infrastructure ate the timeline.

others copy the hello-world webhook example, get a JSON response back, assume they understand the system, and ship something that breaks the first time a session runs past ten minutes, a remote sandbox goes down mid-task, or the context window fills without compaction configured.

the result is usually the same: a lot of plumbing, no production agents, and no mental model for what a production agent runtime actually looks like.

if your goal is to build and ship real agents in 2026, you don't need to learn six frameworks.

you need to understand one runtime deeply enough to own a production agent from handler to deployment.

that means learning how to:

- wire the three-layer architecture so your handler logic survives provider swaps and target changes without touching agent code
- use sessions and tasks correctly so long jobs don't contaminate their own context
- write roles and skills that shape model behavior without recompiling anything
- configure compaction so sessions running for two hours don't start hallucinating at hour one
- point HttpSessionEnv at remote sandboxes so the binary runs locally while execution runs on Linux
- pick the right build target : native, node, or Cloudflare , without rewriting any agent logic between them
- generate connectors instead of hand-writing adapters, and understand why that distinction matters under real load

this guide is a full technical walkthrough built from the actual agentic-harness codebase, six weeks of building and breaking real agents with it, and the failure modes that cost the most time to debug.

**the piece is 4,000+ WORDS and pulls from the repo and the docs directly not secondhand summaries or demo-level examples.**

**but its real value is that every section has a working code snippet, a clear explanation of why the decision was made, and the exact failure mode you'll hit if you skip it.**

**that way, by the time you finish reading, you can own a production agent end to end from the first handler to the sandbox to the CI job that runs it unattended.**

**building this understanding took more than 6 WEEKS of daily work with the codebase, most of it debugging things that looked correct before they broke under real conditions.**

**now let's get into it.** **⬇️**

## The Shape of the Project

two crates. one binary. every execution target is a config choice, not a rewrite.

```rust
agentic-harness/
├── crates/
│   ├── agentic-harness        — SDK: AgentApp, sessions, tasks, roles, skills,
│   │                            ModelClient, tools, HttpSessionEnv, HTTP/SSE serving
│   └── agentic-harness-cli    — CLI: guide, code, new, dev, run, build, serve,
│                                host, doctor, dashboard, inspect, sandbox, add, smoke
├── examples/
│   └── hello-world            — minimal webhook agent, works as a starter template
├── docs/                      — architecture, targets, runtime config, HTTP protocol,
│                                Cloudflare boundary, deployment guides, feature status
├── Formula/                   — Homebrew formula for local install
└── scripts/
    └── install.sh             — tarball install, copies binary to ~/.agentic-harness/bin
```

- the SDK is a library you pull into any rust project. the CLI wraps it. your agent is a rust binary that starts with use agentic\_harness::prelude::\*.
- cargo build is the whole pipeline. no bundler. no transpile step. no language runtime on the target machine. one self-contained executable plus a manifest.json.

the design constraint that drove everything: the same agent binary should run on your laptop in interactive mode, in a GitHub Actions job cloning a fresh repo, against a remote E2B sandbox over HTTP, and on a Cloudflare Worker boundary without changing a single line of agent logic between them.

every decision in this codebase exists to honor that constraint.

## The 3 layers and why each one exists

the mental model is three concentric rings. knowing where each boundary sits will save you more debugging time than anything else in this guide.

**your rust code is the outer ring.**

- you write handlers. handlers receive an AgentContext. they call sessions. sessions call the model, read files, write files, run shell commands, spawn tasks, connect to MCP servers.
- you never touch an HTTP client directly. you never parse a model response directly. the SDK handles both.

**the harness is the middle ring.**

- it manages the agent registry, routes identity by URL path, handles session persistence across calls, context compaction when sessions grow, role and skill discovery, model selection precedence, and the provider-neutral ModelClient trait .
- that lets you swap Anthropic for OpenAI for a local Ollama instance without touching handler code.
- the harness is what makes your agent logic reusable across providers and targets.
- it's also where all the things that break in production get handled session state, context overflow, provider failures, concurrent request ordering.

**execution targets are the inner ring.**

- local filesystem. CI checkout. HttpSessionEnv pointed at Daytona or E2B. Cloudflare Worker boundary.
- the harness doesn't care which one you're using. your handlers don't either. they call [session.shell](https://session.shell/)() and session.write() and the harness translates those to whatever the underlying target needs.
- this separation is the whole point. when E2B releases a new API version, you update the connector, not your agent logic.
- when Anthropic ships claude-opus-4-7, you update runtime.json, not your handlers. the outer ring stays clean because the middle ring absorbs all the churn.

## runtime config: the file that controls the model layer

before you write a single handler, you need runtime.json in your workspace.

```rust
{
  "defaultModel": "anthropic/claude-sonnet-4-6",
  "openaiCompatibleModels": ["anthropic/claude-sonnet-4-6"],
  "providers": {
    "anthropic": {
      "baseUrl": "https://api.anthropic.com/v1",
      "apiKeyEnv": "ANTHROPIC_API_KEY"
    }
  }
}
```

drop this at .agentic-harness/config.json or at the workspace root as agentic-harness.json. load\_workspace\_context() picks it up automatically.

```rust
fn app() -> Result<AgentApp, AgenticHarnessError> {
    Ok(AgentApp::new()
        .with_workspace(".")
        .load_workspace_context()?)
}
```

model selection at runtime follows this precedence:

1. PromptOptions::model(...) : per-call override
2. the selected role's model metadata : per-role default
3. defaultModel from runtime config : workspace default

the thing to understand: the model ID must be registered before you can use it. openaiCompatibleModels is the list the harness uses to wire up the built-in chat-completions client. if your model isn't in that list, you get a clean error at startup instead of a confusing failure mid-session.

**for OpenAI-compatible gateways, the config looks the same. point baseUrl at your gateway:**

```rust
{
  "defaultModel": "gateway/gpt-5.5",
  "openaiCompatibleModels": ["gateway/gpt-5.5"],
  "providers": {
    "gateway": {
      "baseUrl": "https://gateway.example/v1",
      "apiKeyEnv": "GATEWAY_API_KEY",
      "headers": {
        "X-Custom-Header": "value"
      }
    }
  }
}
```

- never write a literal API key into runtime.json. use apiKeyEnv and keep the actual key in your environment.
- the harness reads the env var at request time, not at startup which means you can rotate keys without restarting the server.

## agent identity is a URL path, never a registry lookup

this was the first design decision that surprised me. now i think it's the right one.

there is no agent ID system. no registry key. no UUID you generate yourself. your agent's identity is POST /agents/<name>/<id>.

```bash
# start a session or continue an existing one
curl http://localhost:3583/agents/codebot/pr-review-447 \
  -H "Content-Type: application/json" \
  -d '{"pr_number": 447, "repo": "my-org/my-repo"}'

# same id = same session, history carries over
curl http://localhost:3583/agents/codebot/pr-review-447 \
  -H "Content-Type: application/json" \
  -d '{"message": "also check the migration files"}'

# different id = fresh session, clean history
curl http://localhost:3583/agents/codebot/pr-review-512 \
  -H "Content-Type: application/json" \
  -d '{"pr_number": 512, "repo": "my-org/my-repo"}'
```

- the harness handles all session state bookkeeping behind that URL.
- the reason this works: every caller in every system already knows how to construct a meaningful ID from context. a PR number. a run ID. a timestamp combined with a task name. a user handle.
- you don't need a session creation endpoint. you don't need to store session IDs separately. the URL is the session.

**the agent handler on the rust side calls** [ctx.id](https://ctx.id/)**() to get whatever ID the caller provided:**

```rust
.agent(AgentDefinition::webhook("codebot", |ctx: AgentContext| {
    let session = ctx.session_with_id(ctx.id());
    // session history is automatically scoped to this id
    // calling the same endpoint with the same id continues the conversation
    let result = session.prompt("Review the changes in this PR.")?;
    Ok(json!({ "review": result.text() }))
}))
```

## sessions: the stateful execution context

a session is more than a conversation thread. it's the full execution context for an agent invocation.

it holds:

- message history with the model
- workspace file access (read, write, edit, grep, glob, stat, readdir)
- shell execution with cwd and env control
- tool registrations (MCP servers, custom tools)
- the assigned role and its system prompt overlay
- the compaction budget and history watermark

you get a session by calling ctx.session\_with\_id() with whatever ID makes sense:

```rust
let session = ctx.session_with_id(ctx.id());
from there, everything is method calls:
// call the model
let response = session.prompt("Summarize the recent changes to the auth module.")?;

// read a file into context
let content = session.read("src/auth/mod.rs")?;

// write a file
session.write("docs/auth-summary.md", &response.text())?;

// run a shell command, capture stdout
let test_output = session.shell("cargo test auth -- --nocapture 2>&1 | tail -50")?;
println!("exit: {}", test_output.status);
println!("output: {}", test_output.stdout);

// search for patterns across the workspace
let matches = session.grep("unwrap()", "src/", Some("*.rs"))?;

// list directory
let entries = session.readdir("src/auth/")?;
```

- sessions persist across HTTP calls when you use the same ID. call the same agent endpoint three times with the same session ID, the model sees all three exchanges as one continuous conversation.
- history accumulates automatically. you don't manage it.
- this is what makes multi-step workflows possible without managing state yourself. you keep calling session.prompt() and the harness handles everything else.

when you need to pass large amounts of context alongside a prompt, read the file and format it inline:

```rust
let src = session.read("src/payments/processor.rs")?;
let tests = session.read("tests/payments_test.rs")?;

let analysis = session.prompt(format!(
    "Here is the payments processor:\n\nrust\n{src}\n\n\n\
     Here are the tests:\n\nrust\n{tests}\n\n\n\
     The integration tests are failing in CI. Identify all the places \
     where an error is silently swallowed that could cause intermittent failures."
))?;
```

the session manages token counting so you don't accidentally overflow the context window mid-conversation. when you're close to the budget, compaction fires. more on that in a later section.

## tasks: focused child sessions that keep the parent clean

- this is the primitive i wish i'd understood on day one. it's the difference between agents that stay coherent across long jobs and agents that start hallucinating halfway through.
- a task is a one-shot child session. fresh history. shared workspace. returns a result to the parent. the parent's history never sees any of the task's intermediate reasoning.

```rust
let research = session.task(
    "Read the files in src/auth/ and produce a complete summary of the public \
     interface surface: every public function, its signature, its documented \
     behavior, and any preconditions or invariants the caller must respect.",
    TaskOptions::new().role("code-reader"),
)?;

let plan = session.prompt(format!(
    "Here is the auth module's complete public surface:\n\n{}\n\n\
     Now draft an implementation plan for adding OAuth2 PKCE support \
     that does not break any of the existing public API contracts. \
     List every function you'll need to add or modify, and explain \
     the sequencing.",
    research.text()
))?;
```

- the research task runs in isolation. its entire reasoning chain.
- every intermediate observation the model made about the code, every "wait, let me check this file too" , stays inside the task.
- the parent session gets one clean summary. that's all it ever sees.why this matters in practice: when you run exploratory analysis directly inside a long-running session, the history fills with intermediate tool calls, partial answers, and model reasoning about things that are no longer relevant.
- the model anchors on that noise when it shouldn't. compaction eventually fires and loses context you actually needed. tasks are the surgical fix.

the rule: if the sub-problem has a clear deliverable and doesn't need the parent's conversation history to complete, make it a task. the threshold for "make it a task" is lower than you think.

for parallel analysis across a codebase : the cartographer pattern , fan tasks out and collect results:

```rust
let src = PathBuf::from("src");
let mut sections = Vec::new();

for entry in session.readdir(&src)?.into_iter().filter(|e| e.is_dir) {
    let child = session.task_with_id(
        format!("module-{}", entry.name),
        format!(
            "Summarize the public surface of src/{name}. \
             List: all exported types and their purpose, all public functions \
             with signatures, cross-module imports this module depends on, \
             and any global state or shared resources it touches.",
            name = entry.name,
        ),
        TaskOptions::new().role("module-summarizer"),
    )?;
    sections.push(format!("## {}\n\n{}\n", entry.name, child.text()));
}

session.write("ARCHITECTURE.md", &sections.join("\n"))?;
```

each task is clean. each task is focused on exactly one directory. the parent session collects the results and writes the final document.

if you have 12 modules, you run 12 focused tasks, each starting with zero baggage from the others.

## roles and skills: shaping behavior without recompiling

1. roles live in .agentic-harness/roles/. skills live in .agents/skills/. both are auto-discovered when the harness starts.
2. roles are system-prompt overlays scoped to a call. applied at call time and discarded after. they don't persist into message history. they don't accumulate across calls.

> **the precedence chain: call role > session role > agent role > no role.**

```rust
// agent-level default
AgentDefinition::webhook("reviewer", handler)
    .with_role("code-reviewer")

// session-level override for multi-step work
let session = ctx.session_with_id(ctx.id())
    .with_role("senior-reviewer");

// call-level override for one specific prompt within a session
let result = session.prompt_with_options(
    "Explain what this function does in plain English.",
    PromptOptions::new().role("explainer"),
)?;
what a role file looks like:
<!-- .agentic-harness/roles/code-reviewer.md -->
---
model: anthropic/claude-opus-4-7
---

you are a senior software engineer reviewing a pull request for a rust codebase.

focus on:
- correctness: does the code do what the commit message claims?
- error handling: are all error paths handled, not just the happy path?
- security: injection risks, auth bypass conditions, improper secret handling
- readability: will the next developer understand this change in six months?

do not comment on formatting, whitespace, or variable naming conventions.
do not suggest micro-optimizations unless they affect correctness.
be specific: when you flag a problem, cite the exact file and line number,
explain why it matters, and suggest the minimal change that fixes it.
```

- the model frontmatter is optional but useful. it lets you route specific roles to specific models.
- your explainer role runs on claude-sonnet-4-6 for speed and cost. your security-auditor runs on claude-opus-4-7 for depth. you configure this once in the role file and never think about it again.
- skills are behavior descriptor files the model reads at the start of a session.
- they're markdown files in .agents/skills/. the harness finds them automatically. you don't register them anywhere.

> **the practical use: a skills library alongside your codebase describes how you work. commit message format, preferred libraries, migration naming conventions, API design patterns, testing requirements.**

> **the model reads this before every session. you edit the markdown. behavior updates on the next run. no recompile.**

```markdown
<!-- .agents/skills/commit-style.md -->

when writing commit messages for this repository:

- use conventional commits: feat:, fix:, chore:, docs:, refactor:, test:
- keep the subject line under 72 characters, present tense imperative
- if the change touches more than one module, list them in the body with
  a one-sentence explanation for each
- never use "update" or "changes" as the entire message — be specific about
  what changed and why

examples of good commit messages:
  feat(auth): add PKCE flow to OAuth2 client
  fix(payments): handle stripe webhook signature mismatch on retry
  chore(deps): upgrade tokio to 1.38 for async-trait compatibility
  refactor(sessions): extract compaction logic into standalone module
```

the model reads this. it writes commits that match your convention. you don't remind it every session. you maintain one file.

## the coding agent loop in full detail

the coding agent loop is the primary use case the CLI was built around. it's also where the most things can go wrong if you misconfigure it.

the full command with all the options that matter:

```bash
agentic-harness code --workspace . --llm auto \
  --prompt "Add a --dry-run flag to the deploy command that prints \
            the complete list of changes that would be made without \
            actually making them. The flag should work with all three \
            deploy subcommands: prod, staging, and preview." \
  --deny-path .env \
  --deny-path .agentic-harness/secrets/ \
  --deny-path config/production.yaml \
  --approve-dependencies \
  --commit "feat(deploy): add --dry-run flag to all deploy subcommands" \
  --pr
```

what each flag does and why it matters:

1. \--workspace . sets the root. all file operations are sandboxed here. the agent cannot read or write outside this path, enforced at the harness level — not by trusting the model to self-restrict.
2. \--llm auto selects the model from defaultModel in your runtime config. use --llm anthropic/claude-opus-4-7 for complex tasks that need deep reasoning, or --llm anthropic/claude-sonnet-4-6 for faster iteration.
3. \--deny-path is a hard block. it matches prefix-style, so --deny-path config/ covers everything under config/. audit your workspace before the first run and enumerate every path that holds secrets or production config — not just .env.
4. \--approve-dependencies allows Cargo.toml modifications without a human approval step. leave this out if you want to review every new crate before it gets added.
5. \--commit auto-stages all changes and commits them at the end of a successful run with the message you provide. without this flag, changes land as unstaged modifications for you to review.
6. \--pr opens a pull request from the commit. requires a clean git state before the run and a real branch, not a detached HEAD.

> **the loop itself: Inspect → Brief → LLM + Tools → Edit + Test → Commit · PR.**

- **inspect**: reads the workspace structure, loads skills and roles, identifies the files most likely relevant to the prompt.
- writes its understanding to coding-brief.md before touching any code.
- **brief**: the model commits to a plan. you can read .agentic-harness/runs/<id>/coding-brief.md mid-run to see what it decided.
- if the brief looks wrong, kill the run. it's cheaper to restart with a clearer prompt than to let the agent execute a bad plan.
- **LLM + tools**: the edit-test loop. the model makes changes, runs the test suite, reads the output, makes more changes. iterates until tests pass, the iteration limit is hit, or it decides the task is complete.

> **commit · PR: stages, commits, pushes, opens the PR with the diff attached.**

**every run writes six artifacts to .agentic-harness/runs/<id>/:**

1. coding-brief.md : the plan the agent committed to before writing any code
2. summary.md : human-readable account of what was done, what was tried, and why
3. run.json :structured metadata: model used, total duration, input/output token counts, iteration count, final exit status
4. events.jsonl : every single tool call in order with full inputs and outputs, for debugging what went wrong
5. diff.patch : the complete diff of all file changes
6. checks.json : final test and lint results that determined success or failure

## Tips to Remember

- treat these as structured logs, not ephemeral output. i commit run artifacts to the repo for any task i need to be able to reproduce.
- the run.json alone 2KB , tells you the model, the token costs, and whether it succeeded. the events.jsonltells you exactly what the agent did and in what order when you need to debug a bad run.

for CI, the pattern is:

```bash
# .github/workflows/agent-task.yml
- name: checkout on real branch
  run: git checkout -b "agent/task-${{ github.run_id }}"

- name: run coding agent
  run: |
    agentic-harness code \
      --workspace . \
      --llm auto \
      --prompt "$(cat .agentic-harness/current-task.md)" \
      --deny-path .env \
      --deny-path config/production.yaml \
      --commit "chore: automated task run-${{ github.run_id }}" \
      --pr \
      --output-json > result.json
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

- name: check result
  run: cat result.json | jq '.success, .pr_url, .token_costs'
--output-json writes a structured summary to stdout. your pipeline can parse it to determine success, extract the PR URL, log token costs, or gate on test results.
```

## HttpSessionEnv: running the binary locally, executing remotely

- this is the capability i took the longest to fully understand. i use it on almost every task that touches infrastructure now.
- the agent binary runs on your machine or in CI. the filesystem and shell operations execute inside a remote sandbox.
- the agent doesn't know or care which environment it's in.

**use agentic\_harness::HttpSessionEnv;**

```rust
let sandbox = HttpSessionEnv::new(
    std::env::var("SANDBOX_URL")?,
    "/workspace"  // root path inside the sandbox
)
.header("Authorization",
    format!("Bearer {}", std::env::var("SANDBOX_TOKEN")?));

let session = ctx.session_with_id_and_env("repro-task", sandbox);
from this point, every file and shell operation goes through HTTP to the sandbox. the call sites look identical to local:
// these execute remotely despite looking like local calls
session.shell("git clone https://github.com/my-org/my-repo /workspace/repo")?;
session.shell("cd /workspace/repo && git checkout the-failing-branch")?;
session.shell("cd /workspace/repo && cargo build 2>&1")?;

let test_output = session.shell(
    "cd /workspace/repo && cargo test --no-fail-fast 2>&1 | tail -200"
)?;

session.write(
    "/workspace/repro-report.md",
    &format!(
        "## reproduction report\n\nbranch: the-failing-branch\nexit code: {}\n\n\n{}\n\n",
        test_output.status,
        test_output.stdout
    )
)?;

let report = session.read("/workspace/repro-report.md")?;
```

the wire protocol is JSON over HTTP. every operation :

1. exec
2. read
3. write
4. edit
5. grep
6. glob
7. stat
8. readdir
9. mkdir
10. rm has a defined request/response shape.

**any sandbox that implements this protocol works as an HttpSessionEnv target.**

**to wire up a named sandbox:**

```bash
agentic-harness setup sandbox --target e2b --endpoint $SANDBOX_URL
agentic-harness sandbox exec "uname -a && rustc --version" --json
```

the built-in connectors handle auth and lifecycle boilerplate for Vercel Sandbox, Daytona, and E2B:

```rust
// after running \`agentic-harness add e2b | claude\` to generate the connector
let sandbox = SandboxConnector::e2b(
    std::env::var("E2B_SANDBOX_URL")?,
    std::env::var("E2B_API_KEY")?,
)?;

let session = ctx.session_with_id_and_env("isolated-repro", sandbox);
```

- the concrete use case i use this for most: reproducing CI failures in a clean Linux environment.
- the agent clones the repo at the exact failing commit hash, runs the exact failing test command, reads the full output, diagnoses the failure, and writes a report.
- i read the report. i never touched my local machine. the sandbox is discarded when the session ends.

**the performance thing nobody warns you about: every shell call over HttpSessionEnv is a network round trip. tight loops : edit, test, check output, edit : accumulate latency fast.**

a 40-iteration loop that takes 5 seconds locally takes several minutes against a remote sandbox if each iteration makes three separate shell calls.

the fix: batch shell work into scripts.

```rust
// write this to the sandbox before the loop
session.write("/workspace/agent-check.sh", r#"
#!/bin/bash
set -e
cd /workspace/repo
cargo fmt --check 2>&1
cargo clippy -- -D warnings 2>&1
cargo test --no-fail-fast 2>&1 | tail -100
"#)?;
session.shell("chmod +x /workspace/agent-check.sh")?;

// now each iteration is one call, not three
let result = session.shell("/workspace/agent-check.sh")?;
```

one call per iteration instead of three. write the script once, run it repeatedly. the latency difference on a 40-iteration loop is real.

## build targets: same codebase, three deployment shapes

```bash
agentic-harness build --target native      # self-contained binary + manifest.json
agentic-harness build --target node        # native binary wrapped by node server.mjs
agentic-harness build --target cloudflare  # Cloudflare Worker boundary + WASM adapter
```

native is the default. one binary. one manifest. nothing else on the target machine. runs anywhere that can execute a native Linux binary.

node is for hosting platforms that require a Node entrypoint. the build generates server.mjs that starts the native rust binary as a child process and proxies HTTP to it. the agent logic still runs as rust. the Node layer is a 30-line HTTP shim.

## Cloudflare is for edge deployment.

- the build generates a Worker boundary file and links a Worker-compatible app adapter.
- handlers compile to WASM via the WASM JSON ABI.
- Durable Object bindings handle session persistence via Cloudflare KV.

the important constraint about Cloudflare: Workers don't support long-running shell commands. they don't have a real filesystem.

they don't support cargo or any build tooling. --target cloudflare is for webhook handling, route metadata, small control endpoints, and Durable Object routing , not for coding work.

for anything that needs to run cargo test, delegate to a native process or remote sandbox.

the practical decision matrix:

- shipping an agent as an API that other services call → native behind nginx or a managed platform
- hosting on Railway, Render, or a platform that expects Node → node
- webhook ingestion, lightweight routing, Durable Object state management → cloudflare
- everything else → native

## schema-guided output: typed rust structs from model responses

asking the model to return JSON and hoping it does is half the solution.

having the harness extract, validate, and deserialize it into your rust struct is the full solution.

```rust
#[derive(Deserialize)]
struct SecurityAudit {
    vulnerabilities: Vec<Vulnerability>,
    severity: Severity,
    immediate_action_required: bool,
    recommended_fix: String,
}

#[derive(Deserialize)]
struct Vulnerability {
    file: String,
    line: Option<u32>,
    category: String,
    description: String,
}

#[derive(Deserialize)]
#[serde(rename_all = "lowercase")]
enum Severity { Low, Medium, High, Critical }

let audit: SecurityAudit = session.prompt_json_with_options(
    "Review the authentication module for security vulnerabilities. \
     Specifically look for: SQL/command injection risks, auth bypass conditions, \
     improper secret handling in logs or error messages, and missing input validation.",
    PromptOptions::new().result_schema(json!({
        "type": "object",
        "required": ["vulnerabilities", "severity",
                     "immediate_action_required", "recommended_fix"],
        "properties": {
            "vulnerabilities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["file", "category", "description"],
                    "properties": {
                        "file": { "type": "string" },
                        "line": { "type": "integer" },
                        "category": { "type": "string" },
                        "description": { "type": "string" }
                    }
                }
            },
            "severity": { "enum": ["low", "medium", "high", "critical"] },
            "immediate_action_required": { "type": "boolean" },
            "recommended_fix": { "type": "string" }
        }
    })),
)?;

// now audit is a typed rust struct — not a string, not a Value
if audit.immediate_action_required {
    let body = format!(
        "severity: {:?}\n\n{}\n\nvulnerabilities:\n{}",
        audit.severity,
        audit.recommended_fix,
        audit.vulnerabilities.iter()
            .map(|v| format!("- {}: {} ({})", v.file, v.description, v.category))
            .collect::<Vec<_>>()
            .join("\n")
    );
    session.shell(&format!(
        "gh issue create --title 'security: {} vulnerabilities found in auth module' \
         --label security --label priority-high --body '{}'",
        audit.vulnerabilities.len(),
        body.replace("'", "\\'")
    ))?;
}
```

the model can return reasoning prose alongside the typed payload in the same response. the harness extracts the result block between

- \--RESULT\_START--- and ---RESULT\_END--- markers. you get a rust struct. compile-time type safety from model output to your handler logic.
- the schema does two things: it tells the model what shape to produce, and it gives the harness something to validate against before deserialization.
- if the model returns something that doesn't match the schema, you get PromptError::SchemaValidationFailed instead of a panic three call sites later when you access a missing field.

## MCP tools: reaching outside the sandbox

when the agent needs capabilities beyond file and shell, connect\_mcp is the escape hatch.

```rust
use agentic_harness::McpServerOptions;

let sentry = ctx.connect_mcp(
    "sentry",
    McpServerOptions::new("https://mcp.sentry.io/mcp")
        .header("Authorization",
                format!("Bearer {}", std::env::var("SENTRY_TOKEN")?)),
)?;

let session = ctx.session_with_id(ctx.id()).with_tools(sentry);

let analysis = session.prompt(
    "Find the highest-volume new error in the last 24 hours. \
     For each occurrence, find the file and line number in our codebase. \
     Search the git log for the commit that introduced that code path. \
     Draft a root cause analysis and a hot-fix plan with explicit rollback steps.",
)?;
```

the agent gets the MCP server's full tool set. no tool definitions to write. descriptions come from the server. the model decides when to call which tool based on those descriptions.

you can wire multiple MCP servers to one session:

```rust
let sentry = ctx.connect_mcp("sentry",
    McpServerOptions::new("https://mcp.sentry.io/mcp")
        .header("Authorization", format!("Bearer {}", std::env::var("SENTRY_TOKEN")?)))?;

let linear = ctx.connect_mcp("linear",
    McpServerOptions::new("https://mcp.linear.app/mcp")
        .header("Authorization", format!("Bearer {}", std::env::var("LINEAR_TOKEN")?)))?;

let session = ctx.session_with_id(ctx.id())
    .with_tools(sentry)
    .with_tools(linear);

// the agent can read Sentry errors AND create Linear issues in one session
let result = session.prompt(
    "Find the top 3 errors from the last hour, ranked by volume. \
     For each one, create a Linear issue in the Infrastructure project \
     with priority High. Set the title to the error message and include \
     the stack trace in the description."
)?;
```

- the model calls tools based on their descriptions. a vague description like "search sentry" gets called inconsistently.
- a description that says "call this before responding to any question about errors, incidents, or production issues" gets called reliably.
- if you control the MCP server, write prescriptive descriptions : tell the model when to call, not just what it returns.

## connectors: generating adapters instead of writing them

instead of writing adapter code by hand against an unfamiliar API, pipe a connector recipe to your coding agent:

```bash
agentic-harness add                            # list available connectors
agentic-harness add daytona | claude           # pipe recipe to Claude Code
agentic-harness add e2b     | codex            # pipe recipe to Codex
agentic-harness add https://e2b.dev/docs \
  --category sandbox | claude                  # pipe raw docs + category hint
```

- the connector recipe is a structured description of the sandbox API and the SessionEnv contract it needs to satisfy.
- the coding agent reads it, writes the rust adapter module, handles authentication, wraps the provider lifecycle, and exposes it as an HttpSessionEnv.
- you review the diff. you merge it. the adapter lives in your project. it's your code now.

i wired Daytona using this in about 20 minutes including the full review cycle. the agent got the auth header format right on the first pass.

writing the adapter from scratch against the Daytona docs would have taken most of an afternoon and at least two wrong assumptions about the refresh token flow.

**once the connector is generated:**

```rust
// after \`agentic-harness add daytona | claude\` generates your connector
let sandbox = DaytonaSandboxConnector::new(
    std::env::var("DAYTONA_API_URL")?,
    std::env::var("DAYTONA_API_KEY")?,
)?;
let session = ctx.session_with_id_and_env("task-id", sandbox);
```

## automatic compaction: handling long sessions without losing context

long-running sessions accumulate history.

eventually they overflow the model's context window.

the harness handles this automatically, but you need to configure it correctly or you'll lose context at exactly the wrong moment.

```rust
let response = session.prompt_with_options(
    "Continue implementing the remaining endpoints from the plan.",
    PromptOptions::new().compaction(
        CompactionSettings::new()
            .context_window_tokens(128_000)   // full window for your model
            .reserve_tokens(16_384)           // headroom reserved for the response
            .keep_recent_messages(12),        // tail messages preserved verbatim
    ),
)?;
```

context\_window\_tokens is the total budget for the session.

- reserve\_tokens is what you hold back for the model's response. the effective limit for history is context\_window\_tokens - reserve\_tokens.
- keep\_recent\_messages is the number of messages at the tail that are always preserved verbatim regardless of compaction.

when history exceeds the budget, the harness asks the model to summarize everything between the system prompt and the kept tail.

that summary replaces the middle section. the tail messages remain intact. the compacted session is smaller and the next call fits within budget.

> **the tradeoff is real: summaries lose precision. a specific decision made 50 messages ago : "we chose authlib because it's the only library with PKCE support that works with axum's middleware model" : might survive as "we chose authlib for auth" in the summary.**

**if that precision is load-bearing for decisions later in the session, store it explicitly:**

```rust
// write important decisions to files before they might get compacted away
session.write(
    ".agentic-harness/decisions.md",
    "## auth library\n\nchose authlib over fastapi-users.\n\
     reason: only library with PKCE support compatible with axum middleware.\n\
     do not revisit this decision.\n\n"
)?;
```

- write decisions to files. files survive compaction. the model can read them back on demand. history doesn't need to carry everything if the workspace does.
- run agentic-harness doctor to see your model's actual reported context window. set context\_window\_tokens to 80-90% of that value.
- the token counter isn't perfectly accurate on the model side, and a single large file read can push you over if you're sitting at 99%.

## What to watch out for

**1\. session history contamination**

- problem: exploratory analysis inside a long session poisons later prompts with noise from the exploration phase
- fix: use tasks. task history never touches the parent. the threshold for "make it a task" is lower than you think

**2\. role precedence surprises**

- problem: a call-level role shadows the session role. the model behaves differently than expected and you don't know why
- fix: session role sets identity. call role narrows focus. they layer — the call role adds, it shouldn't cancel

**3\. --deny-path gaps**

- problem: you deny .env. your secrets also live in .env.local and config/staging.yaml. the agent reads one of them
- fix: deny prefixes, not filenames. --deny-path config/ covers everything under it

**4\. detached HEAD in CI**

- problem: the agent edits, tests pass, commit fails — because there's no branch to commit to
- fix: git checkout -b agent-run-$RUN\_ID before invoking the harness

**5\. HttpSessionEnv latency in tight loops**

- problem: 40 iterations at three shell calls each is minutes of pure network latency
- fix: write [agent-check.sh](https://agent-check.sh/) that does everything in one invocation. one call per iteration

**6\. context budget underestimation**

- problem: compaction fires mid-task. the model loses its plan and starts improvising from the summary
- fix: run agentic-harness doctor to get the actual window. set budget to 80-90% of that

**7\. runtime config loaded after handler registration**

- problem: a handler runs before load\_workspace\_context(). no model registered. the error looks nothing like a config problem
- fix: always call load\_workspace\_context() in app() before wiring any agents

**8\. --llm auto changing between runs**

- problem: defaultModel gets updated. two runs six months apart aren't comparable. you can't reproduce the first one
- fix: pin the model in runtime.json for anything that needs reproducibility

**9\. deleting run artifacts**

- problem: you clean runs/ in a gitignore rule. three weeks later you need to reproduce a regression and everything's gone
- fix: commit run artifacts for any task you need to reproduce. run.json is 2KB. keep it

## things i'd do differently

1. run agentic-harness guide before touching anything.
2. write session-level tests before writing handler logic.
3. use tasks for everything that has a sub-deliverable.
4. pin the model from the first serious run.
5. store decisions in files, not in session history.
6. batch shell operations from the start when using remote sandboxes**.**

## the bottom line

most agent frameworks are wrappers around an API call. this is a runtime.

a wrapper solves "make the model respond." a runtime solves "ship an agent to production and keep it working after the model changes, after the sandbox changes, after the codebase changes, after the session runs for two hours and overflows the context window."

**the 3-layer architecture**

1. your code
2. the harness
3. the execution target

is what makes that possible. you write handlers. the harness absorbs all the operational complexity. the execution target is a config choice.

the things that don't change: handler logic, session structure, task patterns, role definitions, skill files. the things that do change: models, providers, sandbox vendors, deploy targets.

the architecture is designed so the things that change never touch the things that don't.

that's the bet. it's the right bet.

hope you enjoyed reading this and exploring how I build for agents and in general ❣️

## Disclaimers

This article was researched and written by the author, edited by Minimax-M2.7 The thumbnail was taken off Pinterest.

Harrison Chase "memory should be open!" —

[https://x.com/hwchase17/status/2046308913939919232Harrison](https://x.com/hwchase17/status/2046308913939919232Harrison)

Chase :"Your Harness, Your Memory" —

[https://www.langchain.com/blog/your-harness-your-memory](https://www.langchain.com/blog/your-harness-your-memory)

Vivek Trivedi :"The Anatomy of an Agent Harness" —

[https://www.langchain.com/blog/the-anatomy-of-an-agent-harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)