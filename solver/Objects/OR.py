from Objects.ComplexObjectBase import ComplexObjectBase


class OR(ComplexObjectBase):
    """
    RSFQ logic OR gate

    Inputs:
    1 - first input signal
    2 - clock
    3 - second input signal
    4 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 4)
        self.N = 14

        self.name = 'OR'
        self.description = 'OR gate'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=1.408, loc=[sk[8]])
        self.add_ib(name='Ib2', val=1.408, loc=[sk[1]])
        self.add_ib(name='Ib3', val=1.056, loc=[sk[13]])
        self.add_ib(name='Ib4', val=1.056, loc=[sk[11]])

        self.add_JJ(name='J1', c=1, r=1, A=2, B=0, loc=[sk[7], 0])
        self.add_JJ(name='J2', c=1, r=1, A=1.408, B=0, loc=[sk[6], 0])
        self.add_JJ(name='J3', c=1, r=1, A=1.408, B=0, loc=[sk[0], sk[7]])
        self.add_JJ(name='J4', c=1, r=1, A=1.408, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J5', c=1, r=1, A=2, B=0, loc=[sk[8], 0])
        self.add_JJ(name='J6', c=1, r=1, A=1.408, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J7', c=1, r=1, A=1.408, B=0, loc=[sk[2], sk[8]])
        self.add_JJ(name='J8', c=1, r=1, A=1.408, B=0, loc=[sk[13], sk[4]])
        self.add_JJ(name='J9', c=1, r=1, A=1.408, B=0, loc=[sk[11], 0])
        self.add_JJ(name='J10', c=1, r=1, A=1.408, B=0, loc=[sk[11], sk[12]])
        self.add_JJ(name='J11', c=1, r=1, A=1.408, B=0, loc=[sk[9], 0])
        self.add_JJ(name='J12', c=1, r=1, A=1.408, B=0, loc=[sk[9], sk[10]])

        self.add_L(name='L1', val=5.72, loc=[sk[7], sk[6]])
        self.add_L(name='L2', val=5.72, loc=[sk[0], sk[2]])
        self.add_L(name='L3', val=1.43, loc=[sk[6], sk[11]])
        self.add_L(name='L4', val=1.43, loc=[sk[4], sk[9]])
        self.add_L(name='L5', val=2.15, loc=[sk[12], sk[3]])
        self.add_L(name='L6', val=2.15, loc=[sk[10], sk[3]])
        self.add_L(name='L7', val=2.15, loc=[sk[1], sk[5]])
        self.add_L(name='L8', val=2.15, loc=[sk[1], sk[13]])
