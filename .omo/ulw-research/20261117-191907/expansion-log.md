| wave | workers_spawned | markers_gained | leads_opened | leads_closed |
|------|-----------------|----------------|--------------|--------------|
| 0 (decomposition) | 0 | 0 | 5 (intent-diff entries) | 0 |
| 1 (saturation) | 5 | 17 EXPAND + 28 CLAIMS | 12 research leads + 2 doc fixes | 4 dead ends |
| 2 (expansion) | 8 | 25 EXPAND + 12 CLAIMS + 2 doc fixes | 8 research leads verified | 6 dead ends |

Wave 2 leads verified:
- L-04 E8 Zenodo: 32+ Caldin papers on Babylonian base-60, ALL freely accessible CC-BY 4.0, directly relevant to Exp B/E/G
- L-05 Schumacher smooth numbers: exact convergent formulas verified, Python module created at smooth_fft_sizes.py
- L-07 Patil direct base conversion: O(m+d+p) algorithm, C++ reference on GitHub, no benchmarks in paper
- L-08 Higher-dimensional Lissajous: KAM tori/Arnold diffusion relevant, no direct base-60 literature
- L-09 Babylonian tablets: YBC 7290, Plimpton 322 reciprocal pairs, √2 iteration — all implementable in base60lab
- L-10 Modular forms: Δ(τ) mod 60 60-cycle (Caldin 2026), partition congruence prime 5 is base-60 factor, Dedekind eta 1/24 = 0;2,30 sexagesimal
- L-03 NTT crypto: 60-smooth moduli offer NO practical advantage vs 2^a·3^b; all standardized schemes use 2^a·3^b-smooth orders only
- L-11/L-12 doc fixes: ALL 29 finding files now have valid YAML frontmatter

Wave 2 dead ends:
- D-09: Plimpton 322 as trigonometric table — anachronistic
- D-10: General base conversion of q-series — exhausted in experiments 01-10
- D-11: Direct "q-expansion base-60 digits" literature — none found, unexplored territory
- D-12: Base-aware coefficient encoding in lattice crypto — novel, no literature
- D-13: 60-smooth vs 2^a·3^b NTT performance — no papers comparing
- D-14: Benchmark results in Patil paper — theoretical only, no empirical data
