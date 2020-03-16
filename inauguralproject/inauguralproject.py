import math
from scipy import optimize
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

#Question 1
#Utility function defined
def u_func(c, l):
    return np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))) - v*l **(1+1/eps)/(1+1/eps)

#Variables defined
m = 1
v = 10
eps = 0.3
t_0 = 0.4
t_1 = 0.1
kappa = 0.4

#Lists pre defined
l_plot = []
c_plot = []
w_plot = []

def value_of_choice(l,m,v,eps,t_0,t_1,kappa,w):
        c = m + w * l - (t_0 * w * l + t_1 * max(w * l - kappa,0))
        return -u_func(c,l)

#Der er lagt 0.05 til i enden af rangen, for at tage højde for 0 indexing.
for w in np.arange(0.5,1.5 + 0.05,0.05):
    

    sol_case = optimize.minimize_scalar(
        value_of_choice,method='bounded',
        bounds=(0,1),args=(m,v,eps,t_0,t_1,kappa,w))

    l = sol_case.x
    c = m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))

    # Store results as lists
    l_plot.append(f'{l:.3}')
    c_plot.append(f'{c:.3}')
    w_plot.append(f'{w:.3}')  

    #float l for plotting
    l_plot = [float(i) for i in l_plot]

#Print the newly stored lists (to see that they are stored correctly)
print('l results: ' + str(l_plot))
print('c results: ' + str(c_plot))
print('w results: ' + str(w_plot))

#Question 2
#Plot of labour and wage
plt.plot(w_plot, l_plot)
plt.xlabel("Wage")
plt.ylabel("Optimal labour")
plt.title("Labour")
plt.show()

#Plot of consumption and wage
plt.plot(w_plot, c_plot)
plt.xlabel("Wage")
plt.ylabel("Optimal consumption")
plt.title("Consumption")
plt.show()

#Question 3 & 4
def u_func3(c, l):
    return np.log(m + wi * l - (t_0 * wi * l + t_1 * max(wi * l-kappa,0))) - v*l **(1+1/eps)/(1+1/eps)

def value_of_choice3(l,m,v,eps,t_0,t_1,kappa,wi):
    c = m + wi * l - (t_0 * wi * l + t_1 * max(wi * l - kappa,0))
    return -u_func3(c,l)

N = 10000

# w = np.random.uniform(size=N, low=0.5, high=1.5)
w = np.linspace(0.5, 1.5, N)

for eps in [0.3, 0.1]:

    l = []
    c = []
    tax_revenue = 0
    for i, wi in enumerate(w):

        sol_case = optimize.minimize_scalar(
            value_of_choice3, method='bounded',
            bounds=(0,1),args=(m,v,eps,t_0,t_1,kappa,wi))

        l.append(sol_case.x)
        c.append(m + wi * l[-1] - (t_0 * wi * l[-1] + t_1 * max(wi * l[-1] - kappa,0)))

        tax_revenue += t_0 * wi * l[i] + t_1 * np.max(wi * l[i] - kappa, 0)
    print(tax_revenue)

#Question 5
N = 100
w = np.linspace(0.5, 1.5, N)
eps = 0.3
tax = {}

for t_0 in np.linspace(0,1, 10):
    for t_1 in np.linspace(0, 1, 10):
        for kappa in np.linspace(0, 1, 10):
            l = []
            c = []
            tax_revenue = 0
            for i, wi in enumerate(w):

                sol_case = optimize.minimize_scalar(
                    value_of_choice3, method='bounded',
                    bounds=(0,1),args=(m,v,eps,t_0,t_1,kappa,wi))

                l.append(sol_case.x)
                c.append(m + wi * l[-1] - (t_0 * wi * l[-1] + t_1 * max(wi * l[-1] - kappa,0)))

                tax_revenue += t_0 * wi * l[i] + t_1 * np.max(wi * l[i] - kappa, 0)
            key = (round(t_0, 2), round(t_1, 2), round(kappa, 2))
            tax[key] = tax_revenue
            print(f"{key} -> T = {round(tax_revenue,2)}")
