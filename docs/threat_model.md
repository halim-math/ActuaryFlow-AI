# Threat model

## Assets

Policy wording, customer/claim data, actuarial assumptions, model configuration, API credentials, audit records, reviewer decisions, and notification channels.

## Representative threats

- prompt injection in user input or retrieved documents;
- retrieval poisoning or stale policy versions;
- cross-tenant data leakage;
- tool argument manipulation;
- secret leakage into prompts or logs;
- SSRF or unrestricted network tools;
- forged citations;
- replayed or tampered review events;
- unauthorized reviewer actions;
- denial-of-service through large documents or tool loops;
- supply-chain compromise of dependencies or model endpoints.

## Controls

Treat retrieved content as untrusted data, keep tools allow-listed and schema constrained, isolate secrets, validate outbound destinations, apply least privilege, sign/hash audit chains, require human authority checks, cap resource use, scan dependencies, and maintain reproducible red-team regression cases.
