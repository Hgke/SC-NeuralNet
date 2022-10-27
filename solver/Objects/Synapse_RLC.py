from Objects.ComplexObjectBase import ComplexObjectBase


class Synapse_RLC(ComplexObjectBase):
    def __init__(self, loc, r_syn=1, l_syn=1, c_syn=1, r_12=1):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 4
        
        self.r_syn = r_syn
        self.l_syn = l_syn
        self.c_syn = c_syn
        self.r_12 = r_12
        
        self.name = 'Synapse_RLC'
        self.description = 'Crotty synapse 2010'
        
    def create_elements(self, sk):
        self.add_L(name='L_syn', val=self.l_syn, loc=[sk[0], sk[2]])
        self.add_R(name='R_syn', r=self.r_syn, loc=[sk[2], sk[3]])
        self.add_C(name='C_syn', c=self.c_syn, loc=[sk[3], 0])
        self.add_R(name='R_12', r=self.r_12, loc=[sk[3], sk[1]])
