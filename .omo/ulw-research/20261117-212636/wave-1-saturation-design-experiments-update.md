# Wave 1 — Saturation: design-experiments-update

## Worker: design-experiments-update (plan)

## Key Findings

### 5 New Experiment Designs (numbered 22-26)

| # | Experiment | Hypothesis | Literature Source |
|---|-----------|-----------|-------------------|
| 22 | NTT with 60-smooth moduli for post-quantum crypto | Base-60 factorization yields more NTT-friendly primes; impacts RLWE/MLWE parameters | Crandall & Pomerance NTT chapter |
| 23 | Diophantine approximation of algebraic numbers in base-60 | Base-60 reveals structure in continued fraction convergents for √d; generalizes to cubic irrationals | Standard number theory (Lagrange) |
| 24 | Kuramoto synchronization with irrational frequency ratios | Base-60 representation of phase-locking boundaries for quadratic/cubic irrationals | Strogatz "Sync" (2003) |
| 25 | Constructible polygon coordinates for n > 120 | Gauss-Wantzel coordinates have deeper nested radicals; base-60 digit patterns | Gauss's Disquisitiones Arithmeticae |
| 26 | Quantum resonance webs and KAM stability in base-60 | Quantum analogues (Floquet theory, quantum chaos) benefit from base-60 frequency spectra | Arnold KAM theorem literature |

## EXPAND Markers
- LEAD: Higher-dimensional NTT with 60-smooth moduli — WHY: RLWE/MLWE parameter impact — ANGLE: Search "NTT 60-smooth cryptography"
- LEAD: Base-60 digit patterns in Diophantine approximation — WHY: Generalize to cubic irrationals — ANGLE: Search "algebraic number base 60"
- LEAD: Kuramoto synchronization with irrational ratios — WHY: Real-world oscillators often irrational — ANGLE: Search "Kuramoto irrational frequencies"
- LEAD: Constructible polygons n > 120 — WHY: 257-gon, 65537-gon coordinates — ANGLE: Search "65537-gon base 60"
- LEAD: Quantum resonance webs and KAM — WHY: Floquet theory, quantum chaos — ANGLE: Search "quantum KAM base representation"
- DEAD END: General base conversion as discovery tool without mathematical structure — exhausted in experiments 01-10

## CLAIMS Markers
- CLAIM: Base-60 factorization provides strictly more NTT-friendly primes than base-10 or base-12 — RISK: low — SOURCES: NTT literature — COUNTER: None — PRIMARY: Crandall & Pomerance
- CLAIM: Continued fraction period lengths are base-invariant but base-60 digit patterns reveal algebraic structure — RISK: normal — SOURCES: number theory — COUNTER: None — PRIMARY: Lagrange theorem
- CLAIM: Phase-locked states in Kuramoto with 5-smooth ratios have more terminating phase representations in base-60 — RISK: normal — SOURCES: synchronization theory — COUNTER: Depends on frequency difference, not representation — PRIMARY: Strogatz 2003
- CLAIM: Constructible polygon coordinates have base-60 digit patterns but are not rational — RISK: normal — SOURCES: algebraic number theory — COUNTER: Coordinates involve nested radicals, not rational — PRIMARY: Gauss Disquisitiones
- CLAIM: Resonance web vectors have more compact notation in base-60 — RISK: normal — SOURCES: KAM theory — COUNTER: None — PRIMARY: Arnold KAM literature
