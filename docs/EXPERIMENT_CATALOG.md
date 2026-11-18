# Experiment Catalog

The registry in src/base60research/catalog.py contains all 45 experiments and their research questions. Domain groupings:

| # | Laboratory | Experiments |
|---|---|---|
| 01–10 | Wave and harmonic | Harmonic fingerprinting; interference; phase cancellation; beats; resonance; noise; drift; multi-channel synchronization; cymatic evolution; room acoustics |
| 11–18 | Time and natural cycles | Lunar; tides; solar activity; weather; seasons; Earth rotation; orbital resonance; long-cycle decomposition |
| 19–25 | Geometry and mechanics | Polygon symmetry; circle subdivision; spirals; crystals; geodesics; gear synchronization; rotational recurrence |
| 26–30 | Biology | Circadian; neural bands; respiration; plant movement; cellular oscillation |
| 31–45 | Unified systems | Coupled oscillators; 2-D interference; electrical harmonics; vortices; seismic; radio astronomy; musical temperament; branching; network synchronization; chaos; randomness; waveform compression; symmetry transitions; multiscale analysis; repeating mechanisms |

## Initial executable studies
- **01 Harmonic fingerprinting:** known synthetic harmonic stack with seeded noise; estimate peaks using a standard periodogram. Metric: mean absolute frequency error.
- **02 Frequency interference:** two tones at 440 Hz and 444 Hz; expected beat frequency is 4 Hz. The envelope is shown against the raw signal.
- **24 Gear synchronization:** exact tooth-count recurrence via integer gcd/lcm; 24/36 example yields 72 tooth-contact events for the pair-contact pattern.
- **31 Coupled oscillator synchronization:** deterministic phase-coupled oscillator simulation; continuous Kuramoto order parameter is primary. Sixty-bin phase is only a visualization diagnostic.

## Planned physical/data studies
All observational studies require a domain-specific null model and independent replication. A ratio scan alone is not a significance test. For tides, fit recognized harmonic constituents and compare forecast residuals. For orbital systems, account for selection effects and dynamical stability. For biological recordings, preserve subject-level grouping and avoid causal interpretation.
