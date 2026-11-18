| claim | risk | error_cost | verification_cost_time | chosen_verification_path | defer_verify_decision | outcome | residual_risk |
|-------|------|------------|------------------------|-------------------------|----------------------|---------|---------------|
| C-01 (composite scores) | normal | wrong ranking recommendation | ~1 min (pytest coverage + docs read) | pytest + docs verification | verify | confirmed | none |
| C-02 (terminating fractions) | normal | wrong mathematical claim | ~1 min (pytest test_numerals) | pytest + docs verification | verify | confirmed | none |
| C-03 (circle subdivisions) | normal | wrong geometry claim | ~1 min (pytest test_geometry) | pytest + docs verification | verify | confirmed | none |
| C-04 (no float arithmetic) | low | violates Control 2 | ~1 min (grep) | grep verification | verify | confirmed | none |
| C-05 (new research directions) | high | wrong research direction | ~30 min (literature search) | literature search via librarian workers | defer to wave 1 | pending | high — no literature searched yet |
