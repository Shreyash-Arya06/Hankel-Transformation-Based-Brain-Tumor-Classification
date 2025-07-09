# Function to extract feature from images

import numpy as np
from radial_profile import radial_profile
from hankel_transform import hankel_transform_1d

def extract_patch_features(img, patch_size=(64, 64)):
    h, w = img.shape
    patch_data = []

    for i in range(0, h, patch_size[0]):
        for j in range(0, w, patch_size[1]):
            patch = img[i:i+patch_size[0], j:j+patch_size[1]]
            if patch.shape[0] != patch_size[0] or patch.shape[1] != patch_size[1]:
                continue
            radial = radial_profile(patch)
            r = np.arange(len(radial))
            k, hankel = hankel_transform_1d(radial, r)
            hankel_features = np.abs(hankel[:50])
            row = {
                'patch_x': j,
                'patch_y': i,
            }
            for idx, val in enumerate(hankel_features):
                row[f"hankel_f_{idx}"] = val
            patch_data.append(row)

    return patch_data
