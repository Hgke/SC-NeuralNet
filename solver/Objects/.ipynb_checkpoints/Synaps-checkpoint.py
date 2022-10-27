from Objects.ComplexObjectBase import ComplexObjectBase


class Synaps(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 3

        self.name = 'Synaps'
        self.description = 'Crotty Synaps 2010'

    def create_elements(self, sk):
        
        self.add_L(name='L_syn', val=1, loc=[sk[0], sk[2]])
        self.add_R(name='R_syn', r=0.01, loc=[sk[2], sk[1]])
        
        self.add_C(name='C_syn', c=1, loc=[sk[1], 0])

       
