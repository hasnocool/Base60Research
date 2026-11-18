# src/base60research/discovery.py
"""Exploratory ratio scanner with shuffled controls and FDR correction."""
from __future__ import annotations
import numpy as np
from .analysis import permutation_correlation,benjamini_hochberg

def scan_ratios(periods, max_integer=12, tolerance=.01, permutations=999, seed=60):
    values=np.asarray(periods,dtype=float)
    if values.ndim!=1 or len(values)<3 or np.any(values<=0): raise ValueError("provide >=3 positive periods")
    candidates=[]
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            ratio=max(values[i],values[j])/min(values[i],values[j])
            for numerator in range(1,max_integer+1):
                for denominator in range(1,max_integer+1):
                    target=numerator/denominator
                    error=abs(ratio-target)/target
                    if error<=tolerance:
                        candidates.append({"i":i,"j":j,"ratio":ratio,"candidate":f"{numerator}:{denominator}","relative_error":error})
    # Candidate matching is descriptive. It is not a significance test until a suitable
    # domain-specific null model and independent observations are specified.
    return {"candidates":candidates,"count":len(candidates),
            "caveat":"Dense rational grids create chance matches. Use preregistered null models, FDR and held-out replication."}
