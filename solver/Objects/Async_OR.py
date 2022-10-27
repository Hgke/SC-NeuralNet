from Objects.ComplexObjectBase import ComplexObjectBase


class Async_OR(ComplexObjectBase):
    """
    RSFQ logic asynchronous OR gate

    Inputs:
    1 - first input signal
    2 - second input signal
    3 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 9

        self.name = 'Async_OR'
        self.description = 'Asynchronous OR gate'

    def create_elements(self, sk):
         
        
        self.add_JJ(name='JJ_1', c=1, r=1, A=1, B=0, loc=[sk[0], sk[3]])
        self.add_JJ(name='JJ_2', c=1, r=1, A=1, B=0, loc=[sk[1], sk[4]])
        self.add_JJ(name='JJ_3', c=1, r=1, A=0.25, B=0, loc=[sk[3], 0])
        self.add_JJ(name='JJ_4', c=1, r=1, A=0.25, B=0, loc=[sk[4], 0])
        self.add_JJ(name='JJ_5', c=1, r=1, A=1, B=0, loc=[sk[3], sk[5]])
        self.add_JJ(name='JJ_6', c=1, r=1, A=1, B=0, loc=[sk[4], sk[5]])
        self.add_JJ(name='JJ_7', c=1, r=1, A=0.05, B=0, loc=[sk[6], 0])
        self.add_JJ(name='JJ_8', c=1, r=1, A=0.05, B=0, loc=[sk[7], 0])
        self.add_JJ(name='JJ_9', c=1, r=1, A=1, B=0, loc=[sk[2], sk[8]])
        
        self.add_ib(name='Ib_1', val=0.7, loc=[sk[5]])

        self.add_L(name='L_1', val=2, loc=[sk[5], sk[6]])
        self.add_L(name='L_2', val=2, loc=[sk[5], sk[2]])
        self.add_L(name='L_3', val=1, loc=[sk[8], 0])

        self.add_R(name='R_1', r=0.4, loc=[sk[6], sk[7]])
