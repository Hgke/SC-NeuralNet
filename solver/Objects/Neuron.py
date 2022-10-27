from Objects.ComplexObjectBase import ComplexObjectBase


class Neuron(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 4

        self.name = 'Neuron'
        self.description = 'Crotty Neuron 2010'

    def create_elements(self, sk):
        
        self.add_JJ(name='JJ_c', c=1, r=1, A=1, B=0, loc=[sk[3], sk[2]])
        self.add_JJ(name='JJ_p', c=1, r=1, A=1, B=0, loc=[sk[1], 0])
        
        self.add_L(name='L_c', val=0.0001, loc=[sk[0], sk[3]])
        self.add_L(name='L_s', val=4.948, loc=[sk[0], 0])
        self.add_L(name='L_p', val=4.948, loc=[sk[2], sk[1]])

        self.add_ib(name='I_NB', val=1, loc=[sk[2]])

        return new_names_obj
