# Fairness evaluation

Group metrics are diagnostic evidence, not a stand-alone declaration that a system is fair. Relevant groups, outcomes, time windows, sample sizes, confounders, business processes, legal constraints, and error costs must be defined for the concrete insurance use case.

Evaluate both model behavior and the surrounding workflow: retrieval quality, missingness, escalation rates, reviewer overrides, tool errors, and downstream outcomes can differ across groups even when the LLM prompt is identical.

Do not infer protected characteristics from unrelated personal data merely to create a metric. Where protected-attribute analysis is legally and ethically appropriate, use governed data access and aggregate reporting. Small samples should be suppressed or accompanied by uncertainty intervals.

The included rate-gap helper is intentionally descriptive and should not be used as an automated underwriting or claims rule.
