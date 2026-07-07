# Lessons Learned / What I'd Validate First

Framed as a postmortem, even though this is a prospective case study rather than a shipped project — because the
discipline of "what would I need to be wrong about, and how would I find out fast" is the same either way.

## What I'm most confident about
- The general shape of the bottleneck (serialized handoffs across DS, actuarial, engineering, legal, and regulators)
  is a well-documented pattern across P&C insurers, not a guess specific to Root.
- Version control, automated validation gates, and feature flagging are proven patterns from software engineering
  that transfer cleanly to a regulated pricing context *without* removing any required review step — the risk of
  this proposal is low precisely because it doesn't ask anyone to skip a control.

## What I'm least confident about, and would validate in week one
- **Whether Rating Plan Manager already does some of this.** It's entirely possible RPM already has versioning or
  validation tooling that I'm proposing to duplicate — the first real task is understanding what exists before
  proposing what's new.
- **Where the actual bottleneck concentrates.** I've assumed actuarial review and regulatory filing are the biggest
  time sinks based on industry norms, but at a growth-stage insurtech the real constraint might be engineering
  capacity, or data pipeline reliability, or something I haven't guessed. This case study is a hypothesis, not a
  finding.
- **State-by-state filing variation.** "File and use" vs. "prior approval" states have very different review
  dynamics, and Root's specific state mix would change how much of the timeline is actually compressible.

## What I'd do differently if I were doing this for real (not as an interview artifact)
- I wouldn't build five components at once. I'd pick the single handoff causing the most measured delay — probably
  by literally interviewing the actuarial and DS teams about where they lose the most time — and ship that one
  improvement first, instrumented, before touching the rest.
- I'd resist the urge to present a full architecture on day one to a team that's been living with the real system for
  years. The value I can add early is asking sharp questions and running small experiments, not arriving with a
  finished blueprint.

## Why I'm sharing this instead of a more conservative case study
I considered doing something safer and more contained. I chose this scope because Root's own JD names this exact
problem as strategic, and because a case study that visibly says "here's where I'm confident, here's where I'm
guessing, here's what I'd check first" is a better demonstration of product judgment than a polished proposal that
implies I already know their systems.
