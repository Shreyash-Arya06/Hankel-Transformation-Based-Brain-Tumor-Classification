# Function to provide the patch features from the images

import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

from radial_profile import radial_profile
from hankel_transform import hankel_transform_1d

def extract_patch_features(img, patch_size=(64, 64)):
    h, w = img.shape
    rows = []

    for i in range(0, h, patch_size[0]):
        for j in range(0, w, patch_size[1]):
            patch = img[i:i + patch_size[0], j:j + patch_size[1]]
            if patch.shape != patch_size:
                continue

            radial = radial_profile(patch)
            r = np.arange(len(radial))
            _, hankel = hankel_transform_1d(radial, r)
            hankel_abs = np.abs(hankel[:50])

            row = {
                "patch_x": j,
                "patch_y": i,
                "hankel_mean": np.mean(hankel_abs),
                "hankel_std": np.std(hankel_abs),
                "hankel_skew": skew(hankel_abs),
                "hankel_kurtosis": kurtosis(hankel_abs),
                "hankel_peak": np.max(hankel_abs),
            }
            rows.append(row)

    if rows:
        df = pd.DataFrame(rows)
        avg = {
            "patch_x": "avg",
            "patch_y": "avg",
            "hankel_mean": df["hankel_mean"].mean(),
            "hankel_std": df["hankel_std"].mean(),
            "hankel_skew": df["hankel_skew"].mean(),
            "hankel_kurtosis": df["hankel_kurtosis"].mean(),
            "hankel_peak": df["hankel_peak"].mean(),
        }
        rows.append(avg)

    return rows