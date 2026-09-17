# Memory design

Conversation memory is deliberately bounded. The working memory stores recent user/assistant messages needed for continuity, while policy documents remain in the retrieval corpus and should not be copied into durable conversational memory by default.

## Principles

- minimize retention;
- separate user conversation from authoritative policy evidence;
- avoid storing secrets and unnecessary personal data;
- make deletion possible at session boundaries;
- never treat a remembered model statement as a verified fact;
- re-retrieve policy evidence when a later answer depends on it;
- record only the provenance necessary for audit.

The in-memory implementation is a local baseline. Production can replace it with an encrypted store that supports TTLs, tenant isolation, access controls, consent/retention policies, and deletion workflows.
