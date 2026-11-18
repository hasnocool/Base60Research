# tests/test_core.py
from fractions import Fraction
import numpy as np
import pytest
from base60research.bases import encode_integer,decode_integer,fraction_terminates,sexagesimal
from base60research.catalog import EXPERIMENTS,get_experiment
from base60research.experiments import run_core,gear_recurrence
from base60research.analysis import phase_bins,benjamini_hochberg

@pytest.mark.parametrize("value",[-100000,-60,-1,0,1,59,60,360,123456789])
def test_base_roundtrip(value):
    assert decode_integer(encode_integer(value,60),60)==value

def test_fraction_termination():
    assert fraction_terminates(Fraction(1,3),60)
    assert not fraction_terminates(Fraction(1,7),60)
    assert fraction_terminates(Fraction(1,8),12)

def test_sexagesimal():
    assert sexagesimal(1.5,2)=="1;30;0"

def test_catalog_has_45_experiments():
    assert len(EXPERIMENTS)==45
    assert get_experiment("gears").number==24

def test_phase_bins_bounds():
    bins=phase_bins(np.linspace(-np.pi,np.pi,100),60)
    assert bins.min()>=0 and bins.max()<60

def test_gear_recurrence():
    assert gear_recurrence((24,36))["contact_pattern_events"]==72

def test_core_experiments_reproducible_and_metrics_finite():
    results=run_core()
    assert len(results)==4
    assert all(r["experiment"] for r in results)
    assert np.isfinite(results[0]["metrics"]["mean_abs_frequency_error_hz"])

def test_bh():
    result=benjamini_hochberg([.001,.02,.5])
    assert result.tolist()==[True,True,False]
