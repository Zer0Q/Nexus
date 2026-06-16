---
type: Concept
title: iron-proxy
description: '- SHA-256 verified binary download - Managed daemon mode - Tokens are
  useless outside the proxy - Composes with Bitwarden Secrets Manager'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# iron-proxy

A network-level egress firewall for AI agent sandboxes. Instead of injecting real API keys into the agent's environment, iron-proxy gives the agent opaque proxy tokens. It intercepts outbound requests at the network boundary, swaps tokens for real credentials, and forwards the request — the sandbox never holds the actual key.

- SHA-256 verified binary download
- Managed daemon mode
- Tokens are useless outside the proxy
- Composes with Bitwarden Secrets Manager

See also: [[concepts/Iron-Proxy-Egress-Firewall]], [[concepts/Bitwarden-Secrets-Manager]]
