# TODO:
#       - Matplotlib
#             - about. architecture. plotting backend
#             - custom tools
#       - Pandas


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data']
              .view(np.recarray))
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0]) ** 2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

# plt.figure(figsize=(20,12))
from matplotlib.pyplot import figure

figure(figsize=(1, 1), dpi=80)
plt.show()

# - 2 -----------------------------
# panchamahabhutas F
#

# space, fire, air, water, earth
system  = np.array([13, 53, 10, 30, 3])
clrs = ['black', 'red', 'blue', 'silver', 'yellow']
names = ['space','fire','air', 'water', 'earth']
sanscritnames = ['akasha', 'agni', 'apu', 'vayu', 'prithvi']

# bars representation
# x = np.arange(5)
# plt.bar(x, height=system, color=['black', 'red', 'green', 'blue', 'cyan'])
# plt.xticks(x, ['space','fire','air', 'water', 'earth'])

# plt.pie(system, colors=clrs, labels=sanscritnames)
# plt.xticks(x, ['space','fire','air', 'water', 'earth'])


natalelements= system
name = np.array([13, 23, 10, 15, 33])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle('Intervention')
ax1.pie(natalelements, colors=clrs, labels=sanscritnames)
ax1.set_title('Entry Point / Prakriti / Current State')
ax2.pie(name, colors=clrs, labels=sanscritnames)
ax2.set_title('FIO')
ax1.set_facecolor('lightblue')
ax2.set_facecolor('lightblue')
ax3.set_facecolor('gray')
ax3.set_title('Superposition')

# TODO
#   add '+' betwen plots
# add superposition pie
# solve pie background




