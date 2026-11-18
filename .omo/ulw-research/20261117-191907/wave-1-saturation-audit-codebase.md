# Wave 1 — Saturation: audit-codebase

## Worker: audit-codebase (explore)

## Key Findings

1. **No floating-point internal arithmetic** confirmed — to_float() calls in lissajous.py:170-172, signal_processing.py:62-86, trigonometry.py:91,525-527, fft_benchmarks.py:211 are documented as display/debug only or for NumPy/SciPy interfacing
2. **__init__.py export bug**: `metrics` listed in `__all__` but not imported (line 47); `numerals` has try/except fallback — 10 of 11 modules import correctly; metrics accessible via direct import but not as `base60lab.metrics`
3. **Test coverage**: All 11 specified modules ≥95% (95-100%); overall 98%. Main `__init__.py` shows 88% (2 missed lines: numerals import fallback)
4. **All 10 experiments run end-to-end**, produce JSON/CSV/visualization outputs, generate findings markdown
5. **All exact rational values verified**: Terminating fractions (22/30/58 of 360 for bases 10/12/60), overall scores (0.442/0.513/0.434), mod 12/60 units and zero divisors, trig values, Lissajous prime factor classes

## Sources
- src/base60lab/__init__.py
- src/base60lab/core/rational.py
- src/base60lab/engines/base10_engine.py, base12_engine.py, base60_engine.py
- src/base60lab/domains/fractions.py
- experiments/01-10_*.py
- docs/findings/*.md

## EXPAND Markers
- DEAD END: None — all claims verified, no unresolved leads from audit

## CLAIMS Markers
- CLAIM: No floating-point internal arithmetic — RISK: normal — SOURCES: 13 finding files — COUNTER: to_float() calls exist but documented as display-only — PRIMARY: source code
- CLAIM: 11 modules exist and export correctly — RISK: normal — SOURCES: __init__.py — COUNTER: metrics not imported — PRIMARY: __init__.py line 47
- CLAIM: Test coverage ≥95% on all modules — RISK: normal — SOURCES: pytest --cov output — COUNTER: __init__.py 88% — PRIMARY: pytest output
- CLAIM: All 10 experiments run end-to-end — RISK: normal — SOURCES: experiments/01-10 — COUNTER: None — PRIMARY: experiment execution
- CLAIM: Terminating fractions 22/30/58 of 360 — RISK: normal — SOURCES: experiment-01-fraction-analysis.md:9-11 — COUNTER: None — PRIMARY: direct computation
- CLAIM: Overall scores 0.442/0.513/0.434 — RISK: normal — SOURCES: findings docs — COUNTER: Rounding differences (exact values slightly different) — PRIMARY: compare_bases() output
- CLAIM: Mod 12 units={1,5,7,11}, zero_divisors={0,2,3,4,6,8,9,10} — RISK: normal — SOURCES: experiment-04-modular-patterns.md — COUNTER: None — PRIMARY: modular.units()/zero_divisors()
- CLAIM: Exact trig values sin(30°)=1/2, sin(45°)=√2/2, sin(60°)=√3/2 — RISK: normal — SOURCES: experiment-03-trigonometry-analysis.md — COUNTER: None — PRIMARY: trigonometry.sin_degrees()
- CLAIM: Frequency intervals 8/11/8/11 terminate in base-10/base-12/base-60 — RISK: normal — SOURCES: experiment-06-harmonic-analysis.md — COUNTER: None — PRIMARY: FrequencyRatio.value.is_terminating_in_base()
- CLAIM: Lissajous classes 252/70/780 — RISK: normal — SOURCES: experiment-07-lissajous-analysis.md — COUNTER: None — PRIMARY: analyze_prime_factor_effects(60)
- CLAIM: Combined experiments rank Base-12 > Base-10 > Base-60 — RISK: normal — SOURCES: experiment-10-combined-experiments.md — COUNTER: None — PRIMARY: compare_bases(10,12,60)
