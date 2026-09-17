# Research branch: governance and evaluation

This branch builds the control plane around ActuaryFlow-AI: human review cases, authority profiles, deterministic escalation policy, audit hashing, provenance, redaction, notification abstraction, runtime monitoring, fairness diagnostics, risk-register primitives, evaluation metrics, red-team cases, governance regression tests, configuration, and operational templates.

The research objective is not merely higher answer accuracy. It is measurable **selective reliability**: answer when the evidence/tools support an auditable response and escalate when they do not. Core measurements therefore include citation validity, retrieval quality, review precision/recall, prompt-injection control activation, tool failure rates, reviewer override patterns, and subgroup diagnostics.

This branch is designed to merge after or alongside the orchestration and RAG/actuarial branches.
