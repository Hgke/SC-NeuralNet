from Objects.ComplexObjectBase import ComplexObjectBase


class Synaps(ComplexObjectBase):
    def __init__(self, loc, L_value=1, R_value=0.1, C_value=1):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 3

        self.L_value = L_value
        self.R_value = R_value
        self.C_value = C_value

        self.name = 'Synaps'
        self.description = 'Crotty Synaps 2010'

    def create_elements(self, sk):
        
        self.add_L(name='L_syn', val=self.L_value, loc=[sk[0], sk[2]])
        self.add_R(name='R_syn', r=self.R_value, loc=[sk[2], sk[1]])
        
        self.add_C(name='C_syn', c=self.C_value, loc=[sk[1], 0])

       
