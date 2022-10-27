from Objects.ComplexObjectBase import ComplexObjectBase


class MDriver(ComplexObjectBase):
    """
    Matched Microstrip line (MSL) Driver

    Inputs:
    1 - input
    2 - output to a superconductive line
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 8

        self.name = 'MDriver'
        self.description = 'Microstrip Driver'

    def create_elements(self, sk):
        self.add_ib(name='Ib', val=2.77, loc=[sk[4]])

        self.add_JJ(name='Jin', c=1, r=1, A=2.01, B=0, loc=[sk[2], 0])
        self.add_JJ(name='Jout', c=1, r=1, A=2.01, B=0, loc=[sk[6], 0])

        self.add_L(name='Lin', val=0.75, loc=[sk[0], sk[7]])
        self.add_L(name='L1', val=0.05, loc=[sk[7], sk[2]])
        self.add_L(name='L2', val=0.6, loc=[sk[7], sk[3]])
        self.add_L(name='L3', val=0.05, loc=[sk[4], sk[3]])
        self.add_L(name='L4', val=0.62, loc=[sk[3], sk[5]])
        self.add_L(name='L5', val=0.05, loc=[sk[5], sk[6]])
        self.add_L(name='Lout', val=0.6, loc=[sk[5], sk[1]])

        self.add_R(name='R', r=1.5, loc=[sk[1], 0])
