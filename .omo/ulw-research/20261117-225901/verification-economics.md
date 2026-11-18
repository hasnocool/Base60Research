| claim | risk | error_cost | verification_cost_time | chosen_verification_path | defer_verify_decision | outcome | residual_risk |
|-------|------|------------|------------------------|-------------------------|----------------------|---------|---------------|
| C-01 (composite scores) | normal | wrong ranking recommendation | ~1 min (pytest coverage + docs read) | pytest + docs verification | verify | confirmed | none |
| C-02 (terminating fractions) | normal | wrong mathematical claim | ~1 min (pytest test_numerals) | pytest + docs verification | verify | confirmed | none |
| C-03 (circle subdivisions) | normal | wrong geometry claim | ~1 min (pytest test_geometry) | pytest + docs verification | verify | confirmed | none |
| C-04 (no float arithmetic) | low | violates Control 2 | ~1 min (grep) | grep verification | verify | confirmed | none |
| C-05 (partition congruences) | normal | wrong mathematical claim | ~1 min (pytest test_partition) | pytest + docs verification | verify | confirmed | none |
| C-06 (5-smooth FFT faster) | normal | wrong performance claim | ~2 min (pytest + manual run) | verify_smooth_fft_claim.py | verify | confirmed | none |
| C-07 (Delta mod 60 cycle) | normal | wrong claim in literature | ~3 min (compute up to n=1000) | verify_delta_mod60.py | verify | refuted | none |