# Research branch: agent orchestration

This branch develops the LLM-facing orchestration layer for ActuaryFlow-AI. It includes typed request/response contracts, bounded memory, lifecycle state, intent classification, deterministic planning, prompt-injection signals, an explicit tool registry and allow-list, an escalation router, structured traces, an OpenAI Responses API adapter, offline deterministic test mode, FastAPI entry point, tests, configuration, prompts, examples, and evaluation cases.

The design intentionally separates model reasoning from authoritative policy retrieval and quantitative actuarial calculations. It is built for merge with the RAG/actuarial and governance branches.

Research questions include calibrated escalation, agent reliability under retrieval failures, tool-selection accuracy, citation faithfulness, prompt-injection resilience, and the trade-off between automated assistance and human-review burden.
