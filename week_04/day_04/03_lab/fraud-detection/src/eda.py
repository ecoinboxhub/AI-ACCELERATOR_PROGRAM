from data_and_library_import import *

# Exploratory data analysis: distribution of amount purchased

sns.displot(trades['amount'])
plt.ticklabel_format(style='plain', axis='x')
plt.title('Distribution of Amount Purchased')
plt.xlabel('Amount'); plt.ylabel('Frequency')
plt.tight_layout(); plt.show()

# Top 3 Trading Pairs by Volume
pair_volumes = trades.groupby('pair')['amount'].sum().sort_values(ascending=False)
top3 = pair_volumes.head(3)

plt.figure(figsize=(8,5))
top3.plot(kind='bar', color='skyblue')
plt.title('Top 3 Trading Pairs by Volume')
plt.ylabel('Total USD Volume'); plt.xlabel('Trading Pair')
plt.xticks(rotation=0); plt.tight_layout(); plt.show()

# Volatility Analysis (BTCNGN)
btc = trades[trades['pair'] == 'BTCNGN'].copy()
btc['price'] = btc['amount'] / btc['volume']
btc['timestamp'] = pd.to_datetime(btc['timestamp'])
btc['date'] = btc['timestamp'].dt.date

daily = btc.groupby('date')['price'].agg(['max','min','mean'])
daily['volatility'] = (daily['max'] - daily['min']) / daily['mean']
daily['vol_7d'] = daily['volatility'].rolling(7).mean()

plt.figure(figsize=(10,5))
plt.plot(daily.index, daily['vol_7d'], marker='o')
plt.title('7-Day Rolling BTCNGN Volatility')
plt.xlabel("Date"); plt.ylabel("Volatility"); plt.grid(True)
plt.tight_layout(); plt.show()

# Deposit Patterns (User Activity)
user_activity['timestamp'] = pd.to_datetime(user_activity['timestamp'])
deposits = user_activity[user_activity['activity_type'] == 'deposit'].copy()
deposits['day_of_week'] = deposits['timestamp'].dt.day_name()
deposits['hour'] = deposits['timestamp'].dt.hour

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day_counts = deposits.groupby('day_of_week').size().reindex(days)
hour_counts = deposits.groupby('hour').size()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
day_counts.plot(kind='bar', ax=axes[0], color='orange')
axes[0].set_title('Deposits by Day of Week')
hour_counts.plot(kind='bar', ax=axes[1], color='green')
axes[1].set_title('Deposits by Hour')
plt.tight_layout(); plt.show()

