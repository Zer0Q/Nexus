# Bitwarden Secrets Integration

## Definition
Credential management layer for production Hermes agents using Bitwarden Secrets Manager. One bootstrap token in .env, all real credentials live in Bitwarden. Every Hermes instance pulls secrets at startup; rotate a key once in the web app and every instance picks it up on next restart.

## Why It Matters
Eliminates the security risk of embedding API keys and credentials in config files. Centralized credential management with instant revocation and propagation across the entire agent fleet.

## Key Ideas
- `hermes secrets bitwarden setup` — wizard installs bws, prompts for token
- `hermes secrets bitwarden status` — verify connection
- `hermes secrets bitwarden sync` — dry-run to see what gets applied
- One bootstrap token in .env, all real credentials in Bitwarden
- Rotate a key in the web app → every instance picks it up on next restart
- Instant revocation from the web UI
- Free tier available

## Tradeoffs
- Requires Bitwarden account setup
- Adds a dependency on Bitwarden's availability at startup
- Overkill for personal single-agent use

## Related
- [[Iron-Proxy-Egress-Firewall]] -- Layer 2 of the security stack; composes with Bitwarden
- [[Agent-Profiles]] -- each profile pulls secrets independently
- [[Local-AI-Privacy]] -- broader context of data security

## Source
[[IBuzovskyi-Hermes-Agent-Complete-Guide]]
