# Experiment Design: Base-60 MR-OTP Key Derivation Efficiency

## Objective
Empirically validate the theoretical efficiency gains of Mixed-Radix One-Time Pad (MR-OTP) with base-60 alphabets over classical binary OTP, using Horner's method for bias-free key derivation from QKD entropy sources.

## Theoretical Baseline (from Buono 2026b)

### Pipelines Compared
- **Pipeline A (Binary OTP)**: QKD bits → binary key → XOR encryption
- **Pipeline B (Base-60 MR-OTP)**: QKD bits → Algorithm 1 (rejection sampling + inverse Horner) → MR-OTP encryption

### Expected Efficiency Gains
| Base Sequence | log₂(P) | Binary Cost | MR-OTP Cost | Saving |
|---------------|---------|-------------|-------------|--------|
| (60) | 5.9069 | 6 bits | 5.9069 bits | 1.55% |
| (5, 12) | 5.9069 | 7 bits | 5.9069 bits | 15.62% |
| (6, 10) | 5.9069 | 7 bits | 5.9069 bits | 15.62% |
| (3, 4, 5) | 5.9069 | 7 bits | 5.9069 bits | 15.62% |

### Rejection Sampling Stats
| Base Sequence | P | k=⌈log₂P⌉ | 2ᵏ | Acceptance Rate | Expected Rounds |
|---------------|---|-----------|-----|-----------------|-----------------|
| (60) | 60 | 6 | 64 | 93.75% | 1.067 |
| (5,12) | 60 | 6 | 64 | 93.75% | 1.067 |

## Experimental Setup

### Software Implementation
```
mr_otp/
├── key_extraction/
│   ├── algorithm1_standard.py    # Standard rejection sampling
│   ├── algorithm1_lemire.py      # Lemire's multiplication-based method
│   ├── batched_extraction.py     # Open Problem 4: cascaded inverse Horner
│   └── horner.py                 # Forward/inverse Horner utilities
├── encryption/
│   ├── binary_otp.py
│   └── mr_otp.py
├── qkd_simulator/
│   ├── ideal_source.py           # Perfect uniform bits
│   └── non_ideal_source.py       # ε-close to ideal (Open Problem 5)
├── analysis/
│   ├── efficiency_metrics.py
│   ├── statistical_tests.py      # χ², KS tests for perfect secrecy
│   └── throughput.py
└── experiments/
    ├── run_comparison.py
    └── configs/
        ├── base60_single.yaml
        ├── base60_mixed_5_12.yaml
        ├── base60_mixed_6_10.yaml
        └── base60_mixed_3_4_5.yaml
```

### Parameters
- **Message lengths**: [100, 500, 1000, 5000, 10000] symbols
- **QKD bit rates**: [1 Mbps, 10 Mbps, 100 Mbps, 1 Gbps] (simulated)
- **Trials per configuration**: 10,000+
- **Base sequences**: (60), (5,12), (6,10), (3,4,5), (2,2,3,5)

### Metrics Collected
1. **Key bits consumed per symbol** (theoretical vs empirical)
2. **Rejection count per key tuple**
3. **End-to-end latency** (key extraction + encryption)
4. **Throughput** (symbols/second)
5. **Ciphertext uniformity** (χ² test p-values)
6. **Perfect secrecy verification** (P[C=c|M=m] ≈ 1/bᵢ)

## Experiment Configurations

### Config 1: Single-Base 60 vs Binary OTP
```yaml
base_sequence: [60]
message_length: 1000
qkd_rate_mbps: 100
trials: 10000
```

### Config 2: Mixed-Radix (5,12) vs Binary OTP
```yaml
base_sequence: [5, 12]
message_length: 1000
qkd_rate_mbps: 100
trials: 10000
```

### Config 3: Batched Extraction (Open Problem 4)
```yaml
base_sequence: [5, 12]
message_length: 10000
batch_size: 100
trials: 1000
```

### Config 4: Non-Ideal QKD (Open Problem 5)
```yaml
base_sequence: [5, 12]
message_length: 1000
qkd_rate_mbps: 100
epsilon: [0.0, 0.001, 0.01, 0.1]
trials: 5000
```

## Acceptance Criteria

| Metric | Target |
|--------|--------|
| Key bits/symbol (MR-OTP) | ≤ 5.92 (within 0.2% of theoretical 5.9069) |
| Key bits/symbol (Binary) | = 6.0 (for base-60) or 7.0 (for mixed-radix) |
| Rejection rate | 6.25% ± 0.5% (matches 1 - 60/64) |
| Ciphertext χ² p-value | > 0.01 (uniform distribution) |
| Perfect secrecy test | P[C=c\|M=m] = 1/bᵢ ± 0.001 |
| Throughput speedup | ≥ 1.5% (single-base) or ≥ 14% (mixed-radix) |

## Expected Outcomes

### Hypothesis 1: Mixed-Radix Outperforms Binary OTP
- Mixed-radix base-60 (5×12, 6×10) shows ~15.6% key material reduction
- Single-base 60 shows marginal 1.55% reduction
- Both maintain perfect secrecy (statistically verified)

### Hypothesis 2: Rejection Overhead is Negligible
- Expected 1.067 rounds per key tuple
- Actual overhead < 1% of total latency
- Lemire's method reduces division count by ~50%

### Hypothesis 3: Batched Extraction Reduces Per-Symbol Cost
- Single rejection step for N symbols instead of N independent steps
- Acceptance rate = Pᴺ / 2ᵏᴺ for batched approach
- Theoretical improvement for long messages

## Implementation Checklist

- [ ] Implement Algorithm 1 (standard rejection sampling)
- [ ] Implement Lemire's variant
- [ ] Implement forward/inverse Horner
- [ ] Implement MR-OTP encryption/decryption
- [ ] Implement binary OTP baseline
- [ ] Build QKD simulator (ideal + non-ideal)
- [ ] Statistical test suite for perfect secrecy verification
- [ ] Experiment runner with parameter sweep
- [ ] Results collection and visualization
- [ ] Report generation

## Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Implementation | 1 week | Working pipelines A & B |
| Validation | 3 days | Correctness & secrecy tests |
| Experiment runs | 1 week | 10K+ trials per config |
| Analysis | 3 days | Metrics, plots, statistical tests |
| Report | 2 days | Final experiment report |

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Rejection sampling too slow | Use Lemire's method; implement in C/Rust for speed |
| Non-ideal QKD breaks secrecy | Test ε-security bounds; quantify degradation |
| Statistical tests lack power | Use 100K+ samples; multiple test types |
| Batched extraction complex | Start with sequential; add batched as optimization |

## Relevance to Base-60 Research

This experiment directly tests the practical viability of:
1. **Base-60 alphabets in perfect-secrecy cryptography**
2. **Mixed-radix factorization efficiency** (5×12, 6×10, 3×4×5)
3. **Horner-based key derivation** from binary entropy sources
4. **Key rolling protocols** for long-lived base-60 OTP sessions

Results will inform whether base-60 MR-OTP is a practical alternative to binary OTP for applications requiring sexagesimal data representation (time, angles, coordinates, Babylonian mathematics).