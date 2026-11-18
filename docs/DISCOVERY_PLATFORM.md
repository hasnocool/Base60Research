# Cross-Disciplinary Discovery Platform

## Purpose

Evolve Base60Research from a set of isolated experiments into a reproducible platform for investigating relationships across scientific domains. The platform must be as good at rejecting attractive patterns as it is at finding candidates.

The central question is not "does this look like base-60?" It is:

> Does a proposed relationship carry reproducible information that survives representation changes, conventional explanations, appropriate null models, independent datasets and held-out validation?

Base-12 and base-60 are analytical representations to test, not privileged assumptions about nature.

## AI is advisory; evidence adjudication is deterministic

AI may propose hypotheses, suggest datasets, draft analysis code and explain outputs. It must never decide whether a discovery has occurred or assign or upgrade an evidence classification. A separate deterministic Evidence Adjudication Engine applies versioned, inspectable rules to structured statistical evidence. Missing evidence cannot count as a pass, and human overrides must be separately attributed and audited.

See [AI Research Governance and Evidence Adjudication](AI_RESEARCH_GOVERNANCE.md) for responsibilities, evidence contracts, decision gates, integrity boundaries and acceptance tests.

## Required finding classifications

Every candidate relationship receives one of four explicit outcomes. These are evidence labels, not claims about ultimate truth.

1. **Representation-induced / encoding artifact** — the pattern appears because values were rounded, binned, wrapped, rescaled, selected, or displayed in a base-12/base-60 coordinate system. It disappears under continuous analysis or reasonable alternative representations.
2. **Explained by established mathematics or science** — the relationship is real or reproducible, but a known mechanism/model (for example, harmonics, aliasing, resonance, common periodic forcing, dimensional constraints, or sampling theory) adequately explains it. This is a useful result, not a novel discovery.
3. **Unresolved candidate** — the relationship survives initial controls but lacks sufficient independent replication, causal identification, or a decisive comparison against established models. It must not be advertised as a discovery.
4. **Robust cross-domain candidate** — a preregistered effect survives the full validation protocol, improves on relevant conventional baselines, replicates in independent data, and has a plausible domain-specific interpretation. This label still means "candidate for further investigation", not "new law of nature".

A fifth terminal state, **not supported**, should be available when a hypothesis fails its preregistered test or is not distinguishable from its null model.

## Platform workflow

1. **Question and preregistration**
   - State the hypothesis in operational, falsifiable terms.
   - Identify domains, variables, expected direction/shape, primary outcome, minimum meaningful effect and exclusion rules.
   - Record the analysis plan and version before inspecting held-out outcomes.
2. **Data and provenance**
   - Register each dataset with source, license/terms, retrieval time, checksum, units, sampling rate, timezone, missingness, calibration and transformation history.
   - Distinguish synthetic data with known ground truth from observational measurements.
   - Keep train/validation/test splits grouped by time, instrument, subject, location or source to prevent leakage.
3. **Harmonization**
   - Convert units and timestamps explicitly; retain original values.
   - Record resampling, interpolation, filtering, detrending and normalization.
   - Check whether the apparent relationship can be induced by shared trends, common periodic forcing, sampling cadence, selection effects or measurement artifacts.
4. **Representation tournament**
   - Compare the native/continuous representation and conventional scientific units with relevant encodings: base-10, base-12, base-24, base-30, base-60 and base-360.
   - Compare equal-resolution binning and equal-complexity models. Do not compare a high-capacity model with a coarse encoding and attribute differences to the base.
   - Use radians and continuous phase for angular/signal analyses as primary controls; sexagesimal notation may be an alternate coordinate system.
   - Treat base choice as a model/feature-selection decision subject to the same validation rules as any other hyperparameter.
5. **Conventional explanation challenge**
   - Fit or evaluate accepted domain-specific models before proposing a new interpretation.
   - Include relevant null hypotheses: independent processes, shared driver, harmonics, aliasing, chance alignment, common trend, sampling-window effects and known conservation/kinematic constraints.
   - Record which known model explains the observation and what residual, if any, remains.
6. **Nulls and statistical controls**
   - Use domain-appropriate permutation tests, block shuffles, phase-randomized surrogates, circular shifts, synthetic null simulations and negative controls.
   - Preserve autocorrelation and seasonality when generating time-series nulls; naive row shuffling is generally insufficient.
   - Correct for the full family of tested hypotheses and feature/lag/ratio scans (e.g. Benjamini-Hochberg FDR where appropriate).
   - Report effect sizes, uncertainty intervals, sample sizes, power limitations and sensitivity analyses, not only p-values.
7. **Out-of-sample validation and replication**
   - Freeze the pipeline before opening held-out data.
   - Validate across a second dataset, instrument, epoch or independent source.
   - Require the result to survive reasonable preprocessing and representation choices.
   - Separate exploratory discovery from confirmatory testing.
8. **Evidence report**
   - Produce a human-readable report and machine-readable record with inputs, provenance, code/config versions, random seeds, baseline results, null distributions, multiple-testing correction, effect sizes, uncertainty, diagnostics, known explanations and classification.
   - Preserve failed experiments and negative results.

## Cross-disciplinary research graph

Represent a study as a graph rather than a flat list of experiment names.

- **Domain**: acoustics, astronomy, geophysics, climate, biology, mechanics, mathematics, information theory, etc.
- **Dataset**: source and provenance record.
- **Signal/quantity**: measured variable, units, sampling and uncertainty.
- **Transformation**: filtering, normalization, phase extraction, spectral transform, geometric projection, base encoding.
- **Hypothesis**: proposed relationship and preregistered prediction.
- **Model**: conventional baseline, candidate model and null models.
- **Test**: statistic, validation split, correction family and test implementation.
- **Finding**: result classification, effect size, uncertainty and limitations.
- **Replication**: independent data and outcome.

Cross-domain edges must have an explicit mathematical mapping (for example, dimensionless frequency ratio, phase-locking statistic, normalized period ratio, scaling exponent or information measure). Similar-looking numbers from different units are not a relationship. Dimensional analysis and uncertainty propagation are mandatory before comparing physical quantities.

## Comparison framework

The platform should not assume one universal score. Each experiment declares a primary metric appropriate to its scientific task, such as held-out prediction error, likelihood, compression rate at fixed distortion, phase-estimation error, synchronization prediction, or interpretability on a defined task.

For each representation/model, report:
- primary metric and direction of improvement;
- held-out score and uncertainty interval;
- complexity/cost (parameters, runtime, memory or description length);
- calibration and residual diagnostics;
- sensitivity to bin count, base, units, precision and preprocessing;
- performance against conventional and null models.

A representation advantage is only meaningful when comparisons use equivalent information, data splits, tuning budgets and error tolerances. A 60-bin representation must not be credited for a result that follows from choosing 60 bins after inspecting the data.

## Discovery safeguards

- Never search thousands of ratios, lags, windows or encodings and report only the best match without accounting for the search.
- Never treat a visually striking overlay as statistical evidence.
- Never infer causation from correlation or shared periodicity alone.
- Never interpret numerical proximity across incompatible units as a physical connection.
- Do not use "sacred numbers", prime labels or symbolic protocol identifiers as explanatory variables unless operationalized in a falsifiable hypothesis.
- Keep synthetic demonstrations clearly separate from real-world findings.
- Make the null model and known scientific explanation visible beside every candidate result.
- A failed replication downgrades the finding and remains in the audit trail.

## Suggested software architecture

Keep the existing package and CLI stable while adding modules incrementally:

```text
src/base60research/
  hypotheses.py       preregistration and hypothesis schemas
  provenance.py       immutable dataset/run provenance
  harmonize.py        units, time axes, missingness and transformations
  representations.py  base/precision/binning comparison policies
  baselines.py        conventional domain model registry
  null_models.py      block, phase, circular-shift and synthetic nulls
  validation.py       grouped splits, rolling-origin and replication
  statistics.py       effect sizes, uncertainty and multiplicity control
  discovery_graph.py  cross-domain relationships and evidence graph
  evidence.py         structured statistical evidence and gate schemas
  adjudication.py     deterministic classification; no AI dependency
  policy.py           versioned domain-specific evidence gates
  audit.py             immutable decision traces and evidence digests
  reports.py           auditable reports and comparison tables
```

The first implementation should be a small, composable pipeline rather than a large autonomous "AI discovers laws" system. Domain experts must be able to inspect every transformation and override an inappropriate generic test.

## Phased implementation

### Phase 1 — Trustworthy experiment records
- Define typed schemas for hypotheses, datasets, transformations, baselines, nulls, metrics and findings.
- Store run manifests and checksums.
- Add explicit exploratory vs confirmatory run modes.
- Add a report that always shows baseline and null comparisons.

### Phase 2 — Representation tournament
- Run the same pipeline against continuous/native, decimal, base-12, base-24, base-30, base-60 and base-360 representations when mathematically appropriate.
- Add equal-resolution and equal-complexity controls.
- Sweep precision and bin counts to expose encoding artifacts.
- Add unit tests with synthetic cases where base-60 is known to create an apparent pattern.

### Phase 3 — Explanation and null-model engine
- Add autocorrelation-preserving surrogates, phase randomization and circular-shift controls.
- Add common-trend/common-driver and aliasing diagnostics.
- Register established domain baselines; do not let an unexplained residual automatically imply new physics.

### Phase 4 — Cross-domain graph
- Link datasets and signals through dimensionless, uncertainty-aware transformations.
- Search for preregistered relationship classes across domain pairs.
- Track the complete hypothesis search family and correct for multiplicity.
- Build an explorable graph of candidate links and their evidence status.

### Phase 5 — Independent replication and interface
- Re-run frozen studies on independent sources.
- Add dashboard views for datasets, hypotheses, representation tournaments, null distributions and evidence trails.
- Export complete reproducibility bundles.

## Initial acceptance tests

1. **Encoding artifact test:** construct a continuous dataset with no 60-fold structure, then show that post-hoc 60-bin selection can create an apparent alignment; the platform must classify it as representation-induced.
2. **Known explanation test:** generate a two-tone signal with a beat envelope; the platform must recover the beat and identify ordinary interference as the explanation rather than a novel base-60 effect.
3. **Null calibration test:** under simulated null data, the false-positive rate should be consistent with the declared test level within Monte Carlo uncertainty, including after the complete search procedure.
4. **Multiplicity test:** when scanning many ratios/lags, corrected results must not promote chance matches as robust findings.
5. **Representation invariance test:** a physical relationship expressed in different units or valid coordinate systems should retain its underlying dimensionless result within numerical tolerance.
6. **Replication test:** a candidate that exists only in the discovery dataset must be downgraded when it fails independent replication.
7. **Known-baseline test:** when a conventional model explains the data as well as the candidate representation, the finding must be labelled explained by established mathematics/science, not a Base-60 discovery.
8. **AI boundary test:** an AI-supplied label or confidence score cannot change the adjudicator's decision; missing evidence cannot satisfy a gate.

## Definition of scientific value

Base60Research succeeds when it can reliably distinguish:
- a useful alternate notation or computational representation;
- a pattern created by encoding, sampling or analysis choices;
- an established phenomenon rediscovered in a new visualization;
- an unresolved but reproducible empirical relationship;
- and a genuinely promising cross-domain candidate that merits independent scientific work.

The goal is not to prove that base-60 is special. The goal is to make it possible to test that claim rigorously—and to report honestly when the evidence says it is not.
