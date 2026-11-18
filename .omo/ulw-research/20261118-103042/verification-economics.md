| claim | risk | error_cost | verification_cost_time | chosen_verification_path | defer_verify_decision | outcome | residual_risk |
|---|---|---|---|---|---|---|---|
| C-01 (composite scores) | normal | wrong ranking recommendation | ~1 min (pytest coverage + docs read) | pytest + docs verification | verify | confirmed | none |
| C-02 (terminating fractions) | normal | wrong mathematical claim | ~1 min (pytest test_numerals) | pytest + docs verification | verify | confirmed | none |
| C-03 (circle subdivisions) | normal | wrong geometry claim | ~1 min (pytest test_geometry) | pytest + docs verification | verify | confirmed | none |
| C-04 (no float arithmetic) | low | violates Control 2 | ~1 min (grep) | grep verification | verify | confirmed | none |
| C-05 (partition fractions) | normal | wrong mathematical claim | ~1 min (pytest test_fraction) | pytest + docs verification | verify | confirmed | none |
| C-06 (5-smooth FFT faster) | normal | wrong performance claim | ~1 min (pytest test_fft) | pytest + docs verification | verify | confirmed | none |
| C-07 (Delta mod 60 cycle) | normal | wrong claim in literature | ~3 min (verify_delta_mod60.py) | direct computation | verify | refuted | none |
| C-08 (Babylonian tables) | normal | wrong history claim | ~1 min (pytest test_babylonian) | pytest + docs verification | verify | confirmed | none |
| C-09 (5-smooth FFT faster) | normal | wrong performance claim | ~1 min (pytest test_fft) | pytest + docs verification | verify | confirmed | none |
| C-10 (5-smooth FFT prediction) | normal | wrong prediction claim | ~1 min (pytest test_smooth_fft) | pytest + docs verification | verify | confirmed | none |
| C-11 (direct base conversion) | normal | wrong conversion claim | ~1 min (pytest test_numerals) | pytest + docs verification | verify | confirmed | none |
| C-12 (partition fractions) | normal | wrong math claim | ~1 min (pytest test_fraction) | pytest + docs verification | verify | confirmed | none |
| C-13 (Delta mod 60 refuted) | normal | wrong literature claim | ~3 min (verify_delta_mod60.py) | direct computation | verify | refuted | none |