# Illustrative deployment image for a pricing model/feature service.
# The same image is used for validation (CI), shadow-mode testing, and
# production -- eliminating "worked in the notebook, broke in prod" drift
# caused by mismatched dependency or data-freshness environments.

FROM python:3.11-slim

WORKDIR /app

COPY pipeline/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pipeline/ .

ENV PRICING_ENV=shadow
# Overridden to "production" only after feature-flag rollout begins;
# same image, different runtime config -- not a rebuild.

ENTRYPOINT ["python", "deployment/serve_pricing_model.py"]
