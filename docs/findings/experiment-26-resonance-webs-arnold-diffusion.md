# Experiment 26: Resonance Webs and Arnold Diffusion in Base-60

## Hypothesis
In coupled multi-frequency oscillator systems (n ≥ 4), the resonance web structure is more navigable in base-60 frequency space because the 2,3,5-factorization naturally aligns with dominant low-order resonances that govern transport.

## Dimension Analysis

| Dimension | Frequencies | Resonances | Web Edges | Diffusion Paths | Diophantine Quality |
|-----------|-------------|------------|-----------|-----------------|---------------------|
| dim_4 | 4 | 2 | 1 | 0 | 0.0000 |
| dim_5 | 5 | 8 | 24 | 1048 | 0.0000 |
| dim_6 | 6 | 20 | 162 | 75024 | 0.0000 |

## Frequency Vectors (Base-60)

### dim_4
- ω_1 = Rational(1/18) = 0;3,K (base-60)
- ω_2 = Rational(1/16) = 0;3,<45> (base-60)
- ω_3 = Rational(1/15) = 0;4 (base-60)
- ω_4 = Rational(1/12) = 0;5 (base-60)

### dim_5
- ω_1 = Rational(1/18) = 0;3,K (base-60)
- ω_2 = Rational(1/16) = 0;3,<45> (base-60)
- ω_3 = Rational(1/15) = 0;4 (base-60)
- ω_4 = Rational(1/12) = 0;5 (base-60)
- ω_5 = Rational(1/10) = 0;6 (base-60)

### dim_6
- ω_1 = Rational(1/18) = 0;3,K (base-60)
- ω_2 = Rational(1/16) = 0;3,<45> (base-60)
- ω_3 = Rational(1/15) = 0;4 (base-60)
- ω_4 = Rational(1/12) = 0;5 (base-60)
- ω_5 = Rational(1/10) = 0;6 (base-60)
- ω_6 = Rational(1/9) = 0;6,<40> (base-60)

## Sample Resonances (dim=4)

| Vector | Order | Strength | Base-10 | Base-60 |
|--------|-------|----------|---------|---------|
| (-3, 0, 0, 2) | 5 | 0.200 | (-3,0,0,2) | (-3,0,0,2) |
| (3, 0, 0, -2) | 5 | 0.200 | (3,0,0,-2) | (3,0,0,-2) |

## Sample Diffusion Paths

### dim_4

### dim_5
Path 1: (-3, 0, 0, 2, 0) → (-3, 0, 1, 0, 1) → (0, 0, -3, 0, 2)
Path 2: (-3, 0, 0, 2, 0) → (-3, 0, 1, 0, 1) → (0, 0, -3, 0, 2)
Path 3: (-3, 0, 0, 2, 0) → (-3, 0, 1, 0, 1) → (0, 0, -3, 0, 2)
Path 4: (-3, 0, 0, 2, 0) → (-3, 0, 1, 0, 1) → (0, 0, -3, 0, 2)
Path 5: (-3, 0, 0, 2, 0) → (-3, 0, 1, 0, 1) → (0, 0, -1, 2, -1)

### dim_6
Path 1: (-4, 0, 0, 0, 0, 2) → (-3, 0, 0, 2, 0, 0) → (-3, 0, 1, 0, 1, 0)
Path 2: (-4, 0, 0, 0, 0, 2) → (-3, 0, 0, 2, 0, 0) → (-3, 0, 1, 0, 1, 0)
Path 3: (-4, 0, 0, 0, 0, 2) → (-3, 0, 0, 2, 0, 0) → (-3, 0, 1, 0, 1, 0)
Path 4: (-4, 0, 0, 0, 0, 2) → (-3, 0, 0, 2, 0, 0) → (-3, 0, 1, 0, 1, 0)
Path 5: (-4, 0, 0, 0, 0, 2) → (-3, 0, 0, 2, 0, 0) → (-3, 0, 1, 0, 1, 0)

## Key Findings

- Resonance vector notation: Base-10 total 406 chars, Base-60 total 406 chars
❌ Base-60 does not provide more compact notation for these vectors.
- Resonance web connectivity increases with dimension (expected)
- Diophantine quality measures KAM stability
- Denominator family analysis from Experiment 20 extended to web context

## Controls Applied
- Same quantity: equal resonance order cutoff (|k| ≤ 6) for all representations
- Exact arithmetic: all resonance conditions with Rational
- Independent verification: cross-check with numerical Hamiltonian integration
- Equal conditions: same frequency vectors, same max_order
- Negative results: reported where base-60 adds no insight
