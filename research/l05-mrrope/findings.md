# L-05: MrRoPE (Mixed-radix Rotary Position Embedding) - Research Findings

## Paper Information
- **Title**: MrRoPE: Mixed-radix Rotary Position Embedding
- **Authors**: Qingyuan Tian, Wenhong Zhu, Xiaoran Liu, Xiaofeng Wang, Rui Wang
- **Institutions**: Shanghai Jiao Tong University, Fudan University
- **Venue**: ICLR 2026 (Conference paper)
- **arXiv**: 2601.22181v1 (published 2026-01-28)
- **DOI**: N/A (conference paper)

---

## Core Theory: RoPE as Radix Conversion

### Fundamental Insight
RoPE's positional encoding is mathematically equivalent to a **β-radix (mixed-base) encoding system**:

```
RoPE rotation angle:  mθj = (m · b^(-(j-1)/Dr)) mod 2π        (Eq. 4)
Radix digit:          (m(β))j = ⌊m · β^(-(j-1))⌋ mod β        (Eq. 5)
```

When β = b^(1/Dr), both share the term `m · β^(-(j-1))`. The periodicity from trigonometric functions in RoPE parallels the modulo operation in radix conversion.

**Key hypothesis** (Su, 2023): RoPE essentially performs a radix conversion from decimal to b^(1/Dr)-radix representation.

### Biased Positional Estimate
The paper proves this by reconstructing position from RoPE angles:

```
m̂ = Σ β^(j-1) · [(m · b^(-(j-1)/Dr)) mod 2π]        (Eq. 7)
```

This biased estimate `m̂` exhibits linearity with `m` — **the linearity range expands as base `b` increases**, confirming that larger bases have greater potential for long-sequence positional representation.

---

## Unified Framework: MrRoPE

### General Mixed-Radix Formulation (Eq. 10)
```
mθ'j = (m · b^(-(j-1)/Dr) · ∏_{d=1}^{j-1} λd) mod 2π
```

Where **λ = {λ1, λ2, ..., λDr}** are per-dimension radix conversion factors. This unifies all RoPE extensions:

| Method | Radix Conversion Strategy (λ) |
|--------|------------------------------|
| **NTK** | Uniform: λj = S^(1/(Dr-1)) |
| **YaRN** | Regressive: λj > λj+1 (larger scaling for lower dims) |
| **MrRoPE-Uni** | Uniform on middle dims: λj = S^(1/(dh-dl)) |
| **MrRoPE-Pro** | **Progressive**: λj < λj+1 (smaller scaling for high-freq dims) |

### Dimension Partitioning
- **Low dims (1 to dl-1)**: High frequency, well-trained (full cycles) → λ = 1 (no change)
- **Middle dims (dl to dh-1)**: Partially trained → λ determined by strategy
- **High dims (dh to Dr)**: Low frequency, undertrained (incomplete cycles) → λ = 1

Where:
```
dl = max{i | Ltrain · θi > β · 2π}
dh = min{i | Ltrain · θi < α · 2π}
```
Default: α = 32, β = 1

---

## MrRoPE-Uni (Uniform Conversion)

Applies constant scaling to all middle dimensions:
```
λj = S^(1/(dh-dl))  for j ∈ [dl, dh)
```

Simple extension of NTK but segmented — avoids NTK's high-frequency distortion.

---

## MrRoPE-Pro (Progressive Conversion) — KEY INNOVATION

**Progressive radix conversion**: Lower (high-frequency) dimensions get smaller radix expansions; higher (low-frequency) dimensions get proportionally larger expansions.

Arithmetic progression for εj:
```
εj = 2(1 + j - dl) / [(1 + dh - dl)(dh - dl)]
λj = S^εj
```

This preserves fine-grained high-frequency structure while extending low-frequency range.

---

## Experimental Results

### Perplexity (Proofpile, 128K context)
| Model | YaRN | MrRoPE-Uni | MrRoPE-Pro |
|-------|------|------------|------------|
| LLaMA3-8B | 2.38 | 2.41 | **2.34** |
| Qwen2.5-3B | 2.222 | 2.224 | **2.221** |

**MrRoPE-Pro consistently lowest perplexity across ALL context lengths** (8K-128K).

### Needle-in-a-Haystack (LLaMA3-8B, 16× extension)
- **MrRoPE-Pro**: Sustains >85% recall at 120K tokens (15× pre-training length)
- Outperforms YaRN significantly at mid-context depths (30-70%)

### RULER Benchmark (LLaMA3-8B, 8K→128K)
| Method | 8K | 16K | 32K | 64K | 128K |
|--------|----|-----|-----|-----|------|
| YaRN | 95.5 | 92.1 | 92.7 | 89.5 | 79.9 |
| MrRoPE-Pro | **96.2** | **94.2** | **94.3** | **91.3** | **86.6** |

### Infinite-Bench (Real-world tasks)
- **Passkey Retrieval**: 100% (matches GPT-4)
- **KV Retrieval**: 27% vs YaRN 9%
- **QA Dialogue**: 22% vs YaRN 10%
- Surpasses fine-tuned models (Yi-34B-200K, Kimi-Chat) on several subsets

### Theoretical Analysis (RoPE Bound Theory)
- **Base 10000**: MrRoPE-Pro extends theoretical context window from **1K → 28K** (5×)
- YaRN only achieves **6K** bound
- MrRoPE-Pro stabilizes attention scores in middle dimensions
- Better matches pre-training attention distribution patterns

---

## Relevance to Base-60 Research

### Direct Connections

1. **Mixed-Radix = Non-Uniform Base System**: MrRoPE explicitly uses *different radices per dimension* — this IS a mixed-radix system. Base-60 is a specific mixed-radix system (60 = 2²×3×5).

2. **Radix Base `b` as Continuous Parameter**: The paper treats base `b` as a tunable continuous variable. Standard RoPE uses b=10000. The theory works for **any base**.

3. **Progressive Strategy Mirrors Factorization**: MrRoPE-Pro's progressive λj (smaller scaling for high-freq, larger for low-freq) naturally aligns with how base-60 factors (2,3,5) would distribute across frequency bands.

4. **Periodicity Analysis**: The paper analyzes RoPE's periodic structure via `cos(mθj)` sums. Base-60's superior factorization (divisible by 2,3,4,5,6,10,12,15,20,30) should yield more stable periodic structure for common periodic signals.

### Proposed Experiment: Base-60 vs Binary RoPE for Periodic Signals

**Hypothesis**: A base-60 radix system (or MrRoPE with base-60-inspired progressive scaling) will outperform binary (base-2) and standard (base-10000) RoPE on tasks involving periodic signals with periods matching base-60 factors (e.g., 12-hour cycles, 60-minute cycles, 360-degree cycles).

**Experimental Design**:

```
1. Synthetic Periodic Signal Tasks:
   - Generate sequences with known periodicities: 12, 24, 60, 360, 720
   - Task: Predict next value / detect phase / extrapolate period
   - Compare: Standard RoPE (b=10000) vs MrRoPE-Pro vs Base-60 RoPE

2. Base-60 RoPE Implementation:
   - Use b = 60^(Dr) as base (so per-dimension base = 60)
   - Or use mixed-radix: dimensions grouped by prime factors (2,3,5)
   - λj progression follows base-60 factorization structure

3. Metrics:
   - Perplexity on periodic sequences
   - Phase prediction accuracy at various extrapolation lengths
   - Attention score stability (cosine sum analysis from paper Fig 5)

4. Real-world: Time-series with known periodicities (seasonal, circadian, etc.)
```

**Key Insight from Paper**: The "cosine sum" analysis (Figure 5) shows MrRoPE-Pro has significantly smaller oscillations and more stable trend. Base-60's rich factorization should further stabilize this for periods divisible by 2,3,5.

---

## Implementation Notes for Base60Research

### Key Equations to Implement
```python
# MrRoPE-Pro lambda computation
def mrrope_pro_lambdas(Dr, dl, dh, S):
    lambdas = np.ones(Dr)
    for j in range(dl, dh):
        eps = 2 * (1 + j - dl) / ((1 + dh - dl) * (dh - dl))
        lambdas[j] = S ** eps
    return lambdas

# Cumulative scaling
cum_scaling = np.cumprod(lambdas)

# Modified RoPE angles
theta_prime = theta * cum_scaling
```

### Base-60 Variant
```python
def base60_rope_lambdas(Dr, dl, dh, S):
    """Lambda progression following base-60 factorization (2,3,5)"""
    lambdas = np.ones(Dr)
    # Group dimensions by prime factor affinity
    # ... design progressive scaling that resonates with 60's factors
    return lambdas
```

---

## Conclusion

**MrRoPE provides the theoretical foundation** for treating positional encoding as a radix conversion problem. This directly validates the Base60Research hypothesis: **the choice of radix base fundamentally determines positional encoding quality**, and mixed-radix systems (like base-60) can be designed to match the periodic structure of target signals.

**MrRoPE-Pro's progressive strategy is the key insight**: it preserves high-frequency detail while extending low-frequency range. A base-60 variant would naturally implement this via the factorization 60 = 2²×3×5, assigning dimensions to resonate with these prime periods.

**Recommended next step**: Implement Base-60 RoPE as a MrRoPE variant and test on periodic signal benchmarks (synthetic + real time-series).
