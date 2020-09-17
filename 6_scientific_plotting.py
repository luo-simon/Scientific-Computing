"""
Project 6 - Scientific Plotting

Plot a 2D Sine function using pcolor with a flat shading,
then plot the same sine function in a new figure with two subplots, 
each with a different colourmap.

Then generate and plot values in an array of size (50,50) drawn from a normal distribution
(you will have to research that if you've never met it before).
Next, manipulate the array so that the lowest numbers are in the bottom-left,
and the highest numbers are in the bottom-right (shown above in the right image)
"""

import matplotlib.pyplot as plt
import numpy as np

##### SIN WAVE ####
x = np.linspace(0.0, 3*np.pi, num=50)

fig, axs = plt.subplots(1, 1)
ax = axs
c = ax.pcolor([np.sin(x)]*50, cmap='jet', edgecolors=(1,1,1,0.01))
ax.set_title('Sine - "Flat" (jet) colourmap')

fig, axs = plt.subplots(2, 1)

ax = axs[0]
c = ax.pcolor([np.sin(x)]*50, cmap='plasma', edgecolors=(1,1,1,0.01))
ax.set_title('Sine - Plasma colourmap')

ax = axs[1]
c = ax.pcolor([np.sin(x)]*50, cmap='binary', edgecolors=(1,1,1,0.01))
ax.set_title('Sine - Binary colourmap')

##### NORMAL DISTRIBUTION #####
N = np.random.normal(size=(50, 50))
N_sorted = np.sort(np.sort(N), axis=0)

fig, axs = plt.subplots(1, 2)

ax = axs[0]
c = ax.pcolor(N, cmap='jet')
ax.set_title('Random')

ax = axs[1]
c = ax.pcolor(N_sorted, cmap='jet')
ax.set_title('Sorted')

fig.tight_layout()
plt.show()