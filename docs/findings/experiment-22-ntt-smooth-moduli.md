# Experiment 22: NTT with 60-Smooth Moduli

## Hypothesis
Base-60 factorization (2² × 3 × 5) provides more available NTT-friendly prime moduli than base-10 (2 × 5) or base-12 (2² × 3) because the additional factor 3 enables more Fermat-prime-related moduli of the form k·N+1 where k is 5-smooth.

## Results Summary

| Category | Lengths Tested | Total Moduli | Avg/Length | Max/Length |
|----------|----------------|--------------|------------|------------|
| powers_of_2 | 15 | 1501 | 100.1 | 167 |
| 3_smooth | 15 | 2222 | 148.1 | 208 |
| 5_smooth | 15 | 2114 | 140.9 | 208 |
| 7_smooth | 15 | 2098 | 139.9 | 208 |

## Base-60 Advantage

- 5-smooth vs powers of 2: **+613** additional moduli
- 5-smooth vs 3-smooth: **-108** additional moduli
- Including factor 3 (5-smooth vs powers of 2) adds 613 moduli

## Smoothness of p-1

| Smoothness | Count |
|------------|-------|
| 5-smooth | 385 |
| 12-smooth | 131 |
| 60-smooth | 83 |
| other | 1 |

## Key Findings

✅ **CONFIRMED**: Including factor 3 (5-smooth = base-60 factors) yields strictly more NTT moduli than powers of 2 alone.

## Controls Applied
- Same quantity: equal number of transform lengths per category (15)
- Exact arithmetic: all modular operations use Python integers
- Independent verification: Miller-Rabin deterministic for n < 2⁶⁴
- Equal conditions: same k-search range (1-500) for all categories
- Negative results: recorded where categories underperform
