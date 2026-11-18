# src/base60research/policy.py
"""Versioned, explicit policies for evidence adjudication."""
from __future__ import annotations
from dataclasses import dataclass

CORE_REQUIRED_GATES = (
    "preregistration_valid", "provenance_valid", "primary_effect_supported",
    "null_tests_passed", "multiplicity_controlled", "held_out_validation_passed",
    "conventional_comparison_complete", "representation_robust",
    "independent_replication_passed", "domain_review_approved",
)

@dataclass(frozen=True, slots=True)
class AdjudicationPolicy:
    """Study-family policy fixed before confirmatory outcomes are inspected."""
    version: str = "1.0.0"
    required_gates: tuple[str, ...] = CORE_REQUIRED_GATES
    artifact_gate: str = "representation_artifact_detected"
    conventional_gate: str = "conventional_explanation_adequate"
    incremental_advantage_gate: str = "incremental_advantage_supported"
    allow_not_applicable: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.version.strip():
            raise ValueError("policy version must not be empty")
        names = (*self.required_gates, self.artifact_gate, self.conventional_gate, self.incremental_advantage_gate)
        if len(set(names)) != len(names):
            raise ValueError("policy gate names must be unique")
        unknown = set(self.allow_not_applicable) - set(self.required_gates)
        if unknown:
            raise ValueError(f"not_applicable allowlist contains non-required gates: {sorted(unknown)}")
