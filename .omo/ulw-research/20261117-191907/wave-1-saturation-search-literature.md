# Wave 1 — Saturation: search-literature

## Worker: search-literature (librarian)

## Key Findings

1. **Babylonian exact sexagesimal trigonometry** — Mansfield & Wildberger 2017, "Plimpton 322 is Babylonian exact sexagesimal trigonometry", Historia Mathematica. Claims Plimpton 322 provides exact trigonometry via 5-smooth regular numbers 1500 years before Greeks. Counter: Robson 2001 argues algebraic not trigonometric interpretation.
2. **Mixed-radix Cooley-Tukey FFT** — Johnson & Frigo 2007, 2026. Efficient DFT for any 5-smooth size (2^a·3^b·5^c). Counter: Power-of-two FFT may win on some hardware due to memory access patterns.
3. **Number Theoretic Transform (NTT)** — Liang & Zhao 2022. Exact integer convolution without floating-point error. Counter: Requires prime modulus p ≡ 1 (mod 2n), limiting transform sizes.
4. **Direct base-to-base conversion** — Patil 2025, EngrXiv. O(m+d+p) algorithm avoiding decimal intermediate. Counter: Not yet peer-reviewed; benchmarking needed.
5. **12-smooth/60-smooth FFT sizes** — Steinbach & Werner "gearshifft" arXiv:1702.00629. Competitive vs powers of two. Counter: Implementation-dependent; radix-2 often better optimized.
6. **E8 Intelligence Research Zenodo papers (2026)** — Andrew Stewart Caldin, 10+ papers on Babylonian base-60, divisor lattices, harmonic systems, affine A1 root lattice connections.
7. **Schumacher 2016 smooth number formulas** — arXiv:1608.06928. Convergent formulas for 3-smooth, 5-smooth, 7-smooth counts.
8. **MrRoPE mixed-radix position embedding** — arXiv:2601.22181. Novel mixed-radix application to transformer position encoding.

## Sources
- Mansfield & Wildberger, Historia Mathematica 2017
- Johnson & Frigo, "Implementing FFTs in Practice", arXiv:2602.23525
- Liang & Zhao, "NTT and Applications", arXiv:2211.13546
- Patil, "Direct Base-to-Base Conversion", EngrXiv 2025
- Steinbach & Werner, "gearshifft", arXiv:1702.00629
- Schumacher, arXiv:1608.06928
- MrRoPE, arXiv:2601.22181

## EXPAND Markers
- LEAD: E8 Intelligence Research Zenodo papers (Caldin 2026) — WHY: 10+ recent computational papers on Babylonian base-60 directly relevant to Experiments B, E, G — ANGLE: Search zenodo.org Caldin Babylonian base-60
- LEAD: Schumacher 2016 smooth number distribution formulas — WHY: Can predict optimal FFT sizes near any target length — ANGLE: Implement formulas and test against gearshifft benchmarks
- LEAD: MrRoPE mixed-radix position embedding — WHY: Adaptable to phase/frequency representation in base-12/60 — ANGLE: Study code implementation and adapt for phase encoding
- LEAD: Patil 2025 direct base-to-base conversion — WHY: Core algorithm for base conversion without decimal intermediate — ANGLE: Download from engrxiv.org and implement in base60lab
- DEAD END: Chinese rod numerals / Mayan vigesimal — no direct computational advantage
- DEAD END: Ancient Chinese translation NLP papers — irrelevant to mathematical computation

## CLAIMS Markers
- CLAIM: Babylonian sexagesimal system provides exact trigonometry via 5-smooth regular numbers 1500 years before Greeks — RISK: normal — SOURCES: Mansfield & Wildberger 2017 — COUNTER: Robson 2001 argues algebraic interpretation — PRIMARY: Historia Mathematica 2017
- CLAIM: Mixed-radix Cooley-Tukey FFT efficient for any 5-smooth size — RISK: normal — SOURCES: Johnson & Frigo 2007/2026 — COUNTER: Power-of-two may win on some hardware — PRIMARY: arXiv:2602.23525
- CLAIM: NTT enables exact integer convolution without floating-point error — RISK: normal — SOURCES: Liang & Zhao 2022 — COUNTER: Requires p ≡ 1 (mod 2n) — PRIMARY: arXiv:2211.13546
- CLAIM: Direct base-to-base conversion avoids decimal intermediate — RISK: normal — SOURCES: Patil 2025 EngrXiv — COUNTER: Not peer-reviewed — PRIMARY: EngrXiv 2025
- CLAIM: 12-smooth/60-smooth FFT sizes competitive vs powers of two — RISK: normal — SOURCES: gearshifft arXiv:1702.00629 — COUNTER: Implementation-dependent — PRIMARY: arXiv:1702.00629
