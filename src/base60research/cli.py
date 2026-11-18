# src/base60research/cli.py
"""Command-line entry point for Base60Research."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .catalog import list_experiments
from .experiments import run_core,run_harmonic,run_interference,run_gears,run_oscillator
from .reporting import save_result
from .datasets import load_csv
from .discovery import scan_ratios

RUNNERS={"harmonic":run_harmonic,"interference":run_interference,"gears":run_gears,"oscillator":run_oscillator}

def build_parser():
    parser=argparse.ArgumentParser(prog="base60",description="Comparative base-12/base-60 research laboratory")
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("list",help="list the complete experiment catalog")
    run=sub.add_parser("run",help="run a synthetic experiment")
    run.add_argument("experiment",choices=[*RUNNERS,"all-core"])
    run.add_argument("--output",type=Path,default=Path("artifacts"))
    run.add_argument("--seed",type=int,default=60)
    csv=sub.add_parser("analyze-csv",help="load a local time-series CSV and report its provenance")
    csv.add_argument("path",type=Path); csv.add_argument("--time-column",required=True)
    csv.add_argument("--value-column",required=True); csv.add_argument("--units",default="unspecified")
    ratio=sub.add_parser("scan-ratios",help="scan a supplied comma-separated list of periods")
    ratio.add_argument("periods",help="e.g. 12,18,24,36"); ratio.add_argument("--max-integer",type=int,default=12)
    return parser

def main(argv=None):
    args=build_parser().parse_args(argv)
    if args.command=="list":
        for e in list_experiments(): print(f"{e.number:02d}. [{e.domain}] {e.name} — {e.question}")
        return 0
    if args.command=="run":
        results=run_core(args.seed) if args.experiment=="all-core" else [RUNNERS[args.experiment](args.seed) if args.experiment not in ("gears",) else run_gears()]
        for result in results:
            folder=save_result(result,args.output/result["experiment"])
            print(f"{result['experiment']}: {folder}")
        return 0
    if args.command=="analyze-csv":
        frame,provenance=load_csv(args.path,args.time_column,args.value_column,args.units)
        print(json.dumps({"provenance":provenance,"preview":frame.head(5).to_dict(orient="records")},indent=2,default=str))
        return 0
    if args.command=="scan-ratios":
        periods=[float(x.strip()) for x in args.periods.split(",")]
        print(json.dumps(scan_ratios(periods,args.max_integer),indent=2))
        return 0
    return 2

if __name__=="__main__":
    raise SystemExit(main())
