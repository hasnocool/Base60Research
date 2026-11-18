# src/base60research/catalog.py
"""Registry of the 45 research directions in the project brief."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Experiment:
    number: int
    name: str
    domain: str
    question: str
    hypothesis: str
    primary_metric: str
    status: str = "planned"

_NAMES = [
("Harmonic fingerprinting","waves","Do signals have stable ratio signatures?"),
("Frequency interference","waves","How do multiple tones create interference?"),
("Phase cancellation","waves","When do phase offsets reinforce or cancel signals?"),
("Beat-frequency mapping","waves","Can envelope frequency be recovered from paired tones?"),
("Resonance mapping","waves","Can resonant modes be estimated from response curves?"),
("Noise structure analysis","waves","Do noise classes differ under spectral tests?"),
("Harmonic drift","waves","How do instantaneous frequency ratios evolve?"),
("Multi-channel synchronization","waves","Are independent sensors phase synchronized?"),
("Cymatic pattern evolution","waves","How do driven modes map to nodal patterns?"),
("Room acoustic geometry","waves","Can room impulse responses reveal modal geometry?"),
("Lunar cycle decomposition","cycles","Can known lunar periods explain phase-locked observations?"),
("Tidal harmonic analysis","cycles","Do tidal constituents explain observed water levels?"),
("Solar activity periodicity","cycles","Are candidate solar cycles robust to surrogate tests?"),
("Weather periodicity","cycles","Are weather periodicities stable out of sample?"),
("Seasonal cycle comparison","cycles","How do annual daylight and temperature cycles align?"),
("Earth rotation analysis","cycles","How do measured length-of-day variations behave?"),
("Astronomical resonance","astronomy","Are orbital period ratios near small integer ratios beyond chance?"),
("Long-cycle decomposition","cycles","Do nested periodic models improve held-out forecasts?"),
("Polygon symmetry","geometry","Which rotational symmetries are invariant under representation?"),
("Circle subdivision","geometry","Which angular partitions minimize approximation error?"),
("Spiral relationships","geometry","How do angular increments relate to radial growth?"),
("Crystal geometry","geometry","Can lattice symmetry be classified consistently?"),
("Geodesic structures","geometry","How do sphere subdivision schemes compare in distortion?"),
("Gear synchronization","mechanics","When do selected teeth and full gear states repeat?"),
("Rotational collisions","mechanics","When do multiple rotations revisit configurations?"),
("Circadian synchronization","biology","How do biological daily rhythms entrain to zeitgebers?"),
("Neural frequency relationships","biology","Are cross-band coupling measures robust to surrogates?"),
("Respiratory rhythm patterns","biology","How do respiratory intervals vary and synchronize?"),
("Plant movement cycles","biology","Are plant movements periodic under changing light?"),
("Cellular oscillation analysis","biology","Can cellular oscillations be detected reproducibly?"),
("Coupled oscillator synchronization","dynamics","How do coupling strength and topology affect phase locking?"),
("Two-dimensional wave interference","waves","Can predicted nodal geometry match numerical wave fields?"),
("Electrical frequency relationships","engineering","Do harmonic features identify electrical operating states?"),
("Fluid dynamics and vortex cycles","fluids","How does vortex shedding scale with flow conditions?"),
("Seismic signal decomposition","geophysics","Can signal components be separated from noise and artifacts?"),
("Radio signal pattern analysis","astronomy","Are transient features robust across instruments?"),
("Musical temperament","music","How do tuning systems distribute interval errors?"),
("Natural branching","biology","Can branching geometry be described with scale-invariant metrics?"),
("Network synchronization","networks","How do graph topology and coupling affect synchronization?"),
("Chaotic systems","dynamics","Do phase-space recurrences survive surrogate controls?"),
("Randomness testing","math","Are residue patterns distinguishable from appropriate nulls?"),
("Waveform compression","information","Do harmonic descriptors reduce bits at fixed error?"),
("Symmetry transitions","geometry","When do parameter changes alter symmetry classes?"),
("Multi-scale signal analysis","signals","Do multi-resolution descriptors improve detection?"),
("Repeating mechanical systems","mechanics","Can modular state models predict configuration recurrence?"),
]
EXPERIMENTS = tuple(Experiment(i,n,d,q,"Pre-register a measurable effect; compare conventional and randomized baselines.","held-out score") for i,(n,d,q) in enumerate(_NAMES,1))

def list_experiments(domain: str | None = None) -> tuple[Experiment, ...]:
    return tuple(e for e in EXPERIMENTS if domain is None or e.domain == domain)

def get_experiment(name: str) -> Experiment:
    key = name.casefold().replace("_","-").replace(" ","-")
    aliases = {"harmonic":1,"gears":24,"oscillator":31,"interference":2,"cymatics":9}
    for e in EXPERIMENTS:
        if e.name.casefold().replace(" ","-") == key or str(e.number) == key:
            return e
    if key in aliases:
        return EXPERIMENTS[aliases[key]-1]
    raise KeyError(f"Unknown experiment: {name}")
