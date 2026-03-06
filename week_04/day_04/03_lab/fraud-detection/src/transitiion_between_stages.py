from mlflow import MlflowClient

client = MlflowClient()

# Move version 1 to Staging for validation
client.transition_model_version_stage(
    name="FraudDetectionModel",
    version=1,
    stage="Staging"
)

# After validation passes, promote version 2 to Production
# archive_existing_versions=True automatically archives the previous production model
client.transition_model_version_stage(
    name="FraudDetectionModel",
    version=2,
    stage="Production",
    archive_existing_versions=True
)

# Add a description to document the reason
client.update_model_version(
    name="FraudDetectionModel",
    version=2,
    description="RF v2 — F1-macro 0.89. Passed McNemar test vs v1 (p<0.05). Promoted after staging validation."
)