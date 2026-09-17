from actuaryflow.rag.document import PolicyDocument
from actuaryflow.rag.splitter import split_document


def test_split_document_preserves_source_identity() -> None:
    document = PolicyDocument(document_id="p1", title="Policy", text="a" * 2500)
    chunks = split_document(document, chunk_size=1000, overlap=100)
    assert len(chunks) == 3
    assert all(chunk.document_id == "p1" for chunk in chunks)
    assert chunks[1].start_char == 900


def test_splitter_rejects_invalid_overlap() -> None:
    document = PolicyDocument(document_id="p1", title="Policy", text="text")
    try:
        split_document(document, chunk_size=100, overlap=100)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
