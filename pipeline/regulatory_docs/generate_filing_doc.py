"""
Auto-generates a draft regulatory filing exhibit from the same versioned,
actuarial-approved feature definition used earlier in the pipeline.

Turns a multi-day manual drafting exercise into a same-day
review-and-submit exercise for legal/compliance -- the exhibit is
populated from data actuarial already signed off on, not re-typed from
scratch.

Illustrative sample only -- real SERFF filings have state-specific
requirements this does not attempt to model.
"""

import yaml
from jinja2 import Template


FILING_TEMPLATE = """
RATE FILING EXHIBIT (DRAFT -- FOR LEGAL/COMPLIANCE REVIEW)
============================================================
Rating Factor: {{ feature.display_name }}
Feature ID: {{ feature.id }}
Prepared: auto-generated from approved feature definition v{{ feature.id }}

1. DESCRIPTION OF CHANGE
{{ description }}

2. DATA SOURCES
{% for source in data_sources %}- {{ source }}
{% endfor %}

3. ACTUARIAL REVIEW SUMMARY
Reviewer: {{ actuarial.reviewer }}
Maximum rate disruption threshold applied: {{ actuarial.rate_disruption_threshold_pct }}%

4. PROPOSED EFFECTIVE STATES
{% for state in approved_states %}- {{ state }}
{% endfor %}

5. CONSUMER DISCLOSURE LANGUAGE
See: {{ disclosure_ref }}

---
This draft was generated automatically from a version-controlled, actuarial-approved
feature definition. It requires legal/compliance review before submission -- it is a
starting point, not a substitute for that review.
"""


def generate_filing_draft(feature_def_path: str) -> str:
    with open(feature_def_path) as f:
        feature_def = yaml.safe_load(f)

    template = Template(FILING_TEMPLATE)
    return template.render(
        feature=feature_def["feature"],
        description=feature_def["description"].strip(),
        data_sources=feature_def["data_sources"]["data_sources"] if isinstance(
            feature_def["data_sources"], dict) and "data_sources" in feature_def["data_sources"]
            else [feature_def["data_sources"]] if isinstance(feature_def["data_sources"], str)
            else list(feature_def.get("data_sources", {}).keys()),
        actuarial=feature_def["actuarial_review"],
        approved_states=feature_def["model"].get("approved_states", []),
        disclosure_ref=feature_def["regulatory"]["disclosure_language_ref"],
    )


if __name__ == "__main__":
    print("Would render filing draft from pipeline/feature_definitions/rating_variable.yaml")
