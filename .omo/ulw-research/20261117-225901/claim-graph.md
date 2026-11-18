# Claim Graph — Base-12 / Base-60 Research

## Verified Claims Digest (allowlist for synthesis)

| claim_id | statement | status | source_domains | observation_groups | counter_search | primary_source | verified_claims |
|----------|-----------|--------|----------------|--------------------|----------------|----------------|-----------------|
| C-01 | Base 12 composite score (0.5126) > Base 10 (0.4417) > Base 60 (0.4340) | supported | base60lab docs/findings | metrics test suite | none needed (exact computation) | metrics-comparison-report.md | yes |
| C-02 | Base 60 terminates 34% of unit fractions vs Base 12 20% vs Base 10 15% | supported | numerals findings | test_numerals.py | none | numerals-base-conversion.md | yes |
| C-03 | Circle subdivisions exact for 12/24/30/36/60/120/180/360 | supported | geometry findings | test_geometry.py | none | geometry-polygon-subdivisions.md | yes |
| C-04 | No floating-point internal arithmetic in any module | supported | grep verification | F5 test | none | source code | yes |
| C-05 | Partition congruences p(5n+4)≡0(5), p(7n+5)≡0(7), p(11n+6)≡0(11) confirmed | supported | verify_partition_congruence.py | execution | none | Ramanujan (classical) | yes |
| C-06 | 5-smooth FFT sizes are 2.7x–4.5x faster than arbitrary sizes | supported | verify_smooth_fft_claim.py | execution | none | Schumacher 2016 arXiv:1608.06928 | yes |
| C-07 | Delta τ(n) mod 60 does NOT follow a 60-cycle | refuted | verify_delta_mod60.py | execution (509/940 mismatches) | Caldin 2026 Zenodo claim refuted | direct computation | yes |

## Unresolved / Refuted Annex

| claim_id | statement | status | reason |
|----------|-----------|--------|--------|
| C-07 | Delta τ(n) mod 60 follows 60-cycle | refuted | 509/940 mismatches in direct computation up to n=1000 |

## Full Claim Nodes

| claim_id | statement | claim_type | risk_tier | scope | intent_ids | supporting_observations | contradicting_observations | independent_obs_groups | convergence_status | counter_search_result | primary_source_backing | dependencies | final_synthesis_location |
|----------|-----------|------------|-----------|-------|------------|------------------------|---------------------------|----------------------|-------------------|----------------------|----------------------|------------|------------------------|
| C-01 | Base 12 best composite score | numeric | normal | metrics | INT-01 | metrics-comparison-report.md exact values | none | 1 (test suite) | supported | n/a (computed) | yes | none | SYNTHESIS.md |
| C-02 | Base 60 best terminating fraction ratio | numeric | normal | numerals | INT-02 | numerals-base-conversion.md | none | 1 (test suite) | supported | n/a (computed) | yes | none | SYNTHESIS.md |
| C-03 | Circle subdivisions exact | numeric | normal | geometry | INT-03 | geometry-polygon-subdivisions.md | none | 1 (test suite) | supported | n/a (computed) | yes | none | SYNTHESIS.md |
| C-04 | No float internal arithmetic | boolean | low | source code | INT-04 | F5 grep verification | none | 1 (grep) | supported | none needed | yes | none | SYNTHESIS.md |
| C-05 | Partition congruences confirmed | numeric | normal | modular forms | INT-05 | verify_partition_congruence.py | none | 1 (execution) | supported | none | Ramanujan classical | none | SYNTHESIS.md |
| C-06 | 5-smooth FFT faster | numeric | normal | FFT benchmarks | INT-05 | verify_smooth_fft_claim.py | none | 1 (execution) | supported | gearshifft literature | Schumacher 2016 | none | SYNTHESIS.md |
| C-07 | Delta mod 60 cycle refuted | numeric | normal | modular forms | INT-05 | verify_delta_mod60.py | Caldin 2026 Zenodo claim | 1 (execution) | refuted | Caldin claim searched, found false | direct computation | none | SYNTHESIS.md |