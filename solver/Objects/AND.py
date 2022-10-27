from Objects.ComplexObjectBase import ComplexObjectBase


class AND(ComplexObjectBase):
    """
    RSFQ logic AND gate

    Inputs:
    1 - first input signal
    2 - clock
    3 - second input signal
    4 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 4)
        self.N = 12

        self.name = 'AND'
        self.description = 'AND gate'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=0.2, loc=[sk[4]])
        self.add_ib(name='Ib2', val=0.2, loc=[sk[8]])
        self.add_ib(name='Ib3', val=0.3, loc=[sk[3]])

        self.add_JJ(name='J1', c=1, A=0.25, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J2', c=1, A=0.75, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J3', c=1, A=0.176, B=0, loc=[sk[0], sk[4]])
        self.add_JJ(name='J4', c=1, A=0.176, B=0, loc=[sk[6], sk[5]])
        self.add_JJ(name='J5', c=1, A=0.25, B=0, loc=[sk[8], 0])
        self.add_JJ(name='J6', c=1, A=0.75, B=0, loc=[sk[9], 0])
        self.add_JJ(name='J7', c=1, A=0.176, B=0, loc=[sk[2], sk[8]])
        self.add_JJ(name='J8', c=1, A=0.176, B=0, loc=[sk[7], sk[9]])
        self.add_JJ(name='J9', c=1, A=0.176, B=0, loc=[sk[10], sk[3]])
        self.add_JJ(name='J10', c=1, A=0.176, B=0, loc=[sk[11], sk[3]])
        self.add_JJ(name='J11', c=1, A=1, B=0, loc=[sk[3], 0])

        self.add_L(name='L1', val=15.1, loc=[sk[4], sk[5]])
        self.add_L(name='L2', val=15.1, loc=[sk[8], sk[9]])
        self.add_L(name='L3', val=3.78, loc=[sk[5], sk[10]])
        self.add_L(name='L4', val=3.78, loc=[sk[9], sk[11]])
        self.add_L(name='L5', val=5.68, loc=[sk[1], sk[6]])
        self.add_L(name='L6', val=5.68, loc=[sk[1], sk[7]])
