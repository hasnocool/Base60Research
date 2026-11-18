# src/base60research/signals.py
"""Deterministic synthetic signals with explicit ground truth."""
from __future__ import annotations
import numpy as np
from numpy.typing import NDArray

def harmonic_signal(sample_rate: float = 2048, duration: float = 4, fundamental: float = 64,
                    harmonics=(1,2,3,5), amplitudes=(1,.5,.25,.12), phases=None,
                    noise_std: float = 0, seed: int = 60):
    if sample_rate <= 0 or duration <= 0 or fundamental <= 0:
        raise ValueError("sample_rate, duration and fundamental must be positive")
    if len(harmonics) != len(amplitudes):
        raise ValueError("harmonics and amplitudes must have equal length")
    t = np.arange(int(sample_rate*duration), dtype=float)/sample_rate
    phases = phases or [0.0]*len(harmonics)
    y = sum(a*np.sin(2*np.pi*fundamental*h*t+p) for h,a,p in zip(harmonics,amplitudes,phases))
    if noise_std:
        y += np.random.default_rng(seed).normal(0,noise_std,len(t))
    return t, y

def two_tone_signal(f1=440.0, f2=444.0, sample_rate=4096, duration=3.0, phase1=0.0, phase2=0.0):
    t=np.arange(int(sample_rate*duration))/sample_rate
    return t, np.sin(2*np.pi*f1*t+phase1)+np.sin(2*np.pi*f2*t+phase2)

def coupled_phase_oscillators(count=8, steps=3000, dt=.01, coupling=.8, seed=60):
    rng=np.random.default_rng(seed)
    phases=rng.uniform(-np.pi,np.pi,count)
    history=np.empty((steps,count))
    natural=rng.normal(1.0,.08,count)
    for i in range(steps):
        order=np.mean(np.exp(1j*phases))
        interaction=coupling*np.imag(order*np.exp(-1j*phases))
        phases += dt*(natural+interaction)
        phases=(phases+np.pi)%(2*np.pi)-np.pi
        history[i]=phases
    return np.arange(steps)*dt, history

def phase_order_parameter(phases: NDArray) -> NDArray:
    return np.abs(np.mean(np.exp(1j*phases),axis=-1))
