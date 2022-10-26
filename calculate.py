import numpy as np
from matplotlib import pyplot as plt

import pickle

from Objects import Pulses, L, R, C, Ib,Square_pulse,Pulses,Sine_current, Neuron_3JJ
from FunctionCompiler import *

L_massiv = np.around(np.linspace(0.06, 10, 40),1)
R_massiv = np.around(np.linspace(0.06, 10, 20),1)
C_massiv = np.around(np.linspace(0.06, 10, 50),1)

dictionar_1 = {}
dictionar_2 = {}



r_12_value = 0.01
a=5
time = 50
count = 0
for l_value in L_massiv:
    for r_value in R_massiv:
        for c_value in C_massiv:

            N1 = Neuron_3JJ.Neuron_3JJ(loc=[1,2])

            inductor = L.L(loc=[2,3], val=l_value)
            resistor = R.R(loc=[3,4], r=r_value)
            capacitance = C.C(loc=[4,0], c=c_value)

            r_12 = R.R(loc=[4,5],r=r_12_value)

            N2 = Neuron_3JJ.Neuron_3JJ(loc=[5,6])

            pulse_1 = Pulses.Pulses(loc=[1], t0=40, A=a, T=time)

            t = np.arange(0, 1500, 0.5)
            fc = FunctionCompiler([ pulse_1, N1, inductor, resistor, capacitance, r_12, N2],t)

            sol = fc.solve()

            V_N1 = fc.object_dict['Neuron_3JJ1_JJ_2'].get_data("V",t,sol);
            V_N2 = fc.object_dict['Neuron_3JJ2_JJ_2'].get_data("V",t,sol);
	    
            count += 1
            print(count)

            dictionar_1[tuple([a, l_value,r_value,c_value])] = V_N1
            dictionar_2[tuple([a, l_value,r_value,c_value])] = V_N2
            
            with open("dict_1.pkl", "wb") as f:
                pickle.dump(dictionar_1,f)
                f.close()
            with open("dict_2.pkl", "wb") as f:
                pickle.dump(dictionar_2,f)
                f.close()
    


            