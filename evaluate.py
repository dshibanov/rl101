import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

# Че сделать то надо...
# def evaluation надо написать
# интересно а если попробовать сделать тут.. покурить надо вообщем...
#
# да цветовые схемы нужно раздобыть...
# ну вообще нормально же все вроде...
#
# так вот новый редактор получается...

#
# тогда как мне действовать
#
# писать световидам насчет...
# ну вот в начале им нужно написать
#
# 1) Дмитрий, Димитрий. Последовательность звуков делает всю работу?
# 2) Просьба оценить интервенцию. Какие реальности через мою натальную карту + ФИО1(ФИО2)
#
# вот это вот и нужно.. как можно быстрее)
# 3) также обьяснить им что я планировал обратную смену.. это был эксперимент
#       вопрос при прочих равных выбирать старое ФИО
# и че то еще...


# ну завтра постараюсь сделать..
# надо бы импортнуть среду...
# да импортнуть среду и этот график распечатать в матплотлибе

# нужно тогда импортнуть среду..
# но для этого


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


# TODO:
#       - install openmw
#             - how to play
#       - create rl101 github
#       - move GW to envs and commit | push
#       - Matplotlib
#             - about. architecture. plotting backend
#             - custom tools
#       - Pandas




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig_2, axes_2 = plt.subplots(figsize=(4,4), nrows=1, ncols=3)
plt.tight_layout()


