# Bitwarden Secrets Manager

A credential management service that stores API keys, tokens, and sensitive configuration outside of application code. Hermes Agent integrates with it so one bootstrap token lives in .env while all real credentials live in Bitwarden, with automatic propagation across agent instances on restart.

- Free tier available
- Instant revocation from the web UI
- Rotate a key once, every instance picks it up on next restart
- Composes with [[Iron-Proxy-Egress-Firewall]] for two-layer security

See also: [[Bitwarden-Secrets-Integration]]
