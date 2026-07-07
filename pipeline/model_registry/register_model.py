"""
Registers an approved rating model/feature version in the model registry,
transitioning it through lifecycle stages that mirror the actuarial and
regulatory approval workflow.

Illustrative sample for a portfolio case study -- uses MLflow's API shape
but is not wired to a live tracking server.
"""

import mlflow
from mlflow.tracking import MlflowClient


PRICING_MODEL_NAME = "root-pricing-hard-braking-frequency"


def register_new_version(model_uri: str, feature_def: dict) -> str:
    """
    Registers a new model version and tags it with the metadata actuarial
    and legal need for review -- so the registry, not a side document, is
    the audit trail.
    """
    client = MlflowClient()

    result = mlflow.register_model(model_uri=model_uri, name=PRICING_MODEL_NAME)

    client.set_model_version_tag(
        PRICING_MODEL_NAME, result.version, "feature_id", feature_def["feature"]["id"]
    )
    client.set_model_version_tag(
        PRICING_MODEL_NAME, result.version, "status", "pending_actuarial_review"
    )
    client.set_model_version_tag(
        PRICING_MODEL_NAME,
        result.version,
        "rate_disruption_threshold_pct",
        str(feature_def["actuarial_review"]["rate_disruption_threshold_pct"]),
    )

    return result.version


def transition_stage(version: str, stage: str, approver: str):
    """
    Moves a model version through its approval lifecycle. Every transition
    is logged with an approver, giving a complete, queryable audit trail --
    replacing an email thread as the record of "who approved what, when."

    Valid stages (case-specific, not MLflow defaults):
      pending_actuarial_review -> actuarial_approved -> filed -> live -> retired
    """
    client = MlflowClient()
    client.set_model_version_tag(PRICING_MODEL_NAME, version, "status", stage)
    client.set_model_version_tag(PRICING_MODEL_NAME, version, "approved_by", approver)
    print(f"Model version {version} transitioned to '{stage}' by {approver}")


if __name__ == "__main__":
    print("Model registry transitions would be triggered from CI/CD on merge here.")
