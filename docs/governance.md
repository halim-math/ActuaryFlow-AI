# Governance operating model

ActuaryFlow-AI is designed as a human-governed decision-support system. The AI can organize evidence, retrieve policy text, call approved actuarial tools, draft explanations, and surface inconsistencies. Authority for consequential insurance decisions remains with appropriately authorized people.

## Control layers

1. **Input controls** - validation, size limits, prompt-injection signals, tenant/session boundaries.
2. **Evidence controls** - source provenance, versioning, metadata filters, citation validation.
3. **Tool controls** - allow-list, typed arguments, deterministic calculations, timeout/error handling.
4. **Decision controls** - deterministic escalation rules and financial authority thresholds.
5. **Human controls** - named reviewer, role/authority checks, reasoned override record.
6. **Audit controls** - append-only events, redaction, configuration/model identifiers, hashes.
7. **Evaluation controls** - offline benchmark suites, red-team cases, regression gates, drift monitoring.

Production deployment still requires organization-specific legal, compliance, privacy, security, actuarial, and operational review.
