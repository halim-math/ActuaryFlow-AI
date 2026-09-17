from __future__ import annotations

from enum import StrEnum


class Intent(StrEnum):
    POLICY_QUESTION = "policy_question"
    ACTUARIAL_CALCULATION = "actuarial_calculation"
    CLAIM_SUMMARY = "claim_summary"
    UNDERWRITING_SUPPORT = "underwriting_support"
    RESERVING_SUPPORT = "reserving_support"
    EXPLANATION = "explanation"
    UNKNOWN = "unknown"


def classify_intent(text: str) -> Intent:
    value = text.lower()
    if any(term in value for term in ("reserve", "ibnr", "development factor")):
        return Intent.RESERVING_SUPPORT
    if any(term in value for term in ("premium", "loss ratio", "frequency", "severity")):
        return Intent.ACTUARIAL_CALCULATION
    if any(term in value for term in ("covered", "coverage", "exclusion", "policy")):
        return Intent.POLICY_QUESTION
    if any(term in value for term in ("claim", "loss report", "adjuster")):
        return Intent.CLAIM_SUMMARY
    return Intent.UNKNOWN
