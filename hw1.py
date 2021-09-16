# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:15:40 2020

@author: simon
"""

import numpy as np                  # imports the numeric python library
from matplotlib import pyplot as plt   # imports the required libraries for plotting
dt = 1/1000                             # time increment
t = np.arange(-1,1,dt)                  # vector [-1,-0.99, ...]
f0 = 4                                  # frequency
x = 100 * np.real(np.exp(1j*(2*np.pi*f0*(t - 0.75))))
plt.figure(figsize = (10,5)) # Set up the figure object
plt.plot(t,x)                           # Draw the plot
plt.title("Section of a sinusoid")      # Add the title
plt.xlabel("time (sec)")                # Add label for x-axis
plt.show()                              # Pull up the plot