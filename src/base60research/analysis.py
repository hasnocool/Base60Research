# src/base60research/analysis.py
"""Signal analysis, representation comparisons and statistical controls."""
from __future__ import annotations
import numpy as np
from scipy.signal import periodogram, find_peaks

def spectral_peaks(signal, sample_rate: float, prominence: float | None = None):
    frequencies, power=periodogram(np.asarray(signal),fs=sample_rate,scaling="spectrum")
    peaks,_=find_peaks(power,prominence=prominence)
    order=peaks[np.argsort(power[peaks])[::-1]]
    return frequencies[order],power[order]

def phase_bins(phase, bins: int):
    """Diagnostic quantization only; continuous phase must remain the baseline."""
    if bins < 2: raise ValueError("bins must be >= 2")
    wrapped=(np.asarray(phase)%(2*np.pi))/(2*np.pi)
    return np.floor(wrapped*bins).astype(int)

def circular_phase_error(a,b):
    delta=np.angle(np.exp(1j*(np.asarray(a)-np.asarray(b))))
    return np.abs(delta)

def benjamini_hochberg(p_values, alpha=.05):
    p=np.asarray(p_values,dtype=float)
    if np.any((p<0)|(p>1)): raise ValueError("p-values must be in [0,1]")
    order=np.argsort(p); ranked=p[order]
    thresholds=alpha*np.arange(1,len(p)+1)/max(1,len(p))
    passed=ranked<=thresholds
    reject=np.zeros(len(p),dtype=bool)
    if passed.any(): reject[order[:np.where(passed)[0].max()+1]]=True
    return reject

def permutation_correlation(x,y,iterations=999,seed=60):
    x,y=np.asarray(x),np.asarray(y)
    if x.shape != y.shape or x.ndim != 1: raise ValueError("x and y must be same-length vectors")
    observed=float(np.corrcoef(x,y)[0,1])
    rng=np.random.default_rng(seed)
    null=np.empty(iterations)
    for i in range(iterations): null[i]=np.corrcoef(x,rng.permutation(y))[0,1]
    p=(1+np.count_nonzero(np.abs(null)>=abs(observed)))/(iterations+1)
    return observed,float(p),null

def bootstrap_mean_ci(values,iterations=2000,confidence=.95,seed=60):
    values=np.asarray(values,dtype=float)
    if values.size==0: raise ValueError("values cannot be empty")
    rng=np.random.default_rng(seed)
    means=np.mean(rng.choice(values,(iterations,len(values)),replace=True),axis=1)
    tail=(1-confidence)/2
    return float(values.mean()),tuple(map(float,np.quantile(means,[tail,1-tail])))
