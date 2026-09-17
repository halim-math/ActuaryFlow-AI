# Tool protocol

Every callable tool has a stable name, description, validated argument object, and structured result. Tools are registered explicitly and checked against an allow-list before execution.

A production audit record should include:

- request and session IDs;
- tool name and version;
- normalized arguments;
- units and currency where relevant;
- result and error state;
- formula/model identifier;
- execution duration;
- upstream evidence IDs;
- caller/model version;
- timestamp and configuration hash.

The model must never be asked to perform a calculator's arithmetic when an approved deterministic tool exists. Likewise, the tool result does not decide whether coverage applies: it is one input to a human-governed workflow.

Network-capable tools should have explicit domains, timeouts, response-size limits, secret isolation, and prompt-injection-safe parsing.
