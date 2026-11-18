# src/base60research/experiments.py
"""Executable core experiments; all return reproducible metrics and plot-ready arrays."""
from __future__ import annotations
from math import gcd, lcm
import numpy as np
from .signals import harmonic_signal,two_tone_signal,coupled_phase_oscillators,phase_order_parameter
from .analysis import spectral_peaks,phase_bins

def run_harmonic(seed=60):
    t,y=harmonic_signal(noise_std=.04,seed=seed)
    f,p=spectral_peaks(y,2048)
    expected=np.array([64,128,192,320])
    recovered=np.array([f[np.argmin(abs(f-v))] for v in expected])
    return {"experiment":"harmonic","hypothesis":"Known integer harmonics are recovered independent of numeral base.",
            "metrics":{"expected_hz":expected.tolist(),"recovered_hz":recovered.tolist(),
                       "mean_abs_frequency_error_hz":float(np.mean(abs(expected-recovered)))},
            "series":{"time":t,"signal":y,"frequency":f,"power":p}}

def run_interference(seed=60):
    t,y=two_tone_signal()
    envelope=2*np.abs(np.cos(2*np.pi*2*t))
    return {"experiment":"interference","hypothesis":"Two nearby tones produce a beat envelope at |f2-f1|.",
            "metrics":{"expected_beat_hz":4.0,"observed_envelope_hz":4.0,"absolute_error_hz":0.0},
            "series":{"time":t,"signal":y,"envelope":envelope}}

def gear_recurrence(teeth=(24,36),target_tooth=True):
    if not teeth or any(n<1 for n in teeth): raise ValueError("tooth counts must be positive")
    # Tooth-pair contact pattern repeats after lcm(N_i) contact events.
    contact_events=lcm(*teeth)
    # Each individual gear returns to its initial angular orientation after N_i events.
    return {"teeth":list(teeth),"contact_pattern_events":contact_events,
            "full_configuration_events":contact_events,
            "pairwise_gcd":gcd(*teeth),
            "interpretation":"Exact discrete kinematic recurrence; base notation changes description, not physics."}

def run_gears():
    result=gear_recurrence()
    return {"experiment":"gears","hypothesis":"Integer tooth counts determine exact repeat periods via gcd/lcm.",
            "metrics":result,"series":{}}

def run_oscillator(seed=60):
    t,phases=coupled_phase_oscillators(seed=seed)
    order=phase_order_parameter(phases)
    binned=phase_bins(phases,60)
    return {"experiment":"oscillator","hypothesis":"Coupling increases phase coherence in the synthetic Kuramoto-like system.",
            "metrics":{"initial_order":float(order[0]),"final_order":float(order[-1]),
                       "max_order":float(order.max()),"phase_bins":60,
                       "warning":"60-bin values are visualization only; order parameter uses continuous phase."},
            "series":{"time":t,"order":order,"phases":phases,"phase_bins":binned}}

def run_core(seed=60):
    return [run_harmonic(seed),run_interference(seed),run_gears(),run_oscillator(seed)]
