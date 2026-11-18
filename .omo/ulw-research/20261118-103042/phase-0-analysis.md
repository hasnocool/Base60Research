## Phase 0 Analysis — ulw-research Wave (Paper Update + Expansion Research)

**Core question:** What are the complete current findings of the base-12/base-60 research program after implementing experiments 15-26, and what new research directions can expand the experiments and usages in practical ways including digital simulations?

**Axes (5 orthogonal):**
1. **Paper consolidation** — update RESEARCH_PAPER.md with all new findings from experiments 15-26, including the refuted Delta mod 60 claim, Patil direct conversion results, cognitive load rankings, KAM Diophantine conditions, Plimpton 322 reconstruction
2. **Literature search for new experiment directions** — find academic/technical papers on base-12/base-60 applications not yet covered (e.g., cryptography, signal processing beyond FFT, number theory, physics simulations, machine learning representations, quantum computing, quantum simulation)
4. **Codebase audit** — verify all 16 experiment scripts produce consistent output, all finding files have proper frontmatter, no divergences between code and docs
5. **New experiment design** — propose 3-5 additional experiment scripts beyond 15-26 with testable claims

**Codebase relevant:** yes · **External:** yes (literature search) · **Browsing:** no (arxiv/zenodo accessible) · **Verification likely:** yes

**Scale:** 5 axes, 2 source territories (codebase + arxiv/literature), target document: updated RESEARCH_PAPER.md (~20-25 pages)

**Precision demand:** high — wrong mathematical claim costs research credibility → lifecycle: single research team then refinement team

**Format:** Pending user answer at format-proposal gate.

---

## Format-Proposal Gate

**Proposed final materials:**
- **Markdown paper** (`RESEARCH_PAPER.md`) — living document, citeable, version-controlled
- **Standalone HTML** (`RESEARCH_PAPER.html`) — renderable single-file with embedded charts
- **PDF** (`RESEARCH_PAPER.pdf`) — printable/archivable (via pandoc/wkhtmltopdf)

**Proposed template (mirrors PLAN.md + findings conventions):**
1. Abstract
2. Mathematical Foundations (base factorization, termination rule)
3. Current Results (761 tests, 97.92% coverage, 16 experiments)
4. Composite Score Analysis (Base 12 wins, 0.5126)
6. New Experiment Directions (from literature search)
6. Digital Simulations & Practical Applications (NEW SECTION)
7. Reproducibility (all claims backed by code/docs)
8. References

**Citation style:** `[O-01]` observation-manifest IDs + source paths.

**Cost:** Markdown = zero cost; HTML via pandoc (available); PDF via pandoc+pdflatex (available).

---

**Awaiting user answer on format/template before proceeding to Phase 1.**