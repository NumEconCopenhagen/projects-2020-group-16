def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y

"""
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
"""

import math
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

#Question 1
def u_func(c, l):
    return np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))) - v*l **(1+1/eps)/(1+1/eps)

m = 1
v = 10
eps = 0.3
t_0 = 0.4
t_1 = 0.1
kappa = 0.4
#w = 0.5
#c = np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0)))

#pre define lists
l_plot = []
c_plot = []
w_plot = []

for w in np.arange(0.5,1.5,0.05):
    def print_solution(c,l,u):
        print(f'c = {c:.8f}')
        print(f'l = {l:.8f}')
        print(f'u  = {u:.8f}')

    def value_of_choice(l,m,v,eps,t_0,t_1,kappa,w):
        c = np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0)))
        return -u_func(c,l)

    sol_case = optimize.minimize_scalar(
        value_of_choice,method='bounded',
        bounds=(0,1),args=(m,v,eps,t_0,t_1,kappa,w))

    l = sol_case.x
    c = np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0)))
    u = u_func(c,l)
    print_solution(c,l,u)

    # Store results as lists
    l_plot.append(f'{l:.8}')
    c_plot.append(f'{c:.8}')
    w_plot.append(w)

#print the newly stored lists (to see that they are stored correctly)
print('l results: ' + str(l_plot))
print('c results: ' + str(c_plot))
print('w results: ' + str(w_plot))

#Question 2
print(l_plot)
print(c_plot)
print(w_plot)

plt.scatter(w_plot,l_plot)
plt.show()

plt.scatter(w_plot,c_plot)
plt.show()


w = range(0.5, 1.5, 0.1)
plt.plot(u)

#Question 3
N = 10000

def tax_rev(l):
    return sum(t_0 * w * l + t_1 * max(w * l - kappa, 0))
print(tax_rev)

#Question 4
eps_ny = 0.1