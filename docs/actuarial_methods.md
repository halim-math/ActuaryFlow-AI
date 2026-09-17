# Actuarial methods

The quantitative layer is deliberately composed of small deterministic functions that can be tested independently from an LLM. Tool calls should include input arguments, formula identity, result, units, assumptions, and timestamp in the audit trail.

Implemented research baselines include frequency-severity pricing, expense-loaded indicated premium, loss and combined ratios, pure premium, limited-fluctuation credibility, chain-ladder development, excess-of-loss transformation, discounting, empirical severity summaries, reproducible compound-Poisson simulation, and tail-risk measures.

These routines are examples rather than filing-ready actuarial models. Real use requires appropriate exposure definitions, trend/on-level treatment, development diagnostics, segmentation, parameter uncertainty, data-quality controls, model governance, regulatory review, and qualified actuarial judgment.

## LLM boundary

The language model should choose only from an allow-list of tools. It must not invent calculator results. The numerical function result is authoritative for the specific supplied inputs; the model's role is to explain it and surface assumptions.
