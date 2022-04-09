from pydoc import describe
from Aviation import Aviation
import matplotlib.pyplot as plt
import pandas as pd


c = Aviation()
master = c.get_master_set()
print(master.head().to_string())
# print(master.describe())

df = master.copy()
df['ev_month'] = df['ev_month'].astype(int)
df['ev_year'] = df['ev_year'].astype(int)
df = df[['ev_year', 'ev_month', 'ground_injuries', 'total_injuries']]
df = df.groupby(by=['ev_year'], sort=True, as_index=False).sum()
# df['date'] = df['ev_month'].map(str)+ '-' +df['ev_year'].map(str)
# df['date'] = pd.to_datetime(df['date'], format='%m-%Y').dt.strftime('%m-%Y')
print(df)
# fig, ax = plt.subplots()
# plt.plot_date(df['ev_year'], df['ground_injuries'], color='blue')
# plt.plot_date(df['ev_year'], df['total_injuries'], color='green')
# plt.show()

#Plot configuration
fig, ax1 = plt.subplots()

#Plot 1 -- Ground Injuries
ax1.set_xlabel('Year')
ax1.set_ylabel('Ground Injuries (sum)', color='blue')
ax1.scatter(df['ev_year'], df['ground_injuries'], color='blue', label='Ground Injuries')
ax1.tick_params(axis='y', labelcolor='blue')

#Plot 2 -- Flight Injuries
ax2 = ax1.twinx()
ax2.set_ylabel('Flight Injuries (sum)', color='green')
ax2.scatter(df['ev_year'], df['total_injuries'], color='green', label='Flight Injuries')
ax2.tick_params(axis='y', labelcolor='green')

#Legends
plt.legend()
plt.show()