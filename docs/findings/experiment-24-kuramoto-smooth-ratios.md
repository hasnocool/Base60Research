# Experiment 24: Kuramoto Oscillator Networks with Smooth Frequency Ratios

## Hypothesis
Phase-locking boundaries in Kuramoto oscillator networks with {2,3,5}-smooth frequency ratios are more clearly delineated in base-60 phase representation because the natural synchronization manifolds align with base-60's factor structure.

## Frequency Ratios Tested (5-Smooth)

| Ratio | Value | Base-60 |
|-------|-------|--------|
| 1:20 | 0.0500 | 1:20 |
| 1:18 | 0.0556 | 1:18 |
| 1:16 | 0.0625 | 1:16 |
| 1:15 | 0.0667 | 1:15 |
| 1:12 | 0.0833 | 1:12 |
| 1:10 | 0.1000 | 1:10 |
| 1:9 | 0.1111 | 1:9 |
| 1:8 | 0.1250 | 1:8 |
| 2:15 | 0.1333 | 2:15 |
| 3:20 | 0.1500 | 3:20 |
| 1:6 | 0.1667 | 1:6 |
| 3:16 | 0.1875 | 3:16 |
| 1:5 | 0.2000 | 1:5 |
| 2:9 | 0.2222 | 2:9 |
| 1:4 | 0.2500 | 1:4 |

## Network Configurations

### N3_basic
- Oscillators: 3
- Coupling K: Rational(1/2)
- Final order parameter: 0.0000
- Collective frequency: Rational(121/2160)
- Collective frequency (base-60): 0;3,L,<40>

Locked phase differences:
  - 0,1: 0 turns
  - 0,2: 0 turns
  - 1,2: 0 turns
### N5_harmonic
- Oscillators: 5
- Coupling K: Rational(1/2)
- Final order parameter: 0.0000
- Collective frequency: Rational(29/400)
- Collective frequency (base-60): 0;4,L

Locked phase differences:
  - 0,1: 0 turns
  - 0,2: 0 turns
  - 0,3: 0 turns
  - 0,4: 0 turns
  - 1,2: 0 turns
  - 1,3: 0 turns
  - 1,4: 0 turns
  - 2,3: 0 turns
  - 2,4: 0 turns
  - 3,4: 0 turns
### N8_extended
- Oscillators: 8
- Coupling K: Rational(3/4)
- Final order parameter: 0.0000
- Collective frequency: Rational(61/640)
- Collective frequency (base-60): 0;5,<43>,7,U

Locked phase differences:
  - 0,1: 0 turns
  - 0,2: 0 turns
  - 0,3: 0 turns
  - 0,4: 0 turns
  - 0,5: 0 turns
  - 0,6: 0 turns
  - 0,7: 0 turns
  - 1,2: 0 turns
  - 1,3: 0 turns
  - 1,4: 0 turns
  - 1,5: 0 turns
  - 1,6: 0 turns
  - 1,7: 0 turns
  - 2,3: 0 turns
  - 2,4: 0 turns
  - 2,5: 0 turns
  - 2,6: 0 turns
  - 2,7: 0 turns
  - 3,4: 0 turns
  - 3,5: 0 turns
  - 3,6: 0 turns
  - 3,7: 0 turns
  - 4,5: 0 turns
  - 4,6: 0 turns
  - 4,7: 0 turns
  - 5,6: 0 turns
  - 5,7: 0 turns
  - 6,7: 0 turns

## Phase Representation Comparison

| Network | Pair | Phase Diff | Base-10 | Base-12 | Base-60 | B10 Term | B12 Term | B60 Term |
|---------|------|------------|---------|---------|---------|----------|----------|----------|
| N3_basic | 0,1 | Rational(0) | True | True | True | True | True | True |
| N3_basic | 0,2 | Rational(0) | True | True | True | True | True | True |
| N3_basic | 1,2 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 0,1 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 0,2 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 0,3 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 0,4 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 1,2 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 1,3 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 1,4 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 2,3 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 2,4 | Rational(0) | True | True | True | True | True | True |
| N5_harmonic | 3,4 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,1 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,2 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,3 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,4 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,5 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 0,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,2 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,3 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,4 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,5 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 1,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 2,3 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 2,4 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 2,5 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 2,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 2,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 3,4 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 3,5 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 3,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 3,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 4,5 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 4,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 4,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 5,6 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 5,7 | Rational(0) | True | True | True | True | True | True |
| N8_extended | 6,7 | Rational(0) | True | True | True | True | True | True |

## Key Findings

- Terminating phase differences: Base-10: 41/41, Base-12: 41/41, Base-60: 41/41
❌ Base-60 does not significantly improve termination for these ratios.

## Controls Applied
- Same quantity: equal initial conditions per network
- Exact arithmetic: frequency ratios and phases as Rational
- Independent verification: cross-check with numerical ODE integration
- Equal conditions: same K, N, frequency sets across representations
- Negative results: reported where base-60 adds no clarity
