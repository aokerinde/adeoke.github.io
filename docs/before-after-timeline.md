# Before / After: Feature-to-Production Timeline

All figures are illustrative industry-pattern estimates for this case study, not real Root data.

## Baseline: ~14 weeks, serialized

| Stage | Owner | Duration | What's actually happening | Why it's slow |
|---|---|---|---|---|
| 1. Model/feature finalized | Data Science | 2 weeks | Offline notebook development and backtesting | Not a bottleneck itself, but output isn't yet a shareable artifact |
| 2. Handoff to actuarial | DS → Actuarial | 1 week | Exhibit/spreadsheet prepared and sent | Manual translation step; context loss |
| 3. Actuarial review | Actuarial | 4 weeks | Rate impact analysis, disruption checks, clarifying questions sent back to DS | Round-trip clarification cycles, no shared source of truth |
| 4. Re-implementation | Engineering | 1 week | Engineering rebuilds the model/feature from actuarial's final written spec | Re-derivation risk: engineering's version can drift from what was actually approved |
| 5. QA/UAT | Engineering + QA | 1 week | Testing in a staging environment | Staging data often stale vs. production, causing false negatives/positives |
| 6. Legal/compliance review | Legal | 0.5 week | Consumer disclosure language review | Usually fast once it starts — the problem is it starts late, sequentially |
| 7. Regulatory filing | Legal + Actuarial | 3.5-12+ weeks | SERFF filing prepared, submitted, DOI review | Filing lead time is fixed by regulator, but *filing prep* often waits for step 6 to fully finish first |
| 8. Deployment | Engineering | 1 week | Queued into the next scheduled release train, deployed to 100% of traffic | Binary rollout — no staged exposure, higher rollback cost if something's wrong |

**Total: ~14 weeks**, of which maybe 3-4 weeks is unavoidable regulatory review — the rest is coordination tax.

## Proposed: ~4-6 weeks, parallelized

| Stage | Owner | Duration | What changed |
|---|---|---|---|
| 1. Feature/model committed as versioned artifact | Data Science | 2 weeks (unchanged) | Same modeling work, but output is a diffable, reviewable artifact from day one |
| 2. Automated validation gates | CI | Minutes | Data quality, back-test, fairness checks run automatically on every commit |
| 3. Actuarial review as PR review | Actuarial | 1-2 weeks | Reviewing a structured diff + auto-generated impact dashboard, not a static exhibit; comments happen inline, no re-derivation needed downstream |
| 4. Auto-generated filing exhibit | Legal + Actuarial | Same day as approval | Filing draft populates from the same approved, versioned data — legal review starts immediately instead of waiting for a manual write-up |
| 5. Filing submitted + shadow deployment | Legal / Engineering | Runs in parallel | Regulatory review clock and shadow-mode validation happen concurrently, not sequentially |
| 6. Feature-flagged rollout | Engineering | 1 week ramp | 1% → 10% → 100% with automated guardrails, rather than a single all-or-nothing release |

**Total: ~4-6 weeks** (dominated by whatever the state's actual regulatory review window is — the goal is removing
everything *except* that fixed constraint from the critical path).

## What doesn't change (intentionally)

- Actuarial still reviews and approves every rate impact.
- Legal/compliance still reviews every consumer-facing disclosure.
- The regulator's filing review window is untouched — we can't and shouldn't compress that.
- Nothing here proposes shipping a pricing change without sign-off; it proposes not losing weeks *waiting* for a
  sign-off that's ready to happen sooner.
