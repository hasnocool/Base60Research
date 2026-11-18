# src/base60research/adjudication.py
"""Deterministic scientific evidence classification; no AI integration or inference."""
from __future__ import annotations
from .evidence import AdjudicationDecision, CheckStatus, EvidenceRecord, GateTrace
from .policy import AdjudicationPolicy

def adjudicate(evidence: EvidenceRecord, policy: AdjudicationPolicy | None = None) -> AdjudicationDecision:
    """Apply a fixed policy. Missing, inconclusive and unrun checks fail closed."""
    policy = policy or AdjudicationPolicy()
    trace: list[GateTrace] = []
    reasons: list[str] = []

    def record(gate: str, required: bool = False) -> CheckStatus:
        result = evidence.checks.get(gate)
        status = result.status if result else CheckStatus.NOT_RUN
        reason = result.reason if result else "Required evidence check is missing."
        passed = status is CheckStatus.PASS or (
            status is CheckStatus.NOT_APPLICABLE and gate in policy.allow_not_applicable
        )
        if status is CheckStatus.NOT_APPLICABLE and not passed:
            reason += " NOT_APPLICABLE is not authorized by this policy."
        trace.append(GateTrace(gate, status, passed, reason))
        if required and not passed:
            reasons.append(f"{gate}: {reason}")
        return status

    fatal_gates = (
        "preregistration_valid", "provenance_valid", "primary_effect_supported",
        "null_tests_passed", "multiplicity_controlled",
    )
    fatal_failure = False
    fatal_incomplete = False
    for gate in fatal_gates:
        status = record(gate, required=True)
        if status is CheckStatus.FAIL:
            fatal_failure = True
        elif status is not CheckStatus.PASS:
            fatal_incomplete = True

    artifact_status = record(policy.artifact_gate)
    conventional_status = record(policy.conventional_gate)
    incremental_status = record(policy.incremental_advantage_gate)
    remaining = tuple(g for g in policy.required_gates if g not in fatal_gates)
    for gate in remaining:
        record(gate, required=True)

    if fatal_failure:
        classification = "NOT_SUPPORTED"
        reasons.insert(0, "A preregistered validity or primary-evidence gate failed.")
    elif fatal_incomplete:
        classification = "UNRESOLVED_CANDIDATE"
        reasons.insert(0, "A foundational validity or primary-evidence check is missing or inconclusive.")
    elif artifact_status is CheckStatus.PASS:
        classification = "REPRESENTATION_ARTIFACT"
        reasons.insert(0, "A preregistered diagnostic confirmed representation-induced distortion.")
    elif conventional_status is CheckStatus.PASS and incremental_status is CheckStatus.FAIL:
        classification = "ESTABLISHED_EXPLANATION"
        reasons.insert(0, "A conventional explanation is adequate and incremental advantage failed.")
    else:
        required_trace = [item for item in trace if item.gate in policy.required_gates]
        if required_trace and all(item.passed for item in required_trace):
            classification = "ROBUST_CROSS_DOMAIN_CANDIDATE"
            reasons.insert(0, "Every required policy gate passed; this remains a candidate, not a new law.")
        else:
            classification = "UNRESOLVED_CANDIDATE"
            reasons.insert(0, "Required evidence is missing, inconclusive, or not authorized as inapplicable.")

    return AdjudicationDecision(evidence.hypothesis_id, classification, policy.version,
                                evidence.evidence_digest, tuple(reasons), tuple(trace))
