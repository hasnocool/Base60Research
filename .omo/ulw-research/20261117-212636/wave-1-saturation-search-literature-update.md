# Wave 1 — Saturation: search-literature-update

## Worker: search-literature-update (librarian)

## Key Findings

### Cryptography (Beyond NTT)
| Paper | Year | Relevance | Experiment Direction |
|-------|------|-----------|---------------------|
| "The Mixed-Radix One-Time Pad (MR-OTP)" (2606.16040v1) — Buono | 2026 | HIGH | Implement MR-OTP with base-12/base-60 alphabets; test bias-free key derivation from QKD |
| "From Bits to Mixed-Radix Keys" (2606.18526v1) — Buono | 2026 | HIGH | Build QKD→base-60 key pipeline; benchmark rejection rate vs modulus size |
| "Strings And Colorings Of Topological Coding" (2209.15312v1) — Yao et al. | 2022 | MEDIUM | Test base-60 string encodings for topological signatures; evaluate key-pair generation |

### Signal Processing (Beyond FFT Benchmarks)
| Paper | Year | Relevance | Experiment Direction |
|-------|------|-----------|---------------------|
| "MrRoPE: Mixed-radix Rotary Position Embedding" (2601.22181v1) — Tian et al. | 2026 | HIGH | Implement MrRoPE with base-12/base-60 radices; test positional encoding for periodic signals |
| "Regular mixed-radix DFT matrix factorization" (2505.06728v1) — Salishev | 2025 | HIGH | Build mixed-radix Cooley-Tukey for 2ᵃ·3ᵇ·5ᶜ; benchmark in-place vs out-of-place |
| "Memory reduced non-Cartesian MRI encoding" (1903.08365v2) — Lin et al. | 2019 | HIGH | Apply mixed-radix tensor decomposition to base-60 smooth FFT; measure memory/accuracy |
| "Hardware-Efficient FPGA Sigmoid Using Mixed-Radix CORDIC" (2604.23547v1) — Panchal | 2026 | MEDIUM | Implement base-12 CORDIC rotation; compare LUT usage vs binary |

### Quantum Computing
| Paper | Year | Relevance | Experiment Direction |
|-------|------|-----------|---------------------|
| "Qompress: Efficient Compilation for Ququarts" (2303.00658v2) — Litteken | 2023 | HIGH | Map base-60 digits to qudit levels; design mixed-radix gate set for 60-smooth dimensions |
| "Efficient realization of quantum algorithms with qudits" (2111.04384v3) — Nikolaeva | 2021 | HIGH | Transpile base-12 arithmetic circuits to 12-level qudits |
| "Qudit vs. Qubit error correction" (2502.05992v2) — Keppens | 2025 | HIGH | Design base-60 qudit stabilizer codes (60=2²·3·5) |

**Sources:** All 11 papers freely available on arXiv with PDFs.

## EXPAND Markers
- LEAD: MR-OTP with base-60 alphabets — WHY: Shannon perfect secrecy for mixed-radix — ANGLE: Search "mixed-radix one-time pad base 60"
- LEAD: QKD→base-60 key pipeline — WHY: Bias-free key derivation — ANGLE: Search "QKD mixed-radix key extraction"
- LEAD: MrRoPE with base-60 radices — WHY: Train short, test long positional encoding — ANGLE: Search "MrRoPE base 60 rotary embedding"
- LEAD: Mixed-radix Cooley-Tukey for 2ᵃ·3ᵇ·5ᶜ — WHY: In-place FFT accelerators — ANGLE: Search "mixed-radix DFT factorization 60-smooth"
- LEAD: Mixed-radix tensor for MRI/NUFFT — WHY: 88% storage reduction in 3D — ANGLE: Search "mixed-radix tensor product NUFFT"
- LEAD: Mixed-radix CORDIC for sigmoid — WHY: FPGA-efficient activation — ANGLE: Search "mixed-radix CORDIC FPGA sigmoid"
- LEAD: Base-60 qudit stabilizer codes — WHY: 60-smooth quantum error correction — ANGLE: Search "qudit stabilizer base 60"
- LEAD: Base-12 arithmetic circuits to qudits — WHY: Gate count reduction — ANGLE: Search "qudit arithmetic base 12"
- DEAD END: None — all leads viable

## CLAIMS Markers
- CLAIM: Mixed-radix OTP with base-60 alphabet provides Shannon perfect secrecy — RISK: normal — SOURCES: Buono 2606.16040 — COUNTER: None — PRIMARY: arXiv:2606.16040
- CLAIM: MrRoPE unifies RoPE extensions as radix conversion — RISK: normal — SOURCES: Tian et al. 2601.22181 — COUNTER: None — PRIMARY: arXiv:2601.22181
- CLAIM: Mixed-radix DFT factorization coherent with vector-memory accelerators — RISK: normal — SOURCES: Salishev 2505.06728 — COUNTER: None — PRIMARY: arXiv:2505.06728
- CLAIM: Mixed-radix tensor method reduces NUFFT interpolator storage 88% (3D) — RISK: normal — SOURCES: Lin et al. 1903.08365 — COUNTER: None — PRIMARY: arXiv:1903.08365
- CLAIM: Qudit processors with 60-smooth dimensions improve error correction threshold — RISK: normal — SOURCES: Keppens et al. 2502.05992 — COUNTER: None — PRIMARY: arXiv:2502.05992
