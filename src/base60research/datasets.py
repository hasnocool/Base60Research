# src/base60research/datasets.py
"""Local scientific CSV ingestion with explicit units and provenance."""
from __future__ import annotations
from pathlib import Path
import hashlib
import pandas as pd

def load_csv(path: str|Path, time_column: str, value_column: str, units: str="unspecified"):
    source=Path(path).expanduser().resolve()
    if not source.is_file(): raise FileNotFoundError(source)
    frame=pd.read_csv(source)
    missing={time_column,value_column}-set(frame.columns)
    if missing: raise ValueError(f"missing columns: {sorted(missing)}")
    frame=frame[[time_column,value_column]].dropna()
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    provenance={"path":str(source),"sha256":digest,"rows":len(frame),"time_column":time_column,
                "value_column":value_column,"units":units}
    return frame,provenance
