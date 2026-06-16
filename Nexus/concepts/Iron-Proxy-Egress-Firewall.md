---
type: Concept
title: Iron Proxy Egress Firewall
description: Network-level credential protection for Hermes Agent sandboxes. Instead
  of injecting real API keys into the sandbox, Hermes gives the agent opaque proxy
  toke...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Iron Proxy Egress Firewall

## Definition
Network-level credential protection for Hermes Agent sandboxes. Instead of injecting real API keys into the sandbox, Hermes gives the agent opaque proxy tokens. iron-proxy intercepts outbound requests at the network boundary, swaps tokens for real credentials, and forwards the request. The sandbox never holds the actual key.

## Why It Matters
If the sandbox is compromised, the attacker only gets proxy tokens that work exclusively from behind the proxy. Real credentials never touch the agent's execution environment, dramatically reducing the blast radius of a breach.

## Key Ideas
- `hermes egress install` — downloads iron-proxy binary, SHA-256 verified
- `hermes egress setup` — interactive configuration wizard
- `hermes egress start` — spawns managed proxy daemon
- `hermes egress setup --from-bitwarden` — pull real credentials from BSM at proxy startup
- Agent gets opaque proxy tokens, not real API keys
- iron-proxy intercepts at network boundary, swaps for real credential, forwards request
- Compromise the sandbox → attacker gets tokens useless outside the proxy
- Composes with [[concepts/Bitwarden-Secrets-Integration]]: rotate in Bitwarden, propagates to all sandboxes automatically

## Tradeoffs
- Adds network hop latency to every API call
- Requires proxy daemon to be running
- Overkill for personal use — designed for production agents touching sensitive systems

## Related
- [[concepts/Bitwarden-Secrets-Integration]] -- Layer 1 of the security stack
- [[concepts/Local-AI-Privacy]] -- broader data security context
- [[concepts/Agent-Profiles]] -- each profile can have its own egress configuration

## Source
[[summaries/IBuzovskyi-Hermes-Agent-Complete-Guide]]
