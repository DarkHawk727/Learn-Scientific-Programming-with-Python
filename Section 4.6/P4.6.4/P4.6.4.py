import numpy as np
import matplotlib as plt
from experiment import Experiment

R = 8.314

def description(T):
    return 'The rate of Chloroacetic acid hydrolysis at {}°C'.format(T)


temperatures = (40, 50, 60, 70, 80)
expts = []

for T in temperatures:
    filename = 'C:/Users/arjun/Learn-Scientific-Programming-with-Python-Solutions/LSPwP accompanying files/caa-{}.txt'.format(T)
    expt = Experiment(description(T))
    expt.load_data(filename)
    expt.fit_line(func_y=lambda c: 1/c)
    expts.append(expt)
    print('k = {:9.3e} M-1.s-1'.format(expt.m))

TK = np.array(temperatures) + 273.15
k = np.array([expt.m for expt in expts])

arrhenius = Experiment('Arrhenius plot for Chloroacetic acid hydrolysis')
arrhenius.set_data(TK, k)

print(arrhenius.x)
print(arrhenius.y)

m, c, r_2 = arrhenius.fit_line(func_x=lambda T: 1/T, func_y=lambda k: np.log(k))

A = np.exp(c)
Ea = -m * R
print('A = {:10.3e} M-1.s-1, Ea = {:5.1f} kJ.mol-1'.format(A, Ea/1000))
arrhenius.plot_data(True)