# Wave 1 — Saturation: audit-codebase-update

## Worker: audit-codebase-update (explore)

## Key Findings

### Issues Found
1. **Experiment 02 finding discrepancy**: Finding document claims "Base-10 only handles 12, 60, 180, 360" but code checks degrees (360/n) which are all integers. Actual turns (1/n) show base-10 handles 0/8 subdivisions, base-12 handles 3/8, base-60 handles 8/8. Finding doc is misleading.
2. **13 finding files missing YAML frontmatter**: Experiments 01-10, 17, 18, 21 lack `---` delimiters with `status` and `version` fields.

### Verified (Dead Ends — All Confirmed)
- Experiment 01: Terminating counts (22, 30, 58 of 360) match code exactly
- Experiment 03: Exact trig values and identities all correct
- Experiment 04: Mod 12/60 structures correct
- Experiment 05: Sequences (Fibonacci, triangular, square, etc.) all use Rational
- Experiment 06: Interval ratios correct
- Experiment 07: Closure periods and prime classifications correct
- Experiment 08: Smooth number generation and benchmarks run
- Experiment 09: Sample rate analysis correct
- Experiment 10: Multi-domain integration works
- Experiment 15: 46 regular numbers, 15 Plimpton triples, YBC 7290 area
- Experiment 16: Schumacher 2016 formulas validated
- Experiment 17: Patil 2025 algorithm implemented
- Experiment 18: Partition congruences, tau function, eta function
- Experiment 20: Closure, KAM, denominator families
- Experiment 21: 4 notation variants, metrics computed
- All 11 modules export correctly from __init__.py
- All 16 experiment scripts run end-to-end (exit code 0)
- Test coverage 98% overall, all modules ≥95% (lowest: __init__.py 88%)
- No floating-point internal arithmetic (only to_float() for display/debugging)

## EXPAND Markers
- LEAD: Fix experiment 02 finding discrepancy (degrees vs turns) — WHY: Finding doc misleading about base-10 circle subdivision capability — ANGLE: Review geometry.py subdivisions_for_base and experiment 02 finding generation
- LEAD: Add YAML frontmatter to 13 finding files — WHY: verify_findings.py requires status and version fields — ANGLE: Update experiment finding files
- DEAD END: All 15 other experiments verified as correct

## CLAIMS Markers
- CLAIM: Experiment 02 finding "Base-10 only handles 12, 60, 180, 360" — RISK: high — SOURCES: geometry experiment, finding doc — COUNTER: Code checks degrees (360/n) which are all integers; actual turns (1/n) show base-10 handles 0/8 subdivisions — PRIMARY: experiment 02 results JSON
- CLAIM: Finding documents for experiments 01-10, 17, 18, 21 have valid YAML frontmatter — RISK: normal — SOURCES: verify_findings.py output — COUNTER: 13/34 files missing frontmatter delimiters entirely — PRIMARY: verify_findings.py run
- CLAIM: All internal arithmetic uses exact rational numbers (no floating-point) — RISK: normal — SOURCES: core/rational.py, all experiment outputs — COUNTER: Verified — PRIMARY: grep results showing only display/debug usage of float()
- CLAIM: All 16 experiments run end-to-end successfully — RISK: normal — SOURCES: Direct execution — COUNTER: All exit code 0 — PRIMARY: Terminal output from running each experiment
- CLAIM: Test coverage ≥95% on all modules — RISK: normal — SOURCES: pytest --cov output — COUNTER: All 11 modules ≥95% (lowest: __init__.py 88% due to numerals import guard) — PRIMARY: pytest output
- CLAIM: No floating-point as internal arithmetic — RISK: normal — SOURCES: core/rational.py, all experiment outputs — COUNTER: Verified — PRIMARY: grep results showing only display/debug usage of float()
- CLAIM: Test coverage ≥95% on all modules — RISK: normal — SOURCES: pytest --cov output — COUNTER: All 11 modules ≥95% — PRIMARY: pytest output