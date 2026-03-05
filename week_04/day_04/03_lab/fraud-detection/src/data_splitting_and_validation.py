from feature_engineering_and_labelling import *
# drop non-feature column

drop_cols = ["user_id", "first_deposit_time", "first_withdrawal_time"]
df_model = df.drop(columns=drop_cols)

X = df_model.drop(columns=["is_fraud"])
y = df_model["is_fraud"]

# Stratified Train / Holdout Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
print(f"Train size: {len(X_train)} | Test (holdout) size: {len(X_test)}")
print(f"Fraud rate (train): {y_train.mean():.2%}")
print(f"Fraud rate (test):  {y_test.mean():.2%}")

# Log-Transform Skewed Features
skewed_features = [
    "num_deposits", "total_deposit_amount",
    "total_withdrawal_amount", "total_trading_volume",
    "trading_vs_deposit_ratio"
]

for col in skewed_features:
    X_train[col] = np.log1p(X_train[col])
    X_test[col]  = np.log1p(X_test[col])


# StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform on train
X_test_scaled  = scaler.transform(X_test)        # transform only on test

# Convert back to DataFrames to keep column names
feature_cols = X.columns.tolist()
X_train_scaled = pd.DataFrame(X_train_scaled, columns=feature_cols, index=X_train.index)
X_test_scaled  = pd.DataFrame(X_test_scaled,  columns=feature_cols, index=X_test.index)

# Save Preprocessing Artifacts

# Save scaler and feature list for inference / API use
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(feature_cols, 'models/feature_columns.pkl')
