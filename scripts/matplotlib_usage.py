# -*- coding: utf-8 -*-

################################################################################
# showcase some very basic usage of matplotlib from ipython shell
################################################################################

## IMPORT matplotlib and check if it's interactive
import matplotlib
matplotlib.is_interactive()
matplotlib.interactive(True)

## let see what backend we use
%matplotlib

## these are the usual imports
import matplotlib.pyplot as plt
import numpy as np

# get some dummy data
x = np.arange(-5, 5, .2)
y = np.sin(x)

## state-machine like behavior (MATLAB)
# how to create a new figure
plt.figure()

# new figure with non-default size
plt.figure(2, figsize=(4, 3))

# get the current figure
plt.gcf()
# get the current axes
plt.gca()

plt.subplot(2,3,1)
