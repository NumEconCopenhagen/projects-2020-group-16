def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y

import math
import numpy as np
from scipy import optimize

# The function, budget constraint is in place of the consumption as the model is static, and utility is monotically increasing in c, so there is no reason not to specd everything
def u_func(c, l, m = 1, eps = 0.3, v = 10, t_0 = 0.4, t_1 = 0.1, kappa = 0.4, w):
    return math.log(m + w * l - (t_0 * w * l + t_1 * max(w * l - kappa, 0))) - v * l ** (1 + 1 / eps) / (1 + 1 / eps)

# assigning values to the variables

#m = 1
#eps = 0.3
#v = 10
#t_0 = 0.4
#t_1 = 0.1
#kappa = 0.4

# Plot l* and c* as functions of w
import matplotlib.pyplot as plt
N = 10000

# Calculate the tax revenue
def tax_rev:
    return sum(t_0 * w * l + t_1 * max(w * l - kappa, 0))

# New epsilon
eps = 0.1