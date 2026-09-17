from __future__ import annotations


def accuracy(expected: list[bool], actual: list[bool]) -> float:
    if len(expected) != len(actual) or not expected:
        raise ValueError("expected and actual must be non-empty and equal length")
    return sum(e == a for e, a in zip(expected, actual, strict=True)) / len(expected)


def citation_precision(validity: list[bool]) -> float:
    return sum(validity) / len(validity) if validity else 0.0


def review_metrics(expected_review: list[bool], predicted_review: list[bool]) -> dict[str, float]:
    if len(expected_review) != len(predicted_review):
        raise ValueError("arrays must have equal length")
    tp = sum(e and p for e, p in zip(expected_review, predicted_review, strict=True))
    fp = sum((not e) and p for e, p in zip(expected_review, predicted_review, strict=True))
    fn = sum(e and (not p) for e, p in zip(expected_review, predicted_review, strict=True))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}
