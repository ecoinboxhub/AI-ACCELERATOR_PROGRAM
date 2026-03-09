
from eda import *

# Building user activity and trading features for fraud detection
def create_user_activity_features(ua):
    feats = ua.groupby("user_id").agg(
        num_deposits=("activity_type", lambda x: (x=="deposit").sum()),
        num_withdrawals=("activity_type", lambda x: (x=="withdrawal").sum()),
        total_deposit_amount=("amount",
            lambda x: ua.loc[x.index][ua.loc[x.index,"activity_type"]=="deposit"]["amount"].sum()),
        total_withdrawal_amount=("amount",
            lambda x: ua.loc[x.index][ua.loc[x.index,"activity_type"]=="withdrawal"]["amount"].sum()),
    ).reset_index()

    # First deposit / withdrawal timestamps
    first_dep = ua[ua["activity_type"]=="deposit"].groupby("user_id")["timestamp"].min()
    first_with = ua[ua["activity_type"]=="withdrawal"].groupby("user_id")["timestamp"].min()
    feats["first_deposit_time"]    = feats["user_id"].map(first_dep)
    feats["first_withdrawal_time"] = feats["user_id"].map(first_with)
    feats["time_to_first_withdrawal"] = (
        (feats["first_withdrawal_time"] - feats["first_deposit_time"])
        .dt.total_seconds() / 3600
    ).fillna(9999)
    return feats

# Build trade features
def create_trade_features(trades):
    return trades.groupby("user_id").agg(
        total_trading_volume=("volume", "sum"),
        total_trading_amount=("amount", "sum"),
        num_trades=("pair", "count"),
        num_unique_assets_traded=("pair", pd.Series.nunique)
    ).reset_index()

def build_feature_table(ua, trades):
    user_feats  = create_user_activity_features(ua)
    trade_feats = create_trade_features(trades)
    df = pd.merge(user_feats, trade_feats, on="user_id", how="left").fillna(0)
    df["trading_vs_deposit_ratio"] = (
        df["total_trading_volume"] / (df["total_deposit_amount"] + 1)
    )
    df["trades_per_deposit"] = df["num_trades"] / (df["num_deposits"] + 1)
    return df

features = build_feature_table(user_activity, trades)


# Merging features and engineering ratios
def label_suspicious_users(df, withdrawal_threshold=0.8,
                            trade_threshold=0.2, time_threshold=24):
    conditions = (
        (df["num_deposits"] > 0) &
        (df["num_withdrawals"] > 0) &
        (df["time_to_first_withdrawal"] <= time_threshold) &
        (df["trading_vs_deposit_ratio"] <= trade_threshold) &
        (df["total_withdrawal_amount"] >=
         withdrawal_threshold * df["total_deposit_amount"])
    )
    df["is_fraud"] = conditions.astype(int)
    return df

df = label_suspicious_users(features)
print(df["is_fraud"].value_counts())


#  Rule-Based Fraud Labelling
def label_suspicious_users(df, withdrawal_threshold=0.8,
                            trade_threshold=0.2, time_threshold=24):
    conditions = (
        (df["num_deposits"] > 0) &
        (df["num_withdrawals"] > 0) &
        (df["time_to_first_withdrawal"] <= time_threshold) &
        (df["trading_vs_deposit_ratio"] <= trade_threshold) &
        (df["total_withdrawal_amount"] >=
         withdrawal_threshold * df["total_deposit_amount"])
    )
    df["is_fraud"] = conditions.astype(int)
    return df

df = label_suspicious_users(features)
print(df["is_fraud"].value_counts())

