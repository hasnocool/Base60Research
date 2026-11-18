# Wave 1 — Saturation: verify-claims

## Worker: verify-claims (deep QA)

## Key Findings

1. **761 tests pass**, 97.92% coverage — confirmed
2. **Composite scores are exact rationals**: Rational(935509/2118200) for base-10, Rational(32806417941851/64001624820000) for base-12, Rational(217/500) for base-60 — manual recomputation matches exactly
3. **Terminating fraction ratios match**: numerals.py terminating_denominators() and metrics.py _terminating_fraction_ratio() both give 15/100, 20/100, 34/100 for bases 10, 12, 60 at max_denominator=100
4. **Circle subdivision angles exact**: All 8 standard subdivisions (12,24,30,36,60,120,180,360) yield exact Rational angles
5. **No float internal arithmetic** confirmed — to_float() calls documented as display/debug only
6. **All 10 experiments run successfully** producing JSON/CSV/PNG outputs
7. **Finding file compliance issues**: 10 experiment finding files lack YAML frontmatter; numerals-base-conversion.md has invalid status "implemented" and missing version

## Sources
- pytest output
- metrics.py compare_bases()
- numerals.py terminating_denominators()
- geometry.py subdivision_angle()
- verify_findings.py output
- All experiment finding files

## EXPAND Markers
- LEAD: Experiment finding files lack YAML frontmatter with required status/version fields — WHY: verify_findings.py expects all finding files to have proper frontmatter, but 10 generated experiment findings don't include it — ANGLE: Add frontmatter generation to experiment scripts or update verify_findings.py
- LEAD: numerals-base-conversion.md has invalid status "implemented" and missing version — WHY: Doesn't conform to verification schema — ANGLE: Update file to use valid status "proven" and add version field
- DEAD END: Float usage in Rational.to_float() and TrigValue.to_float() — documented as display/debug only, not internal arithmetic; no-float guarantee holds

## CLAIMS Markers
- CLAIM: All tests pass with >95% coverage — RISK: normal — SOURCES: test execution — COUNTER: none — PRIMARY: pytest output (761 passed, 97.92%)
- CLAIM: Composite scores are exact rationals — RISK: normal — SOURCES: metrics.py compare_bases() — COUNTER: none — PRIMARY: Manual recomputation matches exactly
- CLAIM: Terminating fraction ratios match between modules — RISK: normal — SOURCES: numerals.py + metrics.py — COUNTER: none — PRIMARY: Both give 15/100, 20/100, 34/100
- CLAIM: Circle subdivision angles exact rational — RISK: normal — SOURCES: geometry.py — COUNTER: none — PRIMARY: All 8 standard subdivisions exact
- CLAIM: No floating-point internal arithmetic — RISK: normal — SOURCES: AST scan — COUNTER: to_float() exists but documented as display-only — PRIMARY: Core arithmetic modules
- CLAIM: All 10 experiments run successfully — RISK: normal — SOURCES: Experiment execution — COUNTER: none — PRIMARY: All 10 experiments completed
- CLAIM: Findings documentation partially conforms to schema — RISK: normal — SOURCES: verify_findings.py — COUNTER: none — PRIMARY: 17/28 files pass; 10 experiment files lack frontmatter
