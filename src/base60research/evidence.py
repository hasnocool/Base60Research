# src/base60research/evidence.py
"""Typed, AI-independent evidence records used by deterministic adjudication."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import StrEnum
from hashlib import sha256
import json
from typing import Any, Mapping

class CheckStatus(StrEnum):
    PASS = "pass"
    FAIL = "fail"
    INCONCLUSIVE = "inconclusive"
    NOT_RUN = "not_run"
    NOT_APPLICABLE = "not_applicable"

@dataclass(frozen=True, slots=True)
class CheckResult:
    status: CheckStatus
    reason: str
    justification: str | None = None

    def __post_init__(self) -> None:
        if not self.reason.strip():
            raise ValueError("check reason must not be empty")
        if self.status is CheckStatus.NOT_APPLICABLE and not (self.justification and self.justification.strip()):
            raise ValueError("not_applicable checks require a justification")

@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    """Structured evidence. AI verdicts are not accepted as adjudication inputs."""
    hypothesis_id: str
    preregistration_digest: str
    evidence_digest: str
    checks: Mapping[str, CheckResult]
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name in ("hypothesis_id", "preregistration_digest", "evidence_digest"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        if not isinstance(self.checks, Mapping):
            raise TypeError("checks must be a mapping")
        for name, result in self.checks.items():
            if not isinstance(name, str) or not name.strip():
                raise ValueError("check names must be non-empty strings")
            if not isinstance(result, CheckResult):
                raise TypeError(f"check {name!r} must be a CheckResult")

@dataclass(frozen=True, slots=True)
class GateTrace:
    gate: str
    status: CheckStatus
    passed: bool
    reason: str

@dataclass(frozen=True, slots=True)
class AdjudicationDecision:
    hypothesis_id: str
    classification: str
    policy_version: str
    evidence_digest: str
    reasons: tuple[str, ...]
    trace: tuple[GateTrace, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "hypothesis_id": self.hypothesis_id,
            "classification": self.classification,
            "policy_version": self.policy_version,
            "evidence_digest": self.evidence_digest,
            "reasons": list(self.reasons),
            "trace": [{"gate": x.gate, "status": x.status.value, "passed": x.passed, "reason": x.reason} for x in self.trace],
        }

def canonical_digest(payload: Mapping[str, Any]) -> str:
    """SHA-256 digest of canonical JSON-compatible data."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return sha256(encoded).hexdigest()
