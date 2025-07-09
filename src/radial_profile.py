# Function to extract radial profile from the images

import numpy as np

def radial_profile(img, center=None):
    y, x = np.indices(img.shape)
    center = center or np.array([x.max() / 2, y.max() / 2])
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2).astype(int)
    tbin = np.bincount(r.ravel(), img.ravel())
    nr = np.bincount(r.ravel())
    return tbin / (nr + 1e-8)
