# Demo Walkthrough Script (10-15 minutes)

Use this as a Loom voiceover outline or a live screen-share script. Timings are approximate.

## 0:00-1:30 — The problem, in one breath
"Root's job posting names its own #1 velocity problem: getting new data and model features into production pricing
faster. I wanted to show how I'd think about that on day one, so I built this case study around what I know of
insurance pricing operations generally — not Root's actual systems, which I haven't seen."

*(Show README Section 1 bottleneck table.)*

"The core bottlenecks aren't mysterious — actuarial review, IT deploy queues, regulatory filing, model validation.
None of those steps should be removed. The opportunity is in how much time gets lost *between* them."

## 1:30-4:00 — Current state: the 14-week baseline
*(Show `docs/before-after-timeline.md` baseline table.)*

"Walk through it stage by stage — notice steps 2 through 5 in particular: a spreadsheet handoff, a re-implementation
by engineering from a written spec, and a staging environment that doesn't match production. None of that is
regulated work. That's coordination tax."

## 4:00-8:00 — The proposed architecture
*(Show the Mermaid diagram in README Section 3, then `diagrams/pipeline-swimlane.mmd`.)*

"Five components, each targeting one specific handoff:"
1. Version-controlled feature definitions — *(open `pipeline/feature_definitions/rating_variable.yaml`)*
2. Automated validation gates — *(open `pipeline/data_quality/validation_gates.py`)*
3. Containerized environments — *(open `pipeline/deployment/Dockerfile`)*
4. Feature-flagged rollout — *(open `pipeline/deployment/feature_flags.py`)*
5. Auto-generated regulatory docs — *(open `pipeline/regulatory_docs/generate_filing_doc.py`)*

"None of these replace actuarial or legal review. They replace the *waiting* between review steps."

## 8:00-11:00 — What actually compresses, and what doesn't
*(Show the "proposed" timeline table and the "what doesn't change" callout.)*

"The regulatory filing window is fixed by the state — I'm not proposing to shortcut that. What compresses is
everything that currently runs sequentially around it: actuarial review becomes a PR review with an
auto-generated impact dashboard instead of a static exhibit; filing prep starts the same day as approval instead of
after a manual write-up; deployment happens on a flag instead of an all-or-nothing release train."

## 11:00-13:00 — Metrics I'd actually propose tracking
*(Show README Section 4.)*

"These aren't commitments — they're the KPI framework I'd bring into a roadmap conversation in the first 90 days:
cycle time, deployment frequency, rollback rate, time-to-rate-new-segment."

## 13:00-15:00 — The honest caveat, and the actual ask
"I want to be upfront: I don't have visibility into Rating Plan Manager's real architecture or Root's actual
bottlenecks. This case study is meant to show how I approach a cross-functional, regulated systems problem — not a
finished proposal. If this role moves forward, the first thing I'd want to do is sit with actuarial, DS, and
engineering and find out which of these guesses are right and which aren't."
