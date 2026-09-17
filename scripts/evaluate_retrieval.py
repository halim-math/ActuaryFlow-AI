from __future__ import annotations

import json
from pathlib import Path

from actuaryflow.rag.loader import load_text_policy
from actuaryflow.rag.retrieval import PolicyRetriever
from actuaryflow.rag.splitter import split_document


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    chunks = []
    document_names: dict[str, str] = {}
    for path in sorted((ROOT / "data" / "policies").glob("*.md")):
        document = load_text_policy(path)
        document_names[document.document_id] = path.stem
        chunks.extend(split_document(document))
    retriever = PolicyRetriever(chunks)

    total = 0
    hits = 0
    with (ROOT / "eval" / "retrieval_queries.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            case = json.loads(line)
            expected = case["relevant_document"]
            if expected is None:
                continue
            total += 1
            results = retriever.search(case["query"], k=5)
            returned = {document_names.get(str(item["document_id"])) for item in results}
            hits += int(expected in returned)
    print(json.dumps({"recall_at_5": hits / total if total else 0.0, "cases": total}, indent=2))


if __name__ == "__main__":
    main()
