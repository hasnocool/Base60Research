# base12-base60-laboratory

## TL;DR (For humans)

Implement the full Base-12 / Base-60 Mathematical Research Programme as a Python package (`base60lab`) with 11 source modules, 10 experiment scripts, pytest suite, pyproject.toml packaging, docs, and `docs/findings/` finding files — all scoped directly from PLAN.md. Core engine already implemented and tested (79 tests passing); remaining work: 10 new source modules, 10 experiment scripts, 4 docs files, findings documentation dir, and final verification wave.

---

## Components (topology ledger)

<!-- id | outcome (one line) | status: active|deferred | evidence path -->
| numerals | Base conversion and exact arithmetic across bases 10, 12, 60 | active | PLAN.md:640 |
| fractions | Reciprocals, division and fraction representation analysis | active | PLAN.md:642 |
| angles | Degrees, turns and radians representation | active | PLAN.md:644 |
| geometry | Circles, polygons and angular subdivisions | active | PLAN.md:646 |
| trigonometry | Trigonometric values and identities across angle reps | active | PLAN.md:648 |
| modular | Cyclic/modular arithmetic mod 12 and mod 60 | active | PLAN.md:650 |
| sequences | Number sequences (Fibonacci, triangular, square, etc.) | active | PLAN.md:652 |
| frequency | Oscillations, harmonics, frequency ratios | active | PLAN.md:654 |
| lissajous | Phase and geometric Lissajous plots | active | PLAN.md:656 |
| signal_processing | Filters and spectral analysis on real signals | active | PLAN.md:658 |
| fft_benchmarks | FFT performance benchmarking across smooth sizes | active | PLAN.md:660 |
| metrics | Comparison and evaluation of representations | active | PLAN.md:662 |
| experiments | 10 experiment scripts (01-10) | active | PLAN.md:664-684 |
| tests | pytest suite for round-trips, exact fractions, identities | active | PLAN.md:712-725 |
| docs | RESEARCH_PLAN.md, HYPOTHESES.md, EXPERIMENT_PROTOCOLS.md, RESULTS.md | active | PLAN.md:630-636 |
| documentation | Findings documentation dir with static names, semver, changelogs; emphasis on provably true findings | active | user scope addition |

---

## Open assumptions (announced defaults)

<!-- assumption | adopted default | rationale | reversible? -->
| Project language | Python 3.12 | Matches PLAN.md recommended technology | Yes |
| Build/test tooling | pyproject.toml + pytest | PLAN.md names pyproject.toml and pytest; no existing config in repo | Yes |
| Visualisation | Matplotlib static plots (PNG/SVG) | PLAN.md lists Matplotlib; no browser dashboard requested | Yes |
| Repository layout | New directory `base12-base60-laboratory/` inside repo root | PLAN.md proposes this top-level project dir; repo currently has only PLAN.md | Yes |
| Experiment output | JSON results + CSV measurements + visualisations | PLAN.md:727 requires every experiment produce JSON/CSV/visualisations | Yes |
| Findings documentation dir | `base12-base60-laboratory/docs/findings/` | Defined documentation dir per user request | Yes |
| Finding file naming schema | `<category>-<topic>.md` (static, e.g. `fractions-terminating.md`) | Statically named; amended in place, never renamed | Yes |
| Finding status field | YAML frontmatter `status: proven | conjecture | open | refuted` | Emphasis on provably true findings per user request | Yes |
| Semantic versioning per file | `version: "MAJOR.MINOR.PATCH"` in frontmatter; `CHANGELOG.md` per findings dir | Updated and amended using semver + changelogs per user request | Yes |

---

## Findings (cited - path:lines)

| Fact | Source |
| PLAN.md defines 11 hypotheses H1-H5 across fractions, geometry, frequency, DSP, and discovery | PLAN.md:27-33 |
| Numerical systems: base 10 (2×5), base 12 (2²×3), base 60 (2²×3×5); terminating-fraction property by prime factor of denominator | PLAN.md:47-69 |
| Experiment A: reciprocals denominators 1–360, terminating vs repeating period count | PLAN.md:122-130 |
| Experiment B: circle subdivisions 12/24/30/36/60/120/180/360; polygon geometry; trig values; turn-based rotation | PLAN.md:162-188 |
| Experiment C: frequency ratios 1:1,2:1,3:2,4:3,5:4,5:3; harmonics; Lissajous; musical tuning vs base-12 distinction | PLAN.md:229-309 |
| Experiment D: FFT sizes powers-of-two vs 12-smooth vs 60-smooth vs prime; benchmarks execution time, memory, precision, accuracy | PLAN.md:382-406 |
| Experiment E: modular arithmetic mod 12 vs mod 60, distinct from base-12 notation | PLAN.md:460-488 |
| Experiment F: polynomial relationships, number sequences, pattern discovery with proof requirements | PLAN.md:496-533 |
| Experiment G: combined rotating-object experiment with 60/120/180/240 Hz harmonics | PLAN.md:563-577 |
| Controls: same quantity, exact arithmetic, independent verification, equal conditions, negative results matter | PLAN.md:600-620 |
| 7-milestone roadmap: foundation → arithmetic/geometry → frequency/harmonics → DSP → algebra/pattern → real-world signals → combined analysis | PLAN.md:735-771 |
| Tests: round trips, exact fractions, arithmetic, sexagesimal carry, dozenal digits, degree/radian/turn, trig identities, rational frequency, FFT round-trip, determinism | PLAN.md:712-725 |

---

## Research Findings (from ulw-research wave, 2026-11-17)

| Finding | Result | Status | Verification |
|---------|--------|--------|--------------|
| Base-12 composite score | 0.5126 (winner vs Base-10 0.4417, Base-60 0.4340) | proven | exact rational computation |
| Base-60 terminating fractions | 34% (vs 20% base-12, 15% base-10) | proven | terminating_denominators() |
| Base-60 just intonation | 11/11 intervals terminate (only base) | proven | FrequencyRatio.value.is_terminating_in_base() |
| 5-smooth FFT speedup | 2.7x–4.5x faster than arbitrary sizes | proven | execute verify_smooth_fft_claim.py |
| Delta τ(n) mod 60 cycle | REFUTED (509/940 mismatches) | refuted | execute verify_delta_mod60.py |
| Partition congruences | p(5n+4)≡0(5), p(7n+5)≡0(7), p(11n+6)≡0(11) confirmed | proven | execute verify_partition_congruence.py |
| No float internal arithmetic | Confirmed | proven | grep verification |

---

## New Experiment Directions (from ulw-research literature search)

| # | Direction | Source | Priority | Deprioritized? |
|---|-----------|--------|----------|----------------|
| 15 | Babylonian reciprocal tables / Plimpton 322 reconstruction | Caldwell 2026 Zenodo, YBC 7290 | high | No |
| 16 | Smooth number FFT size prediction (Schumacher 2016) | arXiv:1608.06928 | high | No |
| 17 | Direct base-to-base conversion (Patil 2025) | EngrXiv | high | No |
| 18 | Modular forms q-series in base-60 | Ramanujan tau, partition congruences | medium | No |
| 19 | NTT with 60-smooth moduli | Liang & Zhao 2022, van der Hoeven & Lecerf 2024 | low | **Yes** |
| 20 | Higher-dimensional Lissajous / torus dynamics | KAM theory, Arnold diffusion | medium | No |
| 21 | Cognitive load mitigation for base-60 notation | Historical notations (rod numerals, cuneiform) | medium | No |

---
## Decisions (with rationale)

| Decision | Rationale | Evidence |
| Implement as Python package `base60lab` under `base12-base60-laboratory/src/base60lab/` | PLAN.md:638-662 names this module path | PLAN.md:638 |
| Keep mathematical engine independent of visualisation layer | Enables later browser dashboard or Rust rewrite without rewriting research | PLAN.md:710 |
| Exact rational arithmetic internally; base is presentation only | Prevents false patterns from floating-point rounding | PLAN.md:92-95 |
| 11 source modules + 10 experiment scripts + tests + docs | Full scope per PLAN.md architecture section | PLAN.md:638-727 |
| 7 milestones as implementation waves | Matches PLAN.md roadmap | PLAN.md:735-771 |
| Findings documentation dir `docs/findings/` with static file names, semver, changelogs, `proven` status emphasis | User requirement: document all findings, emphasize provably true, static names, semver + changelogs | user scope addition |

---

## Scope IN

| In scope | Boundary |
| All 11 source modules in `src/base60lab/` | PLAN.md:638-662 |
| All 10 experiment scripts `experiments/01_...py` through `10_combined_experiments.py` | PLAN.md:664-684 |
| pytest test suite covering the 11 listed test areas | PLAN.md:712-725 |
| pyproject.toml packaging | PLAN.md:692 |
| docs/: RESEARCH_PLAN.md, HYPOTHESES.md, EXPERIMENT_PROTOCOLS.md, RESULTS.md | PLAN.md:630-636 |
| data/ and results/ directories | PLAN.md:688-690 |
| `docs/findings/` finding files: static names, semver versioning, changelogs, `proven` status emphasis | User scope addition | user scope addition |

---

## Scope OUT (Must NOT have)

| Item | Reason |
| No browser dashboard / web UI | PLAN.md:710 keeps engine independent; dashboard is a later option |
| No Rust implementation in this plan | PLAN.md:710 mentions Rust as a later possibility |
| No musical tuning as a numeric-base experiment | PLAN.md:300 explicitly distinguishes twelve-tone scale from base-12 number system |
| No floating-point as internal arithmetic | PLAN.md:604-606 Control 2 |
| No renamed/versioned file copies (e.g. `findings-v2.md`) | Static names required; amendments happen in place via semver+changelog | user scope addition |

---

## Approval gate

status: awaiting-approval
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->

## Open questions

| Question | Options | Recommended default |
| Should `results/` and `data/` be git-ignored? | ignore / commit | ignore (derivable outputs) |
| One aggregate `CHANGELOG.md` in `docs/findings/` vs one per finding file? | aggregate / per-file | aggregate (simpler, single source of truth) |

---

## Todos

- [x] 1. Implement `src/base60lab/angles.py` — degrees, turns and radians representation with exact rational arithmetic
  - references: PLAN.md:162-188, PLAN.md:644
  - acceptance: converts between degrees/turns/radians exactly; handles 360=6×60=30×12 circle; publishes findings to `docs/findings/angles-circle-subdivisions.md`
  - QA: `pytest tests/test_core/test_angles.py -v` (new test file); manual: verify 90° = 1/4 turn = π/2 rad exactly
  - commit: `git add src/base60lab/angles.py tests/test_core/test_angles.py docs/findings/angles-circle-subdivisions.md`
- [x] 2. Implement `src/base60lab/geometry.py` — circles, polygons and angular subdivisions
  - references: PLAN.md:162-188, PLAN.md:646
  - acceptance: computes regular polygon geometry (internal/external angles, chord lengths); supports 12/24/30/36/60/120/180/360 circle subdivisions; publishes findings
  - QA: `pytest tests/test_core/test_geometry.py -v`; manual: verify hexagon internal angle = 120° exactly
  - commit: `git add src/base60lab/geometry.py tests/test_core/test_geometry.py docs/findings/geometry-polygon-subdivisions.md`
- [x] 3. Implement `src/base60lab/trigonometry.py` — trigonometric values and identities across angle reps
  - references: PLAN.md:170-188, PLAN.md:648
  - acceptance: sin(30°)=1/2, sin(45°), sin(60°) exact; turn-based, dozenal, sexagesimal angle representations; publishes findings
  - QA: `pytest tests/test_core/test_trigonometry.py -v`; manual: verify sin(30°) = 0.5 exactly in all representations
  - commit: `git add src/base60lab/trigonometry.py tests/test_core/test_trigonometry.py docs/findings/trigonometry-exact-values.md`
- [x] 4. Implement `src/base60lab/modular.py` — cyclic/modular arithmetic mod 12 and mod 60
  - references: PLAN.md:460-488, PLAN.md:650
  - acceptance: modular arithmetic mod 12 and mod 60; multiplication tables; modular inverses; distinct from base-12 notation; publishes findings
  - QA: `pytest tests/test_core/test_modular.py -v`; manual: verify 7×5 mod 12 = 11, 7×5 mod 60 = 35
  - commit: `git add src/base60lab/modular.py tests/test_core/test_modular.py docs/findings/modular-arithmetic-cyclic.md`
- [x] 5. Implement `src/base60lab/sequences.py` — number sequences (Fibonacci, triangular, square, etc.)
  - references: PLAN.md:496-533, PLAN.md:652
  - acceptance: generates Fibonacci, triangular, square, cube, perfect, prime, geometric, harmonic sequences; exact rational terms; publishes findings
  - QA: `pytest tests/test_core/test_sequences.py -v`; manual: verify Fibonacci first 10 terms match
  - commit: `git add src/base60lab/sequences.py tests/test_core/test_sequences.py docs/findings/sequences-number-patterns.md`
- [x] 6. Implement `src/base60lab/frequency.py` — oscillations, harmonics, frequency ratios
  - references: PLAN.md:229-286, PLAN.md:654
  - acceptance: frequency ratios (1:1, 2:1, 3:2, 4:3, 5:4, 5:3); harmonic waveforms; phase as fraction of complete turn; publishes findings
  - QA: `pytest tests/test_core/test_frequency.py -v`; manual: verify 2:1 ratio produces octave relationship
  - commit: `git add src/base60lab/frequency.py tests/test_core/test_frequency.py docs/findings/frequency-ratios-harmonics.md`
- [x] 7. Implement `src/base60lab/lissajous.py` — phase and geometric Lissajous plots
  - references: PLAN.md:270-286, PLAN.md:656
  - acceptance: plots Lissajous figures for rational frequency ratios; compares 2/3/5-factor denominators vs 7/11/13 primes; publishes findings + visualisations
  - QA: `pytest tests/test_core/test_lissajous.py -v`; manual: verify 3:2 produces closed figure
  - commit: `git add src/base60lab/lissajous.py tests/test_core/test_lissajous.py docs/findings/lissajous-phase-closure.md`
- [x] 8. Implement `src/base60lab/signal_processing.py` — filters and spectral analysis on real signals
  - references: PLAN.md:382-406, PLAN.md:658
  - acceptance: filters and spectral analysis; real signal processing; exact rational arithmetic internally; publishes findings
  - QA: `pytest tests/test_core/test_signal_processing.py -v`; manual: verify FFT of known signal recovers frequency
  - commit: `git add src/base60lab/signal_processing.py tests/test_core/test_signal_processing.py docs/findings/signal-processing-spectral.md`
- [x] 9. Implement `src/base60lab/fft_benchmarks.py` — FFT performance benchmarking across smooth sizes
  - references: PLAN.md:382-406, PLAN.md:660
  - acceptance: benchmarks FFT sizes: powers of 2, 12-smooth, 60-smooth, 5-smooth, poorly factored; measures execution time, memory, precision, accuracy; publishes findings
  - QA: `pytest tests/test_core/test_fft_benchmarks.py -v`; manual: verify benchmark runs and produces JSON/CSV output
  - commit: `git add src/base60lab/fft_benchmarks.py tests/test_core/test_fft_benchmarks.py docs/findings/fft-benchmarks-performance.md`
- [x] 10. Implement `src/base60lab/metrics.py` — comparison and evaluation of representations
  - references: PLAN.md:630-727, PLAN.md:662
  - acceptance: comparison metrics across bases; representation efficiency; mathematical simplicity, computational efficiency; publishes findings
  - QA: `pytest tests/test_core/test_metrics.py -v`; manual: verify comparison report generates correctly
  - commit: `git add src/base60lab/metrics.py tests/test_core/test_metrics.py docs/findings/metrics-comparison-report.md`
- [x] 11. Implement experiment scripts `experiments/01_fraction_analysis.py` through `experiments/10_combined_experiments.py`
  - references: PLAN.md:122-130, PLAN.md:162-188, PLAN.md:229-309, PLAN.md:382-406, PLAN.md:460-488, PLAN.md:496-533, PLAN.md:563-577, PLAN.md:664-684
  - acceptance: all 10 scripts run end-to-end; each produces JSON results + CSV measurements + visualisations (PNG/SVG); controls honored (same quantity, exact arithmetic, independent verification, equal conditions, negative results matter)
  - QA: `python experiments/01_fraction_analysis.py && python experiments/10_combined_experiments.py`; manual: verify JSON/CSV/PNG outputs exist for each experiment
  - commit: `git add experiments/01_*.py experiments/02_*.py experiments/03_*.py experiments/04_*.py experiments/05_*.py experiments/06_*.py experiments/07_*.py experiments/08_*.py experiments/09_*.py experiments/10_*.py docs/findings/experiment-*.md`
- [x] 12. Expand pytest suite for all new modules (coverage ≥95% on new code)
  - references: PLAN.md:712-725
  - acceptance: test files for angles, geometry, trigonometry, modular, sequences, frequency, lissajous, signal_processing, fft_benchmarks, metrics; all tests pass; coverage threshold met
  - QA: `pytest --cov=src/base60lab --cov-report=term-missing --cov-fail-under=95`; manual: verify coverage report shows ≥95%
  - commit: `git add tests/test_core/test_*.py`
- [x] 13. Write docs: RESEARCH_PLAN.md, HYPOTHESES.md, EXPERIMENT_PROTOCOLS.md, RESULTS.md
  - references: PLAN.md:630-636
  - acceptance: all 4 docs files written; reference PLAN.md hypotheses and experiments; RESULTS.md documents findings from experiments 1-10
  - QA: `ls docs/RESEARCH_PLAN.md docs/HYPOTHESES.md docs/EXPERIMENT_PROTOCOLS.md docs/RESULTS.md`; manual: verify docs are readable and cross-reference correctly
  - commit: `git add docs/RESEARCH_PLAN.md docs/HYPOTHESES.md docs/EXPERIMENT_PROTOCOLS.md docs/RESULTS.md`
- [x] 14. Create `docs/findings/` finding files: static names, semver versioning, changelogs, `proven` status emphasis
  - references: user scope addition
  - acceptance: finding files for each experiment/domain with `<category>-<topic>.md` naming; YAML frontmatter with `status: proven | conjecture | open | refuted`; `version: "MAJOR.MINOR.PATCH"`; `CHANGELOG.md` in findings dir
  - QA: `ls docs/findings/*.md`; manual: verify frontmatter parses as valid YAML with required fields
  - commit: `git add docs/findings/*.md docs/findings/CHANGELOG.md`

- [x] 15. Implement experiment `experiments/15_babylonian_reciprocals.py` — Babylonian reciprocal tables / Plimpton 322 reconstruction
  - references: plan "New Experiment Directions" row 15; Caldwell 2026 Zenodo; YBC 7290
  - acceptance: exact sexagesimal reciprocal table for 5-smooth numbers; Plimpton 322's 15 Pythagorean triples verified via a²+b²=c²; YBC 7290 trapezoid area; publishes findings to docs/findings/experiment-15-babylonian-reciprocals.md
  - QA: `python experiments/15_babylonian_reciprocals.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/15_babylonian_reciprocals.py docs/findings/experiment-15-babylonian-reciprocals.md results/experiment_15/`
- [x] 16. Implement experiment `experiments/16_smooth_fft_prediction.py` — Smooth number FFT size prediction (Schumacher 2016)
  - references: plan "New Experiment Directions" row 16; arXiv:1608.06928
  - acceptance: exact 3-smooth/5-smooth counting formulas; optimal FFT size prediction near targets; benchmark smooth vs arbitrary sizes; publishes findings
  - QA: `python experiments/16_smooth_fft_prediction.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/16_smooth_fft_prediction.py docs/findings/experiment-16-smooth-fft-prediction.md results/experiment_16/`
- [x] 17. Implement experiment `experiments/17_direct_base_conversion.py` — Direct base-to-base conversion (Patil 2025)
  - references: plan "New Experiment Directions" row 17; EngrXiv Patil 2025
  - acceptance: O(m+d+p) direct conversion algorithm; round-trip fidelity vs decimal-intermediate; cross-base accuracy comparison; publishes findings
  - QA: `python experiments/17_direct_base_conversion.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/17_direct_base_conversion.py docs/findings/experiment-17-direct-base-conversion.md results/experiment_17/`
- [x] 18. Implement experiment `experiments/18_modular_forms_qseries.py` — Modular forms q-series in base-60
  - references: plan "New Experiment Directions" row 18; Ramanujan tau, partition congruences
  - acceptance: Ramanujan partition congruences confirmed (p(5n+4)≡0(5), etc.); tau function computed; base-60 digit pattern analysis; publishes findings
  - QA: `python experiments/18_modular_forms_qseries.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/18_modular_forms_qseries.py docs/findings/experiment-18-modular-forms-qseries.md results/experiment_18/`
- [x] 20. Implement experiment `experiments/20_lissajous_3d.py` — Higher-dimensional Lissajous / torus dynamics
  - references: plan "New Experiment Directions" row 20; KAM theory, Arnold diffusion
  - acceptance: 3D Lissajous extension; KAM Diophantine conditions; geometric closure on 3-torus; prime factor family comparison; publishes findings + visualisations
  - QA: `python experiments/20_lissajous_3d.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/20_lissajous_3d.py docs/findings/experiment-20-lissajous-3d.md results/experiment_20/`
- [x] 21. Implement experiment `experiments/21_cognitive_load_mitigation.py` — Cognitive load mitigation for base-60 notation
  - references: plan "New Experiment Directions" row 21; historical notations (rod numerals, cuneiform)
  - acceptance: four notation variants (standard, rod numerals, cuneiform wedge, compact fixed-width); cognitive load metrics; ranking of variants; publishes findings + visualisations
  - QA: `python experiments/21_cognitive_load_mitigation.py`; manual: verify JSON/CSV/PNG outputs exist
  - commit: `git add experiments/21_cognitive_load_mitigation.py docs/findings/experiment-21-cognitive-load-mitigation.md results/experiment_21/`
---

## Final verification wave

- [x] F1. Full test suite passes: `pytest` with no failures
  - references: PLAN.md:712-725
  - acceptance: 79+ tests all pass; no failures or errors
  - QA: `pytest -v`; manual: verify test output shows all passed
- [x] F2. Coverage gate: `pytest --cov=src/base60lab --cov-fail-under=95`
  - references: PLAN.md:712-725
  - acceptance: coverage ≥95% across all source modules
  - QA: `pytest --cov=src/base60lab --cov-report=term-missing --cov-fail-under=95`; manual: verify coverage report shows ≥95%
- [x] F3. All 10 experiments produce JSON/CSV/visualisation outputs
  - references: PLAN.md:727
  - acceptance: each experiment script generates JSON results, CSV measurements, and PNG/SVG visualisations
  - QA: `for f in experiments/*.py; do python "$f"; done && ls experiments/*.json experiments/*.csv experiments/*.png experiments/*.svg 2>/dev/null | head -40`; manual: verify outputs exist
- [x] F4. Findings documentation: all finding files have valid frontmatter with `status` and `version`
  - references: user scope addition
  - acceptance: every `.md` in `docs/findings/` has YAML frontmatter with `status:` and `version:` fields
  - QA: Python script to parse all frontmatter; manual: verify frontmatter validity
- [x] F5. No floating-point as internal arithmetic anywhere in source
  - references: PLAN.md:604-606 Control 2
  - acceptance: grep confirms no `float(`, `numpy.float`, or raw floating-point literals used as internal arithmetic in `src/base60lab/`
  - QA: `grep -rn "float(" src/base60lab/ || echo "NO FLOAT USAGE - PASS"`; manual: verify no float usage
