import math
from scipy import optimize
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

#Question 1
<<<<<<< HEAD
#Utility function defined
def u_func(c, l):
    return np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))) - v*l **(1+1/eps)/(1+1/eps)

#Variables defined
=======
def u_func(c, l,):
    return np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))) - v*l **(1+1/eps)/(1+1/eps)


>>>>>>> 2f1b32b2bf59db8902888845486cd90a285ecd6c
m = 1
v = 10
eps = 0.3
t_0 = 0.4
t_1 = 0.1
kappa = 0.4

<<<<<<< HEAD
#Lists pre defined
l_plot = []
c_plot = []
w_plot = []

#Der er lagt 0.05 til i enden af rangen, for at tage højde for 0 indexing.
for w in np.arange(0.5,1.5 + 0.05,0.05):
    def value_of_choice(l,m,v,eps,t_0,t_1,kappa,w):
        c = m + w * l - (t_0 * w * l + t_1 * max(w * l - kappa,0))
        return -u_func(c,l)

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
=======


#pre define lists
l_plot = []
c_plot = []
w_plot = []

#Der er lagt 0.05 til i enden af rangen, for at tage højde for 0 indexing.
for w in np.arange(0.5,1.5 + 0.05,0.05):
    def print_solution(c,l,u):
        print(f'c = {c:.3f}')
        print(f'l = {l:.3f}')
        print(f'u  = {u:.3f}')

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
    l_plot.append(f'{l:.3}')
    c_plot.append(f'{c:.3}')
    w_plot.append(w)

#print the newly stored lists (to see that they are stored correctly)
>>>>>>> 2f1b32b2bf59db8902888845486cd90a285ecd6c
print('l results: ' + str(l_plot))
print('c results: ' + str(c_plot))
print('w results: ' + str(w_plot))

#Question 2
<<<<<<< HEAD
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
=======
print(l_plot)
print(c_plot)
print(w_plot)

plt.plot(w_plot,l_plot)
plt.show()

plt.plot(w_plot,c_plot)
>>>>>>> 2f1b32b2bf59db8902888845486cd90a285ecd6c
plt.show()

#Question 3
N = 10000

#def tax_rev(l):
#    return sum(t_0 * w * l + t_1 * max(w * l - kappa, 0))
#print(tax_rev)

w = np.random.uniform(size=N, low=0.5, high=1.5)
    
tax_revenue = np.sum(t_0 * w * l + t_1 * np.max(w * l - kappa, 0))
print(tax_revenue)

#Question 4
<<<<<<< HEAD
eps_ny = 0.1

def u_func2(c, l):
    return np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))) - v*l **(1+1/eps_ny)/(1+1/eps_ny)
    
for w in np.arange(0.5,1.5 + 0.05,0.05):
    def value_of_choice2(l,m,v,eps_ny,t_0,t_1,kappa,w):
        c = m + w * l - (t_0 * w * l + t_1 * max(w * l - kappa,0))
        return -u_func(c,l)

    sol_case = optimize.minimize_scalar(
        value_of_choice2,method='bounded',
        bounds=(0,1),args=(m,v,eps_ny,t_0,t_1,kappa,w))

    l = sol_case.x
    c = m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0))
    
w = np.random.uniform(size=N, low=0.5, high=1.5)
    
tax_revenue = np.sum(t_0 * w * l + t_1 * np.max(w * l - kappa, 0))
print(tax_revenue)

#Question 5
=======
eps = 0.1

#pre define lists
l_plot_ny = []
c_plot_ny = []
w_plot_ny = []

for w in np.arange(0.5,1.5 + 0.05,0.05):
    def print_solution_ny(c,l,u):
        print(f'c = {c:.3f}')
        print(f'l = {l:.3f}')
        print(f'u  = {u:.3f}')

    def value_of_choice_ny(l,m,v,eps,t_0,t_1,kappa,w):
        c = np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0)))
        return -u_func(c,l)

    sol_case = optimize.minimize_scalar(
        value_of_choice,method='bounded',
        bounds=(0,1),args=(m,v,eps,t_0,t_1,kappa,w))

    l = sol_case.x
    c = np.log(m + w * l - (t_0 * w * l + t_1 * max(w * l-kappa,0)))
    u = u_func(c,l)
    print_solution_ny(c,l,u)

    # Store results as lists
    l_plot_ny.append(f'{l:.3}')
    c_plot_ny.append(f'{c:.3}')
    w_plot_ny.append(w)

#print the newly stored lists (to see that they are stored correctly)
print('l results: ' + str(l_plot_ny))
print('c results: ' + str(c_plot_ny))
print('w results: ' + str(w_plot_ny))

#Question 2
print(l_plot_ny)
print(c_plot_ny)
print(w_plot_ny)

plt.plot(w_plot_ny,l_plot_ny)
plt.show()

plt.plot(w_plot_ny,c_plot_ny)
plt.show()
>>>>>>> 2f1b32b2bf59db8902888845486cd90a285ecd6c
