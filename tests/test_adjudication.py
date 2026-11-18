# tests/test_adjudication.py
"""Adversarial tests for the deterministic, AI-independent adjudication boundary."""
from dataclasses import replace
import inspect
import pytest
from base60research.adjudication import adjudicate
from base60research.evidence import CheckResult, CheckStatus, EvidenceRecord
from base60research.policy import AdjudicationPolicy, CORE_REQUIRED_GATES

def check(status=CheckStatus.PASS, reason=None):
    rationale = "approved preregistration rationale" if status is CheckStatus.NOT_APPLICABLE else None
    return CheckResult(status, reason or f"fixture: {status.value}", rationale)

def robust_checks():
    checks = {name: check() for name in CORE_REQUIRED_GATES}
    checks.update({
        "representation_artifact_detected": check(CheckStatus.FAIL, "No artifact detected."),
        "conventional_explanation_adequate": check(CheckStatus.FAIL, "No adequate conventional explanation."),
        "incremental_advantage_supported": check(CheckStatus.PASS, "Incremental advantage met threshold."),
    })
    return checks

def evidence(checks=None, metadata=None):
    return EvidenceRecord("HYP-001", "a" * 64, "b" * 64,
                          robust_checks() if checks is None else checks,
                          {} if metadata is None else metadata)

def test_complete_evidence_produces_robust_candidate():
    result = adjudicate(evidence())
    assert result.classification == "ROBUST_CROSS_DOMAIN_CANDIDATE"
    assert all(x.passed for x in result.trace if x.gate in CORE_REQUIRED_GATES)

def test_identical_inputs_produce_identical_decisions():
    item = evidence()
    assert adjudicate(item).to_dict() == adjudicate(item).to_dict()

def test_missing_replication_cannot_be_robust():
    checks = robust_checks()
    del checks["independent_replication_passed"]
    assert adjudicate(evidence(checks)).classification == "UNRESOLVED_CANDIDATE"

@pytest.mark.parametrize("gate", ["provenance_valid", "preregistration_valid", "null_tests_passed",
                                  "primary_effect_supported", "multiplicity_controlled"])
def test_failed_validity_or_primary_gate_is_not_supported(gate):
    checks = robust_checks()
    checks[gate] = check(CheckStatus.FAIL, "Adversarial failed gate.")
    assert adjudicate(evidence(checks)).classification == "NOT_SUPPORTED"

def test_ai_supplied_classification_and_confidence_cannot_promote():
    item = evidence(metadata={"ai_classification": "ROBUST_CROSS_DOMAIN_CANDIDATE",
                              "ai_confidence": 1.0, "assistant_verdict": "discovery"})
    checks = robust_checks()
    checks["independent_replication_passed"] = check(CheckStatus.NOT_RUN)
    assert adjudicate(replace(item, checks=checks)).classification == "UNRESOLVED_CANDIDATE"

def test_representation_artifact_takes_precedence_over_candidate():
    checks = robust_checks()
    checks["representation_artifact_detected"] = check(CheckStatus.PASS, "Post-hoc bins created effect.")
    assert adjudicate(evidence(checks)).classification == "REPRESENTATION_ARTIFACT"

def test_conventional_explanation_without_incremental_gain_is_established():
    checks = robust_checks()
    checks["conventional_explanation_adequate"] = check(CheckStatus.PASS, "Known model explains effect.")
    checks["incremental_advantage_supported"] = check(CheckStatus.FAIL, "No incremental gain.")
    assert adjudicate(evidence(checks)).classification == "ESTABLISHED_EXPLANATION"

@pytest.mark.parametrize("status", [CheckStatus.NOT_RUN, CheckStatus.INCONCLUSIVE])
def test_missing_or_inconclusive_gate_fails_closed(status):
    checks = robust_checks()
    checks["held_out_validation_passed"] = check(status)
    assert adjudicate(evidence(checks)).classification == "UNRESOLVED_CANDIDATE"

def test_not_applicable_requires_policy_allowlist():
    checks = robust_checks()
    checks["domain_review_approved"] = check(CheckStatus.NOT_APPLICABLE)
    assert adjudicate(evidence(checks)).classification == "UNRESOLVED_CANDIDATE"
    policy = AdjudicationPolicy(allow_not_applicable=("domain_review_approved",))
    assert adjudicate(evidence(checks), policy).classification == "ROBUST_CROSS_DOMAIN_CANDIDATE"

def test_every_required_gate_appears_in_trace_even_when_missing():
    result = adjudicate(evidence({}))
    assert set(CORE_REQUIRED_GATES).issubset({x.gate for x in result.trace})
    assert result.classification == "UNRESOLVED_CANDIDATE"

def test_adjudicator_has_no_llm_dependency():
    import base60research.adjudication as module
    source = inspect.getsource(module).lower()
    assert "openai" not in source and "llm" not in source and "langchain" not in source

def test_invalid_not_applicable_check_requires_justification():
    with pytest.raises(ValueError, match="justification"):
        CheckResult(CheckStatus.NOT_APPLICABLE, "Not relevant.")
