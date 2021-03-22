# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

# -----------------------------------------
# plt.plot
# plt.show
# plt.figure
# plt.title
plt.figure(num=0, figsize=(8, 5))
plt.title('title!!')
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)
plt.show()

# -----------------------------------------
# plt.xlim, ylim
# plt.xlabel, ylabel
plt.figure(num=1, figsize=(10, 5), )
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks_x = np.linspace(-1, 2, 6)
plt.xticks(new_ticks_x)
plt.yticks([-2, -1.6, -1, 1.2, 2],
			[r'really bad', r'bad', r'normal', r'good', r'really good'])
plt.show()


