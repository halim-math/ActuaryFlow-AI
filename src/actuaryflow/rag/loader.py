from __future__ import annotations

from hashlib import sha256
from pathlib import Path

from .document import PolicyDocument


def load_text_policy(path: str | Path, *, jurisdiction: str | None = None, product_line: str | None = None) -> PolicyDocument:
    source = Path(path)
    text = source.read_text(encoding="utf-8")
    digest = sha256(text.encode("utf-8")).hexdigest()[:16]
    return PolicyDocument(
        document_id=f"policy-{digest}",
        title=source.stem.replace("_", " ").title(),
        text=text,
        source_uri=str(source),
        jurisdiction=jurisdiction,
        product_line=product_line,
        metadata={
            "jurisdiction": jurisdiction or "unspecified",
            "product_line": product_line or "unspecified",
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
        },
    )
