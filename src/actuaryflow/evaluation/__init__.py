"""Offline evaluation utilities for retrieval, agent, and governance research."""

from .metrics import accuracy, citation_precision, review_metrics
from .scenario import Scenario, ScenarioResult

__all__ = ["Scenario", "ScenarioResult", "accuracy", "citation_precision", "review_metrics"]
