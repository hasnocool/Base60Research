| wave | workers_spawned | markers_gained | leads_opened | leads_closed |
|------|-----------------|----------------|--------------|--------------|
| 0 (decomposition) | 0 | 0 | 4 (intent-diff entries) | 0 |
| 1 (saturation) | 5 | 12 EXPAND + 12 CLAIMS | 2 codebase fixes + 9 literature leads + 5 experiment designs | 0 |
| 2 (expansion) | 10 | 25 EXPAND + 15 CLAIMS | 10 research leads verified | 6 dead ends |

Wave 2 leads verified:
- L-03 MR-OTP: Buono 2026 proves Shannon perfect secrecy for mixed-radix OTP; Horner's method for binary→mixed-radix; 15.62% key savings for 5×12 factorization vs binary OTP
- L-04 QKD→base-60: Buono 2606.18526 provides complete bias-free Algorithm 1, end-to-end QKD security proof
- L-05 MrRoPE: Tian et al. arXiv:2601.22181 unifies RoPE as radix conversion; MrRoPE-Pro progressive strategy for "train short, test long"
- L-06 Mixed-radix Cooley-Tukey: Salishev 2505.06728 — in-place mixed-radix DFT for vector-memory accelerators
- L-07 Mixed-radix tensor: Lin et al. 1903.08365 — 88% storage reduction (3D) / 62% (2D) for NUFFT
- L-07 CORDIC: Panchal 2604.23547 — FPGA-efficient mixed-radix CORDIC for sigmoid
- L-08 E8 Zenodo: Caldin 2026 — 32+ papers on Babylonian base-60; YBC 7290 reciprocal tables, Plimpton 322
- L-09 Qudit codes: Keppens 2025 — qudit stabilizer codes d=2,3,5 thresholds ~10⁻⁴; composite d=60 via CRT (Z₆₀≅Z₄×Z₃×Z₅)
- L-10 Qudit circuits: Litteken 2023 Qompress — 2 qubits→1 ququart, mixed-radix gates
- L-11 NTT 60-smooth: Gap in literature — van der Hoeven & Lecerf stop at 12-smooth; Liang & Zhao cover 3-smooth; no 60-smooth NTT literature
- L-12 Diophantine: Temur 2026 — numbers with simultaneously small CF and base-b entropy for ALL b≥2 including 60; Cohen 2025 — cubic algebraic CFs of polynomial type; YBC 7289 √2 ≈ 1;24,51,10 (4th convergent)
- L-12 Partition congruences: p(5n+4)≡0(5) prime 5 divides 60; Dedekind η 1/24 = 0;2,30 sexagesimal
- L-13 Kuramoto: Phase-locking depends on frequency difference, not representation
- L-14 Polygons: Mainik 2025 (arXiv:2505.14865) complete 65536-gon construction; Caldwell 2026 — base-60 matches 12 pentagonal faces (5×12=60)
- L-14 Hermes 1894 manuscript — 10-year 65537-gon construction; base-60 may appear implicitly
- L-15 Quantum KAM: Caldin 2026 — Δ(τ) coefficients mod 60 follow 60-cycle (to be verified/refuted)

Dead ends closed:
- D-01: General base conversion without mathematical structure — exhausted
- D-02: Direct "base-60 CF period length" papers — period is base-invariant (Lagrange)
- D-03: q-expansion base-60 digits — unexplored territory
- D-04: Base-aware coefficient encoding in lattice crypto — novel, no prior art
- D-05: 60-smooth NTT literature — stops at 12-smooth (2^i·3^j), no 5^c
- D-06: 10-smooth moduli — no literature; natural progression 2→12→60 smooth
- D-06: Non-prime qudit thresholds — all papers restrict to prime dimensions
- D-07: Composite-dimension decoders — none exist (MWPM, BM, HDRG assume prime fields)
- D-08: 10-smooth NTT — no literature; natural progression 2→12→60
- D-09: Crandall & Pomerance NTT chapter — predates PQC, no 60-smooth
- D-10: Plimpton 322 as trig table — anachronistic per Robson 2001
- D-09: Chinese rod numerals / Mayan vigesimal — no direct computational advantage
- D-10: Chinese translation NLP — irrelevant