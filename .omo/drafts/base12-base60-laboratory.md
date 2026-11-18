---
slug: base12-base60-laboratory
status: awaiting-approval
intent: clear
review_required: false
pending-action: write .omo/plans/base12-base60-laboratory.md
approach: Convert the existing PLAN.md research programme into a decision-complete ulw-plan work plan under `.omo/plans/`. The plan implements the full Base-12 / Base-60 Mathematical Research Programme as a Python package (`base60lab`) with 11 source modules, 10 experiment scripts, a pytest suite, pyproject.toml packaging, docs, and a 7-milestone roadmap — all scoped directly from PLAN.md. PLUS: a documentation dir `base12-base60-laboratory/docs/findings/` holding statically-named finding files, each semantically versioned with a changelog, emphasizing provably true findings.
---

# Draft: base12-base60-laboratory

## Components (topology ledger)
<!-- Lock the SHAPE before depth. One row per top-level component that can succeed or fail independently. -->
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

## Open assumptions (announced defaults)
<!-- Record any default you adopt instead of asking, so the user can veto it at the gate. -->
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

## Decisions (with rationale)
| Decision | Rationale | Evidence |
| Implement as Python package `base60lab` under `base12-base60-laboratory/src/base60lab/` | PLAN.md:638-662 names this module path | PLAN.md:638 |
| Keep mathematical engine independent of visualisation layer | Enables later browser dashboard or Rust rewrite without rewriting research | PLAN.md:710 |
| Exact rational arithmetic internally; base is presentation only | Prevents false patterns from floating-point rounding | PLAN.md:92-95 |
| 11 source modules + 10 experiment scripts + tests + docs | Full scope per PLAN.md architecture section | PLAN.md:638-727 |
| 7 milestones as implementation waves | Matches PLAN.md roadmap | PLAN.md:735-771 |
| Findings documentation dir `docs/findings/` with static file names, semver, changelogs, `proven` status field | User requirement: document all findings, emphasize provably true, static names, semver + changelogs | user scope addition |

## Scope IN
| In scope | Boundary |
| All 11 source modules in `src/base60lab/` | PLAN.md:638-662 |
| All 10 experiment scripts `experiments/01_...py` through `10_combined_experiments.py` | PLAN.md:664-684 |
| pytest test suite covering the 11 listed test areas | PLAN.md:712-725 |
| pyproject.toml packaging | PLAN.md:692 |
| docs/: RESEARCH_PLAN.md, HYPOTHESES.md, EXPERIMENT_PROTOCOLS.md, RESULTS.md | PLAN.md:630-636 |
| data/ and results/ directories | PLAN.md:688-690 |
| `docs/findings/` finding files: static names, semver versioning, changelogs, `proven` status emphasis | User scope addition | user scope addition |

## Scope OUT (Must NOT have)
| Item | Reason |
| No browser dashboard / web UI | PLAN.md:710 keeps engine independent; dashboard is a later option |
| No Rust implementation in this plan | PLAN.md:710 mentions Rust as a later possibility |
| No musical tuning as a numeric-base experiment | PLAN.md:300 explicitly distinguishes twelve-tone scale from base-12 number system |
| No floating-point as internal arithmetic | PLAN.md:604-606 Control 2 |
| No renamed/versioned file copies (e.g. `findings-v2.md`) | Static names required; amendments happen in place via semver+changelog | user scope addition |

## Open questions
| Question | Options | Recommended default |
| Decision | Decision made |
| git-ignore results/ and data/ | ignore (derivable outputs) |
| Should `results/` and `data/` be git-ignored? | ignore / commit | ignore (derivable outputs) |
| One aggregate `CHANGELOG.md` in `docs/findings/` vs one per finding file? | aggregate / per-file | aggregate (simpler, single source of truth) |

status: approved
<!-- Approval given by user on 2026-11-17; git-ignore=ignore. Plan creation authorized. -->
## Approval gate
status: awaiting-approval
<!-- When exploration is exhausted and unknowns are answered, set status: awaiting-approval. -->
<!-- That durable record is the loop guard: on a later turn read it and resume at the gate instead of re-running exploration. -->
