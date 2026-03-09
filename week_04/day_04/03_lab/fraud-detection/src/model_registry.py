import mlflow
import mlflow.sklearn
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score
from model_training import *   # brings in rf, y_test, y_proba_rf, y_pred_rf etc.



mlflow.set_experiment("fraud-detection")

with mlflow.start_run(run_name="RandomForest_v1"):
    # Log hyperparameters
    mlflow.log_params({
        "n_estimators": 300,
        "max_depth": 10,
        "class_weight": "balanced_subsample"
    })

    # Log evaluation metrics
    mlflow.log_metrics({
        "roc_auc":  roc_auc_score(y_test, y_proba_rf),
        "f1_macro": f1_score(y_test, y_pred_rf, average="macro"),
        "accuracy": accuracy_score(y_test, y_pred_rf)
    })

    # Log and REGISTER model in one step
    mlflow.sklearn.log_model(
        rf, "model",
        registered_model_name="FraudDetectionModel"
    )

    # Tag with dataset / training metadata
    mlflow.set_tag("dataset_version", "v1.0")
    mlflow.set_tag("model_type", "RandomForest")

    