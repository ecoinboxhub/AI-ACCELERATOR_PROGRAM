
from data_splitting_and_validation import *

# Logistic Regression
from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
log_reg.fit(X_train_scaled, y_train)

# Evaluate with a lower threshold (0.3) to favour recall on fraud class
y_proba_lr = log_reg.predict_proba(X_test_scaled)[:, 1]
y_pred_lr  = (y_proba_lr >= 0.3).astype(int)

print("=== Logistic Regression ===")
print(classification_report(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, y_proba_lr))


# Random Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=300, max_depth=10, min_samples_leaf=5,
    class_weight="balanced_subsample", random_state=42, n_jobs=-1
)
rf.fit(X_train_scaled, y_train)

y_proba_rf = rf.predict_proba(X_test_scaled)[:, 1]
y_pred_rf  = (y_proba_rf >= 0.3).astype(int)

print("=== Random Forest ===")
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, y_proba_rf))


# xgboost
from xgboost import XGBClassifier

# scale_pos_weight compensates for class imbalance
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

xgb = XGBClassifier(
    n_estimators=400, max_depth=6, learning_rate=0.05,
    subsample=0.8, colsample_bytree=0.8,
    scale_pos_weight=scale_pos_weight,
    eval_metric="logloss", random_state=42
)
xgb.fit(X_train_scaled, y_train)

y_proba_xgb = xgb.predict_proba(X_test_scaled)[:, 1]
y_pred_xgb  = (y_proba_xgb >= 0.3).astype(int)

print("=== XGBoost ===")
print(classification_report(y_test, y_pred_xgb))
print("ROC-AUC:", roc_auc_score(y_test, y_proba_xgb))


