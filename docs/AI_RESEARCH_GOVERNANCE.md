# AI Research Governance and Evidence Adjudication

## Non-negotiable rule

AI systems may propose hypotheses, identify potentially relevant datasets, suggest analyses, generate code for review, and explain results. **AI systems do not decide whether a scientific discovery has occurred and cannot assign, upgrade, or override a finding's evidence classification.**

Classification is produced by a deterministic, inspectable Evidence Adjudication Engine from structured evidence and versioned rules. The engine does not use an LLM confidence score, natural-language judgement, embedding similarity, or an agent's self-assessment as evidence.

This is an architectural boundary, not a prompt instruction.

## Responsibilities

### AI research assistant — advisory only

Allowed: suggest falsifiable hypotheses; identify candidate public datasets; recommend baselines and null models for review; draft analysis code; explain statistical outputs and limitations.

Not allowed: declare discoveries; change preregistered criteria after seeing confirmatory outcomes; suppress failed tests or replications; turn missing evidence into a pass; alter evidence records or classification rules; use its own explanation as independent validation.

### Deterministic analysis pipeline

Executes versioned plans; calculates metrics, uncertainty, null distributions and corrections; checks provenance and split integrity; evaluates baselines; records failed, skipped and unavailable checks explicitly.

### Evidence Adjudication Engine

Validates structured evidence; applies a versioned policy; produces machine-readable reasons; refuses promotion when required evidence is missing or invalid; records policy version, evidence digest and decision trace.

### Human scientific review

Humans judge domain assumptions, measurement quality and interpretation. Human overrides are separate, attributed, timestamped review events with rationale. They never silently rewrite statistical evidence; automated and human decisions remain visible separately.

## Classification contract

Thresholds are configured per registered study before confirmatory analysis. There is no universal p-value that makes every scientific claim true.

- **NOT_SUPPORTED**: the preregistered primary criterion fails, the effect is not distinguishable from the declared null, or a required validity check fails.
- **REPRESENTATION_ARTIFACT**: encoding, quantization, bin selection, precision, unit conversion or post-hoc representation choice introduces or materially amplifies the pattern, which does not survive appropriate continuous/native and alternative-representation controls.
- **ESTABLISHED_EXPLANATION**: the effect is supported, but a registered conventional model or known mechanism explains it adequately; no preregistered incremental advantage is demonstrated.
- **UNRESOLVED_CANDIDATE**: evidence is incomplete, ambiguous, underpowered, sensitive to reasonable analysis choices, or awaiting independent replication. This is the safe default whenever required evidence is unavailable.
- **ROBUST_CROSS_DOMAIN_CANDIDATE**: all confirmatory gates pass, including preregistration integrity, data quality, appropriate null tests, multiplicity control, held-out performance, conventional-model comparison, representation robustness, independent replication and human domain review. This means a robust candidate for further investigation, not a proven new law.

An inapplicable test must be marked NOT_APPLICABLE with a justification approved during preregistration; it must never be silently treated as passed.

## Required evidence record

Every adjudication consumes a versioned record containing:

- hypothesis ID, version, preregistration timestamp and immutable plan digest;
- dataset IDs, source/provenance, license, checksums, units, sampling and quality flags;
- transformation pipeline and software/environment versions;
- discovery/validation/test split definitions and leakage checks;
- primary and secondary metrics, direction and minimum meaningful effect;
- conventional baseline and candidate-model results;
- null-model definitions, simulation/permutation counts and random seeds;
- effect sizes, uncertainty intervals, p-values where applicable, correction family and adjusted results;
- representation tournament results, precision/binning sensitivity and native/continuous control;
- independent replication evidence;
- missing, failed, skipped and not-applicable checks;
- domain-review status and reviewer rationale.

The record distinguishes false, not_run, failed, inconclusive and not_applicable. Missing evidence is never equivalent to a passing test.

## Decision algorithm

1. Validate schema, immutable preregistration digest, provenance and analysis version.
2. If evidence is malformed, missing or contradictory, return UNRESOLVED_CANDIDATE (or NOT_SUPPORTED for a preregistered validity failure) with explicit reasons.
3. Check representation sensitivity and encoding-artifact diagnostics.
4. Check registered conventional models and explanations.
5. Evaluate the preregistered primary metric, meaningful-effect threshold, uncertainty and null tests.
6. Verify multiplicity policy covers the complete search, not just the reported winner.
7. Verify held-out validation and independent replication.
8. Verify domain-review requirements.
9. Return the highest classification whose complete gate set is satisfied. Never infer a higher classification from partial evidence.
10. Emit a decision trace listing every gate, input, rule version and reason.

## Security and integrity boundaries

- The AI assistant receives read-only access to adjudicated results by default.
- Changes after preregistration create a new version and are exploratory unless independently confirmed.
- The adjudication package must not import or call an LLM client.
- Classification code must be deterministic for identical evidence and policy versions.
- Persist evidence and decision records append-only; corrections create superseding records.
- Keep human overrides separate from automated decisions.
- Test adversarial fixtures: cherry-picked ratios, post-hoc bin counts, leaked test data, missing replication, invalid provenance, failed baselines and p-hacking simulations.

## Implementation layout

Add ai_advisor.py for optional advisory interfaces only; evidence.py for typed evidence and gate schemas; adjudication.py for deterministic classification with no AI dependency; policy.py for versioned domain-specific gates; and audit.py for immutable decision traces and evidence digests.

Keep the adjudicator as a pure, testable component wherever possible: structured evidence plus explicit policy produces a structured decision. The AI layer may read and explain the decision, but cannot write it.

## Required acceptance tests

1. Same evidence and policy produce identical normalized decisions.
2. No LLM/client dependency is imported by the adjudication module.
3. Missing replication cannot produce ROBUST_CROSS_DOMAIN_CANDIDATE.
4. Missing provenance, uncorrected multiple testing or failed validity cannot be interpreted as success.
5. An AI-supplied label or confidence field is ignored or rejected.
6. Post-hoc base/bin selection is detected or leaves the finding unresolved.
7. Conventional-model equivalence prevents a claimed incremental Base-60 advantage.
8. Human override is stored separately with reviewer, timestamp and rationale; original automated decision remains intact.
9. Every decision includes a machine-readable gate-by-gate trace.