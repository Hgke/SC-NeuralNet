from Objects.ComplexObjectBase import ComplexObjectBase


class TFF(ComplexObjectBase):
    """
    T Flip-Flop element

    Inputs:
    1 - input signal
    2 - output signal
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 7

        self.name = 'TFF'
        self.description = 'T trigger with Read-Out line'

    def create_elements(self, sk):
        self.add_JJ(name='J2', c=1, r=1, A=1, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J4', c=1, r=1, A=1, B=0, loc=[sk[3], sk[6]])
        self.add_JJ(name='J1', c=1, r=1, A=1.5, B=0, loc=[sk[4], 0])
        self.add_JJ(name='J3', c=1, r=1, A=1.5, B=0, loc=[sk[6], 0])

        self.add_L(name='L0', val=1, loc=[sk[0], sk[3]])
        self.add_L(name='L1', val=2, loc=[sk[4], sk[5]])
        self.add_L(name='L2', val=2, loc=[sk[5], sk[6]])

        self.add_L(name='L3', val=1, loc=[sk[4], sk[1]])
        self.add_L(name='L4', val=1, loc=[sk[6], sk[2]])

        self.add_ib(name='Ib1', val=1.45, loc=[sk[4]])

        self.add_R(name='R1', r=1, loc=[sk[5], 0])
