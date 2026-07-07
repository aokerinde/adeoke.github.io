"""
Gradual rollout controller for an approved, filed pricing feature.

Decouples "the code is deployed" from "customers are affected by it" --
which is what makes it safe to deploy a filed rate change ahead of its
full-exposure date, and safe to catch a problem at 1% exposure instead of
100%.

Illustrative sample using an Unleash/LaunchDarkly-style flag API shape.
"""

from dataclasses import dataclass


@dataclass
class RolloutGuardrails:
    max_loss_ratio_delta_pct: float
    max_conversion_delta_pct: float


@dataclass
class RolloutStep:
    exposure_pct: int
    min_observation_hours: int = 48


class PricingFeatureRollout:
    """
    Advances a filed pricing feature through a ramp schedule, automatically
    halting and rolling back if guardrail metrics breach thresholds.
    """

    def __init__(self, feature_id: str, ramp_schedule: list[int], guardrails: RolloutGuardrails):
        self.feature_id = feature_id
        self.ramp_schedule = ramp_schedule
        self.guardrails = guardrails
        self.current_step_index = 0

    def current_exposure_pct(self) -> int:
        return self.ramp_schedule[self.current_step_index]

    def check_guardrails(self, observed_loss_ratio_delta_pct: float,
                          observed_conversion_delta_pct: float) -> bool:
        """Returns True if it's safe to advance to the next ramp step."""
        if observed_loss_ratio_delta_pct > self.guardrails.max_loss_ratio_delta_pct:
            self._rollback("loss ratio guardrail breached")
            return False
        if observed_conversion_delta_pct < self.guardrails.max_conversion_delta_pct:
            self._rollback("conversion guardrail breached")
            return False
        return True

    def advance(self):
        if self.current_step_index < len(self.ramp_schedule) - 1:
            self.current_step_index += 1
            print(f"{self.feature_id}: advanced to {self.current_exposure_pct()}% exposure")
        else:
            print(f"{self.feature_id}: fully rolled out at {self.current_exposure_pct()}%")

    def _rollback(self, reason: str):
        self.current_step_index = 0
        print(f"{self.feature_id}: ROLLED BACK to 0% -- {reason}")


if __name__ == "__main__":
    rollout = PricingFeatureRollout(
        feature_id="hard_braking_frequency_v3",
        ramp_schedule=[1, 10, 25, 100],
        guardrails=RolloutGuardrails(max_loss_ratio_delta_pct=5, max_conversion_delta_pct=-3),
    )
    print(f"Starting exposure: {rollout.current_exposure_pct()}%")
