# Retrieval evaluation protocol

Evaluate retrieval before evaluating generated prose. Maintain a small gold set whose query records identify relevant chunk IDs and policy versions.

## Metrics

- Recall@k: whether relevant evidence appears in the top-k candidates.
- MRR: reciprocal rank of the first relevant item.
- nDCG@k: rank-sensitive relevance when multiple passages are useful.
- metadata leakage rate: retrieval from an invalid jurisdiction/product/version.
- citation validity: cited chunk IDs exist and excerpts match source text.
- abstention precision/recall: whether the system escalates when evidence is insufficient.

## Splits

Separate straightforward clause lookup, paraphrased questions, multi-clause reasoning, endorsement conflicts, distractor-heavy cases, adversarial prompt injection in documents, and intentionally unanswerable questions.

Do not optimize the test set through repeated prompt edits. Record configuration hashes, corpus hashes, random seeds, and model versions for every evaluation run.
