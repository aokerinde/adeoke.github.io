"""
Automated validation gates for a proposed rating-variable change.

Runs automatically in CI on every pull request that touches a file under
pipeline/feature_definitions/. Replaces what would otherwise be a manual,
multi-day actuarial "does this look right" pass with an automated first
pass that actuarial then reviews on top of -- not a replacement for their
sign-off, a head start on it.

This is illustrative sample code for a portfolio case study, not
production-ready or connected to real data.
"""

from dataclasses import dataclass
import sys
import yaml


@dataclass
class ValidationResult:
    check_name: str
    passed: bool
    detail: str


class PricingFeatureValidator:
    """Runs the standard gate checks against a feature definition + model output."""

    def __init__(self, feature_def_path: str, backtest_df, holdout_df):
        with open(feature_def_path) as f:
            self.feature_def = yaml.safe_load(f)
        self.backtest_df = backtest_df
        self.holdout_df = holdout_df
        self.results: list[ValidationResult] = []

    def run_all(self) -> list[ValidationResult]:
        self.results = [
            self._check_schema_conformance(),
            self._check_minimum_sample_size(),
            self._check_rate_disruption_threshold(),
            self._check_fairness_disparate_impact(),
            self._check_backtest_lift(),
        ]
        return self.results

    def _check_schema_conformance(self) -> ValidationResult:
        required_cols = {"driver_id", "trip_id", "event_type", "event_ts"}
        missing = required_cols - set(self.backtest_df.columns)
        return ValidationResult(
            "schema_conformance",
            passed=not missing,
            detail=f"Missing columns: {missing}" if missing else "OK",
        )

    def _check_minimum_sample_size(self) -> ValidationResult:
        min_trips = self.feature_def["data_sources"]["min_trips_required"]
        under_threshold = (self.backtest_df["trip_count"] < min_trips).mean()
        passed = under_threshold < 0.5  # sanity bound, not a real production rule
        return ValidationResult(
            "minimum_sample_size",
            passed=passed,
            detail=f"{under_threshold:.1%} of drivers below min-trip threshold",
        )

    def _check_rate_disruption_threshold(self) -> ValidationResult:
        threshold = self.feature_def["actuarial_review"]["rate_disruption_threshold_pct"]
        max_observed_swing = self._compute_max_rate_swing()
        passed = max_observed_swing <= threshold
        return ValidationResult(
            "rate_disruption_threshold",
            passed=passed,
            detail=f"Max observed swing {max_observed_swing:.1f}% vs. threshold {threshold}%",
        )

    def _check_fairness_disparate_impact(self) -> ValidationResult:
        # Placeholder: a real implementation would compute disparate impact
        # ratios across protected-class-adjacent proxies per applicable state
        # regulation, flagged for actuarial + legal review, not auto-approved.
        return ValidationResult(
            "fairness_disparate_impact",
            passed=True,
            detail="Placeholder — real check requires actuarial-defined proxy groups",
        )

    def _check_backtest_lift(self) -> ValidationResult:
        # Placeholder: a real implementation compares Gini/lift of the new
        # factor against the incumbent factor on the holdout set.
        return ValidationResult(
            "backtest_lift",
            passed=True,
            detail="Placeholder — compares new vs. incumbent factor lift on holdout",
        )

    def _compute_max_rate_swing(self) -> float:
        # Placeholder calculation for illustration only.
        return 8.5

    def all_passed(self) -> bool:
        return all(r.passed for r in self.results)


def main():
    # In CI, backtest_df / holdout_df would be loaded from the validated
    # data pipeline output, not hardcoded.
    print("Validation gates would run here against real pipeline output.")
    sys.exit(0)


if __name__ == "__main__":
    main()
