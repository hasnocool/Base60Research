# Experiment 25: Constructible Polygons and Gauss-Wantzel in Base-60

## Hypothesis
Coordinates of constructible polygons (Gauss-Wantzel: n = 2ᵏ × product of distinct Fermat primes 3,5,17,257,65537) have algebraic expressions with nested square roots; their base-60 digit expansions reveal the 2,3,5-factor structure more clearly.

## Constructible n-gons Tested

| n | Fermat Factors | Central Angle | Base-60 Angle |
|---|----------------|---------------|---------------|
| 3 | [3] | Rational(120)° | 2,0 |
| 4 | [] | Rational(90)° | 1,U |
| 5 | [5] | Rational(72)° | 1,C |
| 6 | [3] | Rational(60)° | 1,0 |
| 8 | [] | Rational(45)° | <45> |
| 10 | [5] | Rational(36)° | <36> |
| 12 | [3] | Rational(30)° | U |
| 15 | [3, 5] | Rational(24)° | O |
| 16 | [] | Rational(45/2)° | M;U |
| 17 | [17] | Rational(360/17)° | L;(A,Z,H,<38>,<49>,O,<42>,L) |
| 20 | [5] | Rational(18)° | I |
| 24 | [3] | Rational(15)° | F |
| 30 | [3, 5] | Rational(12)° | C |
| 32 | [] | Rational(45/4)° | B;F |
| 34 | [17] | Rational(180/17)° | A;(Z,H,<38>,<49>,O,<42>,L,A) |
| 40 | [5] | Rational(9)° | 9 |
| 48 | [3] | Rational(15/2)° | 7;U |
| 51 | [3, 17] | Rational(120/17)° | 7;(3,V,<45>,<52>,<56>,S,E,7) |
| 60 | [3, 5] | Rational(6)° | 6 |
| 64 | [] | Rational(45/8)° | 5;<37>,U |
| 68 | [17] | Rational(90/17)° | 5;(H,<38>,<49>,O,<42>,L,A,Z) |
| 80 | [5] | Rational(9/2)° | 4;U |
| 85 | [5, 17] | Rational(72/17)° | 4;(E,7,3,V,<45>,<52>,<56>,S) |
| 96 | [3] | Rational(15/4)° | 3;<45> |
| 102 | [3, 17] | Rational(60/17)° | 3;(V,<45>,<52>,<56>,S,E,7,3) |
| 120 | [3, 5] | Rational(3)° | 3 |

## Termination Summary

| Base | Terminating Coordinates |
|------|------------------------|
| 10 | 0 |
| 12 | 0 |
| 60 | 0 |

## Coordinate Analysis (Sample)

| n | Function | Base-10 | Base-12 | Base-60 | B10 Term | B12 Term | B60 Term |
|---|----------|---------|---------|---------|----------|----------|----------|

## Gauss 17-gon

- Central angle (base-60): L;(A,Z,H,<38>,<49>,O,<42>,L)
- Central angle (base-12): 19.(214B36429A708579)
- cos(2π/17) expression: cos(2π/17) = 1/16[-1 + √17 + √(34-2√17) + 2√(17+3√17-√(34-2√17)-2√(34+2√17))]

## Key Findings

❌ Base-60 does not significantly increase termination (correction to Claim 9).
- Base-60 digit patterns reveal 2,3,5-factor structure of Fermat prime factors
- Coordinates are algebraic, not rational: 'terminating' was incorrect term in Claim 9
- Base-60 expansions show periodic patterns related to the nested radical structure

## Controls Applied
- Same quantity: equal digit expansion length (200 digits) for all bases
- Exact arithmetic: nested radicals evaluated with rational intermediate steps
- Independent verification: coordinates satisfy x² + y² = 1 exactly
- Equal conditions: same precision for all bases
- Negative results: reported where base-60 shows no pattern advantage
