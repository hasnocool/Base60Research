# Base60Research

A reproducible research laboratory for testing whether sexagesimal (base-60), duodecimal (base-12), and related representations improve the description, analysis, visualization, or prediction of real mathematical and scientific systems.

> **Scientific rule:** a base is a representation, not a new physical law. Every proposed advantage must beat appropriate decimal/radian/standard-method baselines on held-out data. A 60-bin display must never be mistaken for evidence of a natural 60-fold structure.

## Research scope

The experiment registry spans 45 research directions across:

1. Sound, vibration, harmonics, phase, interference, resonance, noise, acoustics and cymatics.
2. Time, astronomy, tides, solar activity, weather, seasons, Earth rotation and orbital resonance.
3. Geometry, 12/24/30/60/120/360 subdivisions, spirals, crystals, geodesics, gears and rotational synchronization.
4. Biological rhythms and oscillations (using public, ethically sourced datasets; no causal claims from correlation).
5. Number theory, rational approximation, numerical precision, modular arithmetic, primes, fractals, cellular automata, compression and algorithm performance.
6. Coupled oscillators, 2-D waves, electrical signals, fluid/vortex data, seismic signals, radio astronomy, music, branching, networks, chaos and randomness.

## Quick start

Python 3.12 is supported.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
base60 list
base60 run harmonic --output artifacts/harmonic
base60 run gears --output artifacts/gears
base60 run oscillator --output artifacts/oscillator
base60 run all-core --output artifacts/core
pytest
```

No network access or external dataset is required for the synthetic starter experiments. Real data can be loaded from local CSV files using `base60 analyze-csv PATH --time-column ... --value-column ...`.

## Representation language

- **Base-12:** structural/spatial grouping and factor-rich subdivisions.
- **Base-60:** time, phase and synchronization notation; a minute/second-like coordinate system.
- **Geometry:** maps relationships to angular, radial, lattice or network structures.
- **Frequency:** signals are represented by frequency, phase, amplitude and coherence features.
- **Primes:** deterministic identifiers and optional key derivation for fictional protocols—not evidence of physical meaning.
- **Sacred numbers:** optional fictional authorization/dynastic metadata only. They are not scientific variables unless an independently testable operational definition exists.

Sexagesimal formatting is exact for integer quantities and rational fractions whose reduced denominator divides a power of 60. For other values, the library reports precision and residual rather than implying exactness.

## Architecture

```text
src/base60research/
  bases.py          base conversion and angle/time formatting
  catalog.py        45-experiment registry and metadata
  signals.py        deterministic synthetic signal generation
  analysis.py       spectral, phase, harmonic and statistics utilities
  experiments.py    executable reference experiments
  datasets.py       CSV ingestion and dataset provenance
  discovery.py      candidate ratio search with permutation controls
  reporting.py      machine-readable JSON + plots + summary
  cli.py            command-line interface
```

## Experimental protocol

1. Register a hypothesis and its primary metric before running the analysis.
2. Generate synthetic data with known ground truth or record dataset provenance and license.
3. Apply identical preprocessing and train/test partitions to all representations.
4. Compare standard continuous methods with base-12, base-24, base-30, base-60 and base-360 encodings where meaningful.
5. Include shuffled/permuted nulls, multiple-comparison correction, confidence intervals and held-out validation.
6. Report negative results and effect sizes, not just visually compelling plots.
7. Treat any discovered pattern as exploratory until independently replicated.

## Baselines and controls

- Conventional SI units, decimal arithmetic and radians.
- Continuous-valued phase/spectral analysis (never only 60-bin quantization).
- Equal-complexity representation controls (12, 24, 30, 60, 360 bins as appropriate).
- Randomized phase, shuffled time series and surrogate/noise controls.
- Train/test separation by time or source; no tuning on the test set.
- Benjamini–Hochberg false-discovery-rate correction for candidate scans.
- Deterministic random seeds and recorded configuration/environment.

## Success criteria

A base-60 method is considered useful only if it demonstrates at least one preregistered, repeatable advantage: (a) lower held-out prediction error, (b) shorter exact/near-exact representation at a fixed error tolerance, (c) improved interpretability measured by a defined task, or (d) lower compute cost at equivalent accuracy. As a practical threshold, target >=5% relative improvement on the primary metric with a 95% bootstrap confidence interval excluding zero, corrected p < 0.05 where hypothesis testing applies, and replication on a second dataset. Otherwise report no demonstrated advantage.

## Dataset strategy

Start with deterministic synthetic datasets. For observational research, use documented public sources such as NOAA/NCEI tides and weather, NASA/JPL Horizons orbital ephemerides, SILSO sunspot numbers, USGS earthquake catalogs/waveforms, PhysioNet physiological time series, and public radio-astronomy archives. Dataset adapters should store source URL, retrieval date, license/terms, units, timezone, missing-value policy and checksum. Do not silently download or redistribute data.

## Outputs

Each run writes `summary.json`, `metrics.json`, `experiment_config.json`, and PNG figures into its output directory. Raw source data is not modified. Results include the random seed, package version, hypothesis, baseline, controls, metrics and caveats.

## Roadmap

- [x] Shared base conversion and sexagesimal notation.
- [x] Experiment registry covering the 45 proposed investigations.
- [x] Synthetic harmonic, interference, gear synchronization and coupled-oscillator experiments.
- [x] Reproducible plots, JSON reports, CSV analysis and discovery scan.
- [x] Cross-disciplinary discovery platform architecture and evidence classifications.
- [ ] Typed hypothesis/dataset/evidence schemas and reproducible run manifests.
- [ ] Representation tournament and conventional-explanation/null-model engine.
- [ ] Cross-domain evidence graph and independent replication packs.
- [ ] Domain-specific real-data adapters.
- [ ] Interactive dashboard and experiment builder.
- [ ] Physical lab acquisition adapters (audio interface, accelerometer, electrical measurements) with calibration metadata.

See [the full research plan](docs/RESEARCH_PLAN.md), [45-experiment catalog](docs/EXPERIMENT_CATALOG.md), and [cross-disciplinary discovery platform design](docs/DISCOVERY_PLATFORM.md).
