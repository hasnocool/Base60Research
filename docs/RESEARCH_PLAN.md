# Unified Base-12 / Base-60 Research Plan

## Objective
Test whether base-12, base-60 and related subdivisions improve a defined task in signal analysis, natural-cycle analysis, geometry, mechanics, biology, astronomy, number theory or information processing. The objective is comparative and falsifiable: discover useful relationships where supported, and document null results where not.

## Hypotheses
- H1 (representation): sexagesimal notation expresses more fractions with finite expansions than decimal notation for denominators composed of 2, 3 and 5; this is a number-theoretic property, not a claim of greater physical accuracy.
- H2 (signals): a ratio/phase feature representation may improve interpretability or compactness for selected periodic signals, but should not outperform continuous spectral methods universally.
- H3 (synchronization): integer cycle counts and modular arithmetic exactly predict recurrence in ideal discrete mechanical systems.
- H4 (natural systems): apparent small-integer period ratios occur more often in selected systems than in carefully constructed domain-specific null models. This is exploratory and requires correction for selection effects.
- H5 (geometry): partitions such as 12, 60 and 360 can simplify specific angular tasks when the target geometry shares those symmetries; arbitrary geometry should not benefit systematically.
- H0: after controlling for model complexity, quantization, multiple testing and selection, base choice provides no general predictive advantage.

## Mathematical methodology
Use exact integer arithmetic and fractions for number-theoretic claims; floating-point arrays for physical measurements; continuous phase in radians as the reference; Fourier/periodogram and windowed methods for spectra; circular statistics for phase; gcd/lcm for ideal gear recurrence; rational approximation with bounded numerator/denominator for ratio scans; bootstrap confidence intervals and permutation/surrogate tests for inference.

For a period ratio r, compare against p/q candidates under a predeclared bound and tolerance. Do not scan arbitrary bounds then report only the best-looking ratio. For periodic time series, fit baseline trend + seasonal terms before residual period search. For signals, compare continuous-valued features to binned encodings at matched resolution and equal compute budget.

## Dataset plan
Synthetic ground-truth data first: pure tones, harmonic stacks, mixed tones, noise, chirps, phase-coupled oscillators, known gear tooth counts, geometric lattices and known periodic processes. Observational sources to evaluate later: NOAA/NCEI tide gauges and weather; NASA/JPL Horizons ephemerides; SILSO sunspot series; USGS seismic catalogs/waveforms; PhysioNet physiological data; public radio astronomy archives. Each imported dataset must retain source, retrieval date, license, units, timezone, sampling interval, missingness policy and SHA-256 checksum.

## Experiment design
1. Write a one-page preregistration: hypothesis, primary metric, exclusions, sample size/power rationale, candidate search bounds and stopping rule.
2. Freeze a deterministic seed and software environment.
3. Split data by time/source into discovery and held-out validation sets.
4. Run conventional baseline first, then candidate representations on identical observations.
5. Run null controls: shuffled labels, phase-randomized surrogates, block bootstrap or domain-specific physical null.
6. Correct families of p-values using Benjamini–Hochberg; report all attempted analyses.
7. Repeat on an independent dataset or a second instrument/source.
8. Publish code, config, metrics and negative results.

## Baselines
SI units, decimal notation, radians, continuous phase, standard Fourier/spectral analysis, conventional time-series decomposition, standard geometric algorithms and conventional compression. Compare bases 10, 12, 24, 30, 60 and 360 only when their interpretation is meaningful.

## Statistical controls
Use time-aware splits to avoid leakage; preserve autocorrelation in surrogate controls; account for multiple comparisons; bootstrap at the independent-unit level; predefine exclusions; report effect size and uncertainty; distinguish exploratory from confirmatory results. A visually repeating 60-bin pattern is not a discovery by itself.

## Measurable success criteria
A claimed practical advantage must achieve >=5% relative improvement on a preregistered held-out primary metric, with a 95% confidence interval excluding zero and adjusted p < .05 where applicable, plus independent replication. For compression, compare bits at equal reconstruction error. For interpretability, define a blinded task and score inter-rater agreement or task accuracy. If these thresholds are not met, report no demonstrated advantage.

## Research areas / catalog
See EXPERIMENT_CATALOG.md. The 45 registered studies include harmonics, interference, phase cancellation, beats, resonance, noise, drift, sensor synchronization, cymatics, room acoustics, lunar/tidal/solar/weather/seasonal cycles, Earth rotation, orbital resonance, long-cycle decomposition, symmetry, circle subdivisions, spirals, crystals, geodesics, gears, rotational recurrence, circadian/neural/respiratory/plant/cellular rhythms, coupled oscillators, 2-D waves, electrical harmonics, vortices, seismic signals, radio transients, musical temperament, branching, network synchronization, chaos, randomness, compression and multiscale analysis.

## Base-60 mathematical encryption language (fictional protocol)
The project can define a coherent symbolic language for worldbuilding or simulation:
- Base-12 = structural/spatial coordinates.
- Base-60 = timing, orbital phase and synchronization coordinates.
- Geometry = relational diagrams and transforms.
- Frequency = carrier, modulation, phase and resonance descriptors.
- Primes = identifiers and key-derivation inputs.
- Sacred numbers = fictional authorization tiers and dynastic identifiers.

Keep this protocol separate from scientific inference. If used for actual security, use vetted cryptographic primitives (e.g. modern KDFs and authenticated encryption), not custom number symbolism or prime-based homemade ciphers. The numeral alphabet and mapping must be formally specified, versioned and tested for collisions and canonicalization.
