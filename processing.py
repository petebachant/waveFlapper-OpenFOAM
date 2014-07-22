#!/usr/bin/env python
"""
Processing routines for the waveFlapper case.

"""

import foampy
import numpy as np
import matplotlib.pyplot as plt

width_2d = 0.1
width_3d = 3.66

def plot_force():
    """Plots the streamwise force on the paddle over time."""
    
def plot_moment():
    data = foampy.load_forces_moments()
    i = 10
    t = data["time"][i:]
    m = data["moment"]["pressure"]["z"] + data["moment"]["viscous"]["z"]
    m = m[i:]*width_3d/width_2d
    plt.figure()
    plt.plot(t, m)
    plt.xlabel("t (s)")
    plt.ylabel("Flapper moment (Nm)")
    print("Max moment from CFD =", m.max(), "Nm")
    print("Theoretical max moment (including inertia) =", 5500*3.3, "Nm") 
    plt.show()
    
if __name__ == "__main__":
    plot_moment()
