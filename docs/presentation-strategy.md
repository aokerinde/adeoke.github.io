# Presentation Strategy Across the Interview Loop

This case study is dense on purpose — it's a portfolio artifact, not a single-round script. Here's how much of it to
surface at each stage, and to whom.

## Recruiter screen (Natalie Wynn)
**Don't lead with this.** A recruiter screen is about fit, motivation, and logistics. If it comes up at all, mention
it in one sentence as evidence of genuine interest: *"I actually put together a small case study on Root's
pricing-deployment velocity challenge before this call — happy to walk the hiring manager through it if useful later
in the process."* Then move on. Bringing out architecture diagrams here reads as over-indexing on the wrong signal
for this round.

## Hiring manager round
**This is the primary audience.** Lead with Section 1 (problem framing) and Section 4 (measurable outcomes) — a
hiring manager for this role thinks in roadmap and business-impact terms first. Use the README's top-level sections;
skip the code samples unless asked. Spend the most time on:
- The 14-week-to-5-week timeline compression story (`docs/before-after-timeline.md`)
- The KPI framework in Section 4 — show you'd think about instrumentation and 90-day success metrics, not just
  architecture
- The explicit caveat that this is illustrative, not a claim about Root's real systems — this signals judgment, not
  just enthusiasm

**Close with a question, not a pitch:** *"This is obviously built from public information — I'd want to spend my
first 30 days validating which of these bottlenecks actually match what RPM's users experience today. Does this
match the shape of the problem you're seeing, or is the real constraint somewhere I haven't guessed?"* This turns a
prepared artifact into a genuine conversation instead of a monologue.

## Technical round (if engineering/DS stakeholders are present)
**This is where the code samples earn their place.** Walk through:
- `pipeline/data_quality/validation_gates.py` — show you understand what a real validation gate checks (schema,
  back-test, fairness thresholds) even without deep actuarial modeling background
- `pipeline/ci_cd/.github/workflows/pricing-pipeline.yml` — demonstrates CI/CD literacy, which the JD explicitly asks
  for ("workflow orchestration")
- Be candid where it's true: *"My depth is in BI/data platform integration and AI-enabled workflow automation, not
  actuarial pricing models specifically — this is my best construction of what the pipeline needs to look like from
  the outside; I'd lean hard on your actuarial and DS teams to correct my assumptions fast."*

## Cross-functional panel (if actuarial/legal/state-management stakeholders join)
**Pivot away from code entirely.** Spend time on:
- Section 1's bottleneck table — validate it with them live: *"Does actuarial review typically run 2-6 weeks here, or
  is the real constraint somewhere else?"*
- The "what doesn't change" section at the bottom of `docs/before-after-timeline.md` — this is the single most
  important thing to say to an actuarial or legal stakeholder in the room. It preempts the natural fear that a
  product person is trying to "automate around" their review function.

## General rule across all rounds
Never present this as a finished proposal. Present it as **evidence of how I think about a hard, cross-functional
problem** — and be explicit that the real version of this roadmap gets built with Root's actual teams, not before
day one. Overconfidence about a system you've never seen reads worse than well-framed curiosity.
