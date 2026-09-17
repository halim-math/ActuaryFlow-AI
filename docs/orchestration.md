# Agent orchestration

The runtime follows a state machine rather than an unconstrained autonomous loop:

`request -> guardrails -> intent -> memory -> policy RAG -> approved actuarial tools -> grounded synthesis -> deterministic router -> human review or response -> audit event`

## Why this architecture

Insurance workflows combine natural-language interpretation with policy evidence and quantitative models. The LLM is therefore used as an orchestrator and explainer, not as the source of policy truth or numerical truth. Retrieval supplies traceable evidence; deterministic tools supply calculations; a rules-based router decides whether a qualified human must intervene.

## State

Each request has a unique ID, lifecycle status, bounded conversational context, evidence list, tool results, risk flags, and trace. Risk flags are additive so later stages cannot silently erase an earlier concern.

## Failure handling

A retrieval failure, tool exception, prompt-injection signal, missing evidence, or material ambiguity should produce an auditable escalation path rather than a confident fallback answer.
