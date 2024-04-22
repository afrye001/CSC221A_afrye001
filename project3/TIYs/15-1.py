# TIY 15-1 

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values] 

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots() 

ax.scatter(x_values, y_values, s = 10)
ax.plot(x_values, y_values, linewidth=2)

ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14) 

ax.tick_params(labelsize=14) 

plt.show()




