#!/usr/bin/env python
"""Processing routines for the waveFlapper case."""

import foampy
import numpy as np
import matplotlib.pyplot as plt

width_2d = 0.1
width_3d = 3.66
m_paddle = 1270.0  # Paddle mass in kg, from OMB manual
h_piston = 3.3147
I_paddle = 1/3*m_paddle*h_piston**2


def plot_force():
    """Plots the streamwise force on the paddle over time."""
    pass


def plot_moment():
    data = foampy.load_forces()
    i = 10
    t = data["time"][i:]
    m = data.mz
    m = m[i:] * width_3d / width_2d
    period = 2.2
    omega = 2 * np.pi / period
    theta = 0.048 * np.sin(omega * t)
    theta_doubledot = -0.048 * omega**2 * np.sin(omega * t)
    m_inertial = I_paddle * theta_doubledot
    m = m + m_inertial
    plt.figure()
    plt.plot(t, m)
    plt.xlabel("Time (s)")
    plt.ylabel("Flapper moment (Nm)")
    print(
        "Max moment from CFD (including inertia) = {:0.1f} Nm".format(m.max())
    )
    print("Theoretical max moment (including inertia) =", 5500*3.3, "Nm")
    plt.show()


if __name__ == "__main__":
    plot_moment()
