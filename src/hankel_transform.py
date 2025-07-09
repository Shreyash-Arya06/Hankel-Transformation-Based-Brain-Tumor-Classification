# Function to implement the Hankel Transformation on the radial profile

import numpy as np
from scipy.special import j0
from scipy.integrate import simpson as simps

def hankel_transform_1d(f, r, k_range=(0.01, 50), num_points=None):
    num_points = num_points or len(r)
    k = np.linspace(*k_range, num_points)
    result = [simps(f * r * j0(ki * r), r) for ki in k]
    return k, np.array(result)
