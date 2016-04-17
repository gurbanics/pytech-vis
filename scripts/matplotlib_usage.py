# -*- coding: utf-8 -*-

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
plt.figure()

plt.figure(2, figsize=(4, 3))

plt.gcf()

plt.gca()

plt.subplot(2,3,1)
