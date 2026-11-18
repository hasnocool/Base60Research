# Experiment 23: Continued Fractions and Diophantine Approximation in Base-60

## Hypothesis
While continued fraction *period lengths* are base-invariant, the *digit patterns* of convergents and the *visibility* of near-integer relationships are enhanced in base-60 for constants with 2,3,5-factor-related algebraic structure.

## Notable Pi Approximants (Testing Claim 10)

| Approximant | Base-10 Digits | Base-12 Digits | Base-60 Digits |
|-------------|----------------|----------------|----------------|
| 3/1 | 1/1 | 1/1 | 1/1 |
| 22/7 | 2/1 | 2/1 | 1/1 |
| 333/106 | 3/3 | 3/2 | 3/6 |
| 355/113 | 3/3 | 3/2 | 6/6 |
| 103993/33102 | 6/5 | 5/5 | 8/8 |
| 104348/33215 | 6/5 | 5/5 | 8/5 |
| 208341/66317 | 6/5 | 5/5 | 11/5 |

## Average Digit Efficiency (Base-60 / Base-10)

| Constant | Ratio |
|----------|-------|
| pi | 1.460 |
| e | 1.110 |
| sqrt2 | 1.000 |
| sqrt3 | 1.000 |
| sqrt5 | 1.083 |
| sqrt6 | 0.979 |
| sqrt10 | 1.222 |
| sqrt12 | 1.250 |
| sqrt15 | 0.833 |
| sqrt30 | 1.117 |
| phi | 0.967 |
| ln2 | 1.058 |
| zeta3 | 1.168 |

## Key Findings

- Pi approximants: Base-60 more compact in 1/7 cases, Base-10 more compact in 5/7 cases
- Continued fraction period lengths are base-invariant (confirmed by theory)
- Base-60 digit patterns of convergents differ and may reveal structure

## Controls Applied
- Same quantity: equal number of convergents (30) per constant
- Exact arithmetic: all rational operations use Rational class
- Independent verification: convergents match known OEIS values
- Equal conditions: same max_n for all constants
- Negative results: reported where base-60 offers no advantage
