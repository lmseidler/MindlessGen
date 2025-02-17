"""
This module contains the parameters for the mindlessgen package.
"""

MAX_ELEM = 86

# Covalent radii (taken from Pyykko and Atsumi, Chem. Eur. J. 15, 2009, 188-197)
# Values for metals decreased by 10%
# D3 covalent radii used to construct the coordination number
COV_RADII_PYYKKO = [
    0.32,
    0.46,  # H, He
    1.20,
    0.94,
    0.77,
    0.75,
    0.71,
    0.63,
    0.64,
    0.67,  # Li-Ne
    1.40,
    1.25,
    1.13,
    1.04,
    1.10,
    1.02,
    0.99,
    0.96,  # Na-Ar
    1.76,
    1.54,  # K, Ca
    1.33,
    1.22,
    1.21,
    1.10,
    1.07,  # Sc-
    1.04,
    1.00,
    0.99,
    1.01,
    1.09,  # -Zn
    1.12,
    1.09,
    1.15,
    1.10,
    1.14,
    1.17,  # Ga-Kr
    1.89,
    1.67,  # Rb, Sr
    1.47,
    1.39,
    1.32,
    1.24,
    1.15,  # Y-
    1.13,
    1.13,
    1.08,
    1.15,
    1.23,  # -Cd
    1.28,
    1.26,
    1.26,
    1.23,
    1.32,
    1.31,  # In-Xe
    2.09,
    1.76,  # Cs, Ba
    1.62,
    1.47,
    1.58,
    1.57,
    1.56,
    1.55,
    1.51,  # La-Eu
    1.52,
    1.51,
    1.50,
    1.49,
    1.49,
    1.48,
    1.53,  # Gd-Yb
    1.46,
    1.37,
    1.31,
    1.23,
    1.18,  # Lu-
    1.16,
    1.11,
    1.12,
    1.13,
    1.32,  # -Hg
    1.30,
    1.30,
    1.36,
    1.31,
    1.38,
    1.42,  # Tl-Rn
    2.01,
    1.81,  # Fr, Ra
    1.67,
    1.58,
    1.52,
    1.53,
    1.54,
    1.55,
    1.49,  # Ac-Am
    1.49,
    1.51,
    1.51,
    1.48,
    1.50,
    1.56,
    1.58,  # Cm-No
    1.45,
    1.41,
    1.34,
    1.29,
    1.27,  # Lr-
    1.21,
    1.16,
    1.15,
    1.09,
    1.22,  # -Cn
    1.36,
    1.43,
    1.46,
    1.58,
    1.48,
    1.57,  # Nh-Og
]

COV_RADII_MLMGEN = [
    0.42666663,
    0.6133333,
    1.59999996,
    1.25333325,
    1.02666658,
    0.99999994,
    0.94666658,
    0.83999994,
    0.85333326,
    0.8933333,
    1.86666651,
    1.66666656,
    1.50666656,
    1.38666653,
    1.4666666,
    1.35999989,
    1.31999993,
    1.27999989,
    2.3466665,
    2.05333315,
    1.77333328,
    1.6266666,
    1.61333328,
    1.4666666,
    1.42666664,
    1.38666653,
    1.33333325,
    1.31999993,
    1.34666657,
    1.45333329,
    1.49333325,
    1.45333329,
    1.53333321,
    1.4666666,
    1.51999988,
    1.55999984,
    2.51999982,
    2.22666647,
    1.95999991,
    1.8533332,
    1.75999996,
    1.65333324,
    1.53333321,
    1.50666656,
    1.50666656,
    1.43999997,
    1.53333321,
    1.63999992,
    1.70666652,
    1.67999988,
    1.67999988,
    1.63999992,
    1.75999996,
    1.74666648,
    2.78666637,
    2.3466665,
    2.15999987,
    1.95999991,
    2.10666659,
    2.09333327,
    2.07999979,
    2.06666647,
    2.01333319,
    2.02666651,
    2.01333319,
    1.99999987,
    1.98666655,
    1.98666655,
    1.97333324,
    2.03999983,
    1.94666659,
    1.82666656,
    1.74666648,
    1.63999992,
    1.57333316,
    1.54666652,
    1.47999992,
    1.49333325,
    1.50666656,
    1.75999996,
    1.73333316,
    1.73333316,
    1.81333324,
    1.74666648,
    1.83999988,
    1.89333316,
    2.67999982,
    2.41333311,
    2.22666647,
    2.10666659,
    2.02666651,
    2.03999983,
    2.05333315,
    2.06666647,
]
