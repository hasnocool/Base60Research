# src/base60research/reporting.py
"""Persist reproducible JSON summaries and publication-friendly figures."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _jsonable(value):
    if isinstance(value,np.ndarray): return value.tolist()
    if isinstance(value,(np.integer,np.floating)): return value.item()
    if isinstance(value,dict): return {str(k):_jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [_jsonable(v) for v in value]
    return value

def save_result(result: dict, output: str|Path):
    folder=Path(output); folder.mkdir(parents=True,exist_ok=True)
    metrics={"experiment":result["experiment"],"hypothesis":result["hypothesis"],"metrics":_jsonable(result["metrics"])}
    (folder/"metrics.json").write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    (folder/"summary.json").write_text(json.dumps({"status":"exploratory","result":metrics,
        "scientific_note":"A representation is not evidence of a physical mechanism. Confirm on real held-out data."},indent=2),encoding="utf-8")
    series=result.get("series",{})
    if "time" in series and "signal" in series:
        fig,ax=plt.subplots(figsize=(10,4)); ax.plot(series["time"],series["signal"],lw=.7)
        ax.set(xlabel="Time (s)",ylabel="Amplitude",title=result["experiment"].title())
        fig.tight_layout(); fig.savefig(folder/"signal.png",dpi=140); plt.close(fig)
    if "frequency" in series and "power" in series:
        fig,ax=plt.subplots(figsize=(10,4)); ax.plot(series["frequency"],series["power"])
        ax.set(xlim=(0,500),xlabel="Frequency (Hz)",ylabel="Power",title="Power spectrum")
        fig.tight_layout(); fig.savefig(folder/"spectrum.png",dpi=140); plt.close(fig)
    if "time" in series and "order" in series:
        fig,ax=plt.subplots(figsize=(10,4)); ax.plot(series["time"],series["order"])
        ax.set(ylim=(0,1),xlabel="Time (s)",ylabel="Phase order parameter",title="Coupled oscillator synchronization")
        fig.tight_layout(); fig.savefig(folder/"synchronization.png",dpi=140); plt.close(fig)
    (folder/"experiment_config.json").write_text(json.dumps({"seed":60,"sampling":"deterministic synthetic defaults"},indent=2),encoding="utf-8")
    return folder
