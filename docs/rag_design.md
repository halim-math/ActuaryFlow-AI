# Policy RAG research design

ActuaryFlow-AI treats retrieval as an auditable evidence subsystem rather than a generic chat memory. Every passage has a document identity, chunk identity, source offsets, metadata, and score. The agent receives evidence but must not silently convert a retrieved passage into a final coverage decision.

## Pipeline

1. ingest versioned policy/handbook text;
2. fingerprint source content;
3. split with deterministic overlap;
4. attach jurisdiction, product, effective-date, and source metadata;
5. retrieve candidates;
6. apply metadata constraints before or during ranking;
7. preserve chunk IDs and excerpts as citations;
8. measure Recall@k, MRR, nDCG, abstention quality, and citation validity;
9. escalate when evidence is missing, contradictory, stale, or below threshold.

## Research baselines

The repository includes a dependency-free lexical baseline because it is transparent and reproducible. A production experiment can add dense embeddings and hybrid reciprocal-rank fusion. The lexical baseline remains useful as a control and as a fallback when an embedding service is unavailable.

## Failure modes

Important failure modes include wrong policy version, cross-jurisdiction leakage, retrieving an exclusion without its exception, orphaned endorsements, chunk boundary loss, semantic near-matches with different legal effect, and high model confidence despite low evidence confidence.

Retrieval metrics therefore must be evaluated separately from answer-generation metrics.
