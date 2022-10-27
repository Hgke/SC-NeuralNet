import numpy as np
from matplotlib import pyplot as plt
import sys
import pickle
sys.path.insert(0, r'C:\Users\Admin\main\Science\Coding\SC-NeuralNet')
from Objects import Synaps, JTL, Square_pulse, R, L
from FunctionCompiler import *

Amplitude_steps = 0.1

Amplitude_signal_array = np.arange(0.5, 5, Amplitude_steps)  # амплитуда входного тока

dict_1_JJ1 = {}
dict_1_JJ10 = {}
dict_2_JJ1 = {}
dict_2_JJ10 = {}
count = 0

for amplitude_signal in Amplitude_signal_array:
    
    jtl_1 = JTL.JTL(loc=[1, 2], N=10, ib_val=0.75, l_val=3)
    Synaps_1 = Synaps.Synaps(loc=[2, 3], L_value=1,R_value=0.1,C_value=1)
    r_12 = R.R(loc=[3, 4], r=0.1)
    jtl_2 = JTL.JTL(loc=[4, 5], N=10, ib_val=0.75, l_val=3)
    pulse = Square_pulse.Square_pulse(loc=[1], t0=50, A=amplitude_signal, length=100)

    t = np.arange(0, 400, 0.5)
    fc = FunctionCompiler([jtl_1,Synaps_1, r_12,jtl_2,pulse], t)
    sol = fc.solve()

    count += 1
    print(f'{count} из {len(Amplitude_signal_array)}')

    dict_1_JJ1[tuple([amplitude_signal])] = fc.object_dict['JTL1_JJ1'].get_data("V", t,sol)
    dict_1_JJ10[tuple([amplitude_signal])] = fc.object_dict['JTL1_JJ10'].get_data("V", t,sol)
    dict_2_JJ1[tuple([amplitude_signal])] = fc.object_dict['JTL2_JJ1'].get_data("V", t,sol)
    dict_2_JJ10[tuple([amplitude_signal])] = fc.object_dict['JTL2_JJ10'].get_data("V", t,sol)

    with open("data/dict_1_JJ1.pkl", "wb") as f1:
        pickle.dump(dict_1_JJ1, f1)
        f1.close()
        
    with open("data/dict_1_JJ10.pkl", "wb") as f2:
        pickle.dump(dict_1_JJ10, f2)
        f2.close()
        
    with open("data/dict_2_JJ1.pkl", "wb") as f3:
        pickle.dump(dict_2_JJ1, f3)
        f3.close()
        
    with open("data/dict_2_JJ10.pkl", "wb") as f4:
        pickle.dump(dict_2_JJ10, f4)
        f4.close()
