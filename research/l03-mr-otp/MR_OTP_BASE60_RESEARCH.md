# MR-OTP with Base-60 Alphabets: Research Findings (Lead L-03)

**Paper**: "New Ideas on a New Old Type of Cipher: The Mixed-Radix One-Time Pad" (Buono, 2026) — arXiv:2606.16040v1  
**Follow-up**: "From Bits to Mixed-Radix Keys: Horner Decomposition, Uniform Sampling, and the Information-Theoretic QKD Interface of the MR-OTP" (Buono, 2026) — arXiv:2606.18526v1  
**2012 Preprint**: "A New Type of Cipher" (Buono) — arXiv:1202.2004v3

---

## 1. Shannon Perfect Secrecy for Mixed-Radix Alphabets

### MR-OTP Definition (Buono 2026, Section 2.2)
- **Bases**: Fixed sequence B = (b₁, ..., bₗ) with each bᵢ ≥ 2
- **Key space**: K = Πᵢ {0, 1, ..., bᵢ - 1} — uniform random key K = (k₁, ..., kₗ)
- **Message space**: Dᴮ = Πᵢ {0, 1, ..., bᵢ - 1} — message M = (m₁, ..., mₗ)
- **Encryption**: cᵢ = (mᵢ + kᵢ) mod bᵢ (digitwise modular addition)
- **Decryption**: mᵢ = (cᵢ - kᵢ) mod bᵢ

### Theorem 1: Perfect Secrecy (Buono 2026, Section 3.2)
**Statement**: The MR-OTP with a uniformly random key over K achieves Shannon perfect secrecy.

**Proof Structure** (Bayes' rule):
1. **Conditional**: P[C=c|M=m] = Πᵢ 1/bᵢ — independent of m because each kᵢ is uniform on {0,...,bᵢ-1} and independent
2. **Marginal**: P[C=c] = Σₘ' P[C=c|M=m'] P[M=m'] = Πᵢ 1/bᵢ — also independent of m
3. **Posterior**: P[M=m|C=c] = P[C=c|M=m]P[M=m] / P[C=c] = P[M=m] — perfect secrecy

**Critical Requirements**:
- Key digits kᵢ must be **uniform** over the full set {0, ..., bᵢ-1}
- Key digits must be **independent** across positions
- Any deviation (non-uniformity, dependence, or shortened key) breaks perfect secrecy

### Special Cases (Corollaries 1 & 2)
- **Binary OTP**: bᵢ = 2 for all i → cᵢ = mᵢ ⊕ kᵢ (bitwise XOR)
- **Single-alphabet OTP**: bᵢ = b constant → OTP over alphabet of size b (e.g., b=26 for Latin, b=4 for nucleotides)

### Proposition 2: Secret Bases Cannot Reduce Key Entropy (Section 4)
- H(K) = H(B) + H(k|B) ≥ H(k|B) = Σ log₂ bᵢ ≥ H(M)
- The pad k already carries entropy ≥ H(M); base entropy H(B) is additive overhead
- Perfect secrecy **requires** each kᵢ uniform on full {0,...,bᵢ-1} — shortening k violates this
- Secret bases provide only computational security (search problem), not information-theoretic

---

## 2. Horner's Method for Binary → Mixed-Radix Conversion

### Mixed-Radix Representation as Horner Evaluation (Buono 2026b, Section 2.2)
**Positional weights**: Wᵢ = Π_{j>i} bⱼ, Wₗ = 1  
**Integer value**: V = Σᵢ kᵢ Wᵢ = k₁(b₂b₃...bₗ) + k₂(b₃...bₗ) + ... + kₗ

**Horner's nested form**:
```
V = (((k₁·b₂ + k₂)·b₃ + k₃) ... )·bₗ + kₗ
```

This is exactly **Horner's method** for polynomial evaluation with position-dependent multipliers b₂, b₃, ..., bₗ.

### Inverse Horner Decomposition (Buono 2026b, Section 2.3, Definition 2.2)
**Algorithm** (converts integer V to mixed-radix digits):
```
1. V⁽ᴸ⁾ ← V
2. For i = L downto 1:
     kᵢ ← V⁽ⁱ⁾ mod bᵢ
     V⁽ⁱ⁻¹⁾ ← ⌊V⁽ⁱ⁾ / bᵢ⌋
3. Return (k₁, ..., kₗ)
```

**Proposition 2.3**: Inverse Horner is a bijection between K and {0, ..., P-1} where P = Π bᵢ.

### Uniform Key Sampling (Buono 2026b, Section 3)
**Problem**: QKD produces uniform bits; MR-OTP needs uniform K over Π{0,...,bᵢ-1}.

**Naive approach fails**: Read k = ⌈log₂ P⌉ bits → integer V ∈ {0,...,2ᵏ-1} → V mod P
- **Proposition 3.1**: Modulo bias when P ≠ 2ᵏ breaks uniformity → violates perfect secrecy
- Values 0 to r-1 (where r = 2ᵏ mod P) get probability 2/2ᵏ; others get 1/2ᵏ

**Solution: Rejection Sampling (Algorithm 1)**:
```
1. P ← Π bᵢ; k ← ⌈log₂ P⌉
2. Repeat:
     Read k bits from R → V ∈ {0,...,2ᵏ-1}
   Until V < P
3. Apply inverse Horner decomposition to V → K = (k₁,...,kₗ)
```

**Theorem 3.4**: S(B) terminates almost surely, outputs K uniform on K with independent digits.

**Proposition 3.5**: Expected bit cost ≤ 2k = 2⌈log₂ P⌉ bits per key tuple.

**Practical acceptance rates** (Remark 3.6):
- B = (4)ᴸ (nucleotides): P = 2²ᴸ, k = 2L, acceptance = 100%
- B = (26)⁵ (Latin): P = 11,881,376, k = 24, acceptance ≈ 70.8%
- B = (60) (base-60): P = 60, k = 6, acceptance = 60/64 = 93.75%

---

## 3. Base-60 Efficiency Analysis

### Single-Base 60 (Uniform b=60)
| Metric | Value |
|--------|-------|
| log₂(60) | 5.9069 bits/symbol |
| ⌈log₂(60)⌉ | 6 bits/symbol |
| Binary OTP overhead | 0.0931 bits/symbol |
| **MR-OTP saving** | **1.55%** |

### Mixed-Radix Base-60 (Factorizations of 60)
| Base Sequence | P | log₂(P) | Binary Cost | Overhead | Saving |
|---------------|---|---------|-------------|----------|--------|
| (60) | 60 | 5.9069 | 6 | 0.0931 | 1.55% |
| (6, 10) | 60 | 5.9069 | 3+4=7 | 1.0931 | **15.62%** |
| (5, 12) | 60 | 5.9069 | 3+4=7 | 1.0931 | **15.62%** |
| (3, 4, 5) | 60 | 5.9069 | 2+2+3=7 | 1.0931 | **15.62%** |
| (2, 2, 3, 5) | 60 | 5.9069 | 1+1+2+3=7 | 1.0931 | **15.62%** |

**Key Insight**: Mixed-radix factorization of 60 (e.g., 5×12, 6×10, 3×4×5) yields **15.62% key material savings** vs binary OTP because binary encoding rounds each factor up individually (3→2, 4→2, 5→3, 10→4, 12→4).

### Representational Efficiency (Buono 2026b, Proposition 5.3)
- Binary overhead: Δ(B) = Σᵢ (⌈log₂ bᵢ⌉ - log₂ bᵢ)
- MR-OTP eliminates this overhead, operating at Shannon entropy limit
- For long sessions with key rolling (Section 5.4), savings compound:
  - N=10⁶ messages, L=1000 symbols, b=20 (amino acids) → ~85 MB key material saved

---

## 4. Experiment Design: Base-60 OTP Key Derivation Efficiency

### Objective
Measure and compare the end-to-end key derivation efficiency and throughput of:
- **Pipeline A (Binary OTP)**: QKD → binary key → XOR encryption
- **Pipeline B (Base-60 MR-OTP)**: QKD → Horner + inverse Horner (Algorithm 1) → MR-OTP encryption

### Experimental Parameters
| Parameter | Value |
|-----------|-------|
| Alphabet | Base-60 (sexagesimal) |
| Message length | Variable (100 - 10,000 symbols) |
| Base sequences tested | (60), (6,10), (5,12), (3,4,5), (2,2,3,5) |
| QKD bit rate | Simulated (1 Mbps - 1 Gbps) |
| Trials per config | ≥ 10,000 |

### Metrics to Measure
1. **Key bits consumed per encrypted symbol** (theoretical: 5.9069 vs 6 for single-base; 5.9069 vs 7 for mixed-radix)
2. **Rejection sampling rate** (acceptance probability = P/2ᵏ)
3. **Expected rounds per key tuple** (1/acceptance_prob)
4. **End-to-end latency** (key extraction + encryption)
5. **Throughput** (encrypted symbols/second)
6. **Perfect secrecy verification** (statistical tests on ciphertext uniformity)

### Predicted Results
| Base Sequence | P | k | Acceptance | Expected Rounds | Binary Overhead | MR-OTP Saving |
|---------------|---|---|------------|-----------------|-----------------|---------------|
| (60) | 60 | 6 | 93.75% | 1.067 | 0.0931 bits | 1.55% |
| (6,10) | 60 | 6 | 93.75% | 1.067 | 1.0931 bits | 15.62% |
| (5,12) | 60 | 6 | 93.75% | 1.067 | 1.0931 bits | 15.62% |

### Implementation Notes
- Use **Lemire's method** (Remark 3.7) for faster rejection sampling: multiplication-based, ~1/2 expected divisions vs 1 for standard
- **Batched extraction** (Open Problem 4, Section 9): For long messages, draw single V ∈ {0,...,Pᴺ-1} and cascade inverse Horner → reduces per-symbol overhead
- Verify **ε-security composition** (Open Problem 5, Section 10) for non-ideal QKD sources

### Perfect Secrecy Validation
- Generate ciphertexts with known message distributions
- Run χ² tests on ciphertext digit distributions (should be uniform for each base)
- Verify P[C=c|M=m] = 1/bᵢ for all positions
- Test with biased messages (non-uniform) — MR-OTP must still achieve perfect secrecy

---

## 5. Open Problems Relevant to Base-60 Research

From Buono 2026b, Section 7:

1. **Optimal Base Selection** (Open Problem 1): 
   - For base-60, is (5,12) or (6,10) or (3,4,5) optimal for typical sexagesimal data?
   - Depends on message support structure (product vs non-product)

2. **Dynamic Key Rolling** (Open Problem 2):
   - Can Bₜ₊₁ = f(Cₜ, Bₜ) be secure without full partition?
   - Base-60 adaptive bases could match changing data types per session

3. **Computational Hardness of Base Recovery** (Open Problem 3):
   - Secret bases add computational barrier
   - Base-60 with bₘₐₓ=60, L=1000 → search space (59)¹⁰⁰⁰
   - Average-case hardness analysis needed

4. **Batched Key Extraction** (Open Problem 4):
   - Critical for base-60 efficiency at scale
   - Single rejection step for N symbols instead of N independent steps

5. **ε-Security Composition** (Open Problem 5):
   - Real QKD has ε > 0; quantify degradation for base-60 pipelines

---

## 6. Summary & Conclusions

### MR-OTP is a Rigorous Generalization of OTP
- ✅ Shannon perfect secrecy proven for arbitrary mixed-radix bases
- ✅ Binary OTP and constant-base OTP recovered as special cases
- ✅ Key entropy requirement exactly matches Shannon bound (no overhead)

### Horner's Method is the Canonical Conversion Algorithm
- ✅ Mixed-radix representation = Horner evaluation
- ✅ Inverse Horner = synthetic division (binary → mixed-radix)
- ✅ Rejection sampling (Algorithm 1) achieves bias-free uniform sampling
- ✅ Expected bit cost ≤ 2⌈log₂ P⌉ — within 2 bits of entropy-optimal

### Base-60 Efficiency
- **Single-base 60**: Modest 1.55% saving (60 is close to 2⁶=64)
- **Mixed-radix 60 (5×12, 6×10, 3×4×5)**: **15.62% saving** — significant!
- Mixed-radix factorization exploits binary rounding waste at each factor

### Experimentally Testable
- Algorithm 1 is simple, well-specified, and implementable
- Rejection rate for base-60 is only 6.25% (very practical)
- Mixed-radix base-60 pipelines should show measurable key material savings
- Perfect secrecy is mathematically guaranteed, not just empirical

---

## 7. References

1. **Buono, F.F.G.** (2026). "New Ideas on a New Old Type of Cipher: The Mixed-Radix One-Time Pad." arXiv:2606.16040v1 [cs.CR]
2. **Buono, F.F.G.** (2026). "From Bits to Mixed-Radix Keys: Horner Decomposition, Uniform Sampling, and the Information-Theoretic QKD Interface of the MR-OTP." arXiv:2606.18526v1 [cs.CR]
3. **Buono, F.F.G.** (2012). "A New Type of Cipher." arXiv:1202.2004v3 [cs.CR]
4. **Shannon, C.E.** (1949). "Communication Theory of Secrecy Systems." Bell System Technical Journal, 28(4).
5. **Lemire, D.** (2019). "Fast Random Integer Generation in an Interval." ACM Transactions on Modeling and Computer Simulation.
6. **Draper, S.C. & Saad, W.** (2016). "Entropy-Optimal Discrete Sampling." IEEE Transactions on Information Theory.
7. **Allouche, J.-P. & Shallit, J.** (2003). "Automatic Sequences: Theory, Applications, Generalizations." Cambridge University Press.
8. **Ostrowski, A.** (1922). "Bemerkungen zur Theorie der diophantischen Approximationen." Abh. Math. Sem. Univ. Hamburg.
9. **Rissanen, J.J.** (1976). "Generalized Kraft Inequality and Arithmetic Coding." IBM J. Res. Dev.