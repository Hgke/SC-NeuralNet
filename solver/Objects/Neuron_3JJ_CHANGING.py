from Objects.ComplexObjectBase import ComplexObjectBase
import numpy as np


class Neuron_3JJ(ComplexObjectBase):
    """
        Output: JJ_2
    """
    
    def __init__(self, loc, eta=0.5, beta=0.2, l=5, l_s=3.85, ib=1.9/1.5):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 5
        
        self.eta = eta
        self.beta = beta
        self.l = l
        self.l_s = l_s
        self.ib = ib

        self.name = 'Neuron_3JJ'
        self.description = 'Neuron with 3 JJs'
        
        

    def create_elements(self, sk):
        
        self.add_JJ(name='JJ_1', c=self.beta, A=1, B=0, loc=[sk[2], sk[3]])
        self.add_JJ(name='JJ_2', c=self.beta, A=1, B=0, loc=[sk[1], 0])
        self.add_JJ(name='JJ_3', c=self.beta*self.eta, A=self.eta, B=0, loc=[sk[2], sk[1]])
        
        self.add_L(name='L_1', val=self.l, loc=[sk[0], 0])
        self.add_L(name='L_2', val=self.l_s, loc=[sk[0], sk[2]])
        self.add_L(name='L_3', val=self.l, loc=[sk[3], sk[4]])
        self.add_L(name='L_4', val=self.l_s, loc=[sk[4], sk[1]])

        self.add_ib(name='I_Bias', val=self.ib, loc=[sk[3]])
