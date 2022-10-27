from Objects.ComplexObjectBase import ComplexObjectBase


class MReceiver(ComplexObjectBase):
    """
    Matched Microstrip line (MSL) Receiver

    Inputs:
    1 - input from a superconductive line
    2 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 11

        self.name = 'MReceiver'
        self.description = 'Microstrip Receiver'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=1.54, loc=[sk[4]])
        self.add_ib(name='Ib2', val=1.4, loc=[sk[9]])

        self.add_JJ(name='Jin', c=1, r=1, A=0.96, B=0, loc=[sk[2], 0])
        self.add_JJ(name='J1', c=1, r=1, A=1.12, B=0, loc=[sk[6], 0])
        self.add_JJ(name='Jout', c=1, r=1, A=2.01, B=0, loc=[sk[8], 0])

        self.add_L(name='Lin', val=0.95, loc=[sk[0], sk[10]])
        self.add_L(name='L1', val=0.05, loc=[sk[10], sk[2]])
        self.add_L(name='L2', val=1.76, loc=[sk[10], sk[3]])
        self.add_L(name='L3', val=0.05, loc=[sk[3], sk[4]])
        self.add_L(name='L4', val=1.03, loc=[sk[3], sk[5]])
        self.add_L(name='L5', val=0.05, loc=[sk[5], sk[6]])
        self.add_L(name='L6', val=1.81, loc=[sk[5], sk[7]])
        self.add_L(name='L7', val=0.05, loc=[sk[7], sk[8]])
        self.add_L(name='L8', val=0.05, loc=[sk[7], sk[9]])
        self.add_L(name='Lout', val=0.75, loc=[sk[7], sk[1]])
