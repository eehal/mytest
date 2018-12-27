# Function: Root mean-square-error (RMSE)

import numpy as np

def rmse(true, predicted):
    return np.sqrt(((true - predicted) ** 2).mean())