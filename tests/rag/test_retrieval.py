from actuaryflow.rag.document import PolicyChunk
from actuaryflow.rag.retrieval import PolicyRetriever


def test_retrieval_ranks_matching_chunk() -> None:
    chunks = [
        PolicyChunk("p1", "p1:0", "Fire", "fire damage and smoke are covered", 0, 33),
        PolicyChunk("p2", "p2:0", "Travel", "flight cancellation terms", 0, 25),
    ]
    results = PolicyRetriever(chunks).search("fire smoke coverage", k=2)
    assert results
    assert results[0]["document_id"] == "p1"
    assert float(results[0]["score"]) > 0
