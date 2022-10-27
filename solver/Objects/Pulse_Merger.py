from Objects.ComplexObjectBase import ComplexObjectBase


class Pulse_Merger(ComplexObjectBase):
    """
    SFQ pulse merger

    Inputs:
    1 - first input signal
    2 - second input signal
    3 - merged output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)

        self.N = 14

        self.name = 'Pulse_Merger'
        self.description = 'Merger 2 pulses to 1 pulse'

    def create_elements(self, sk):
        self.add_JJ(name='J3', c=1,  A=2.01, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J2', c=1, A=1.79, B=0, loc=[sk[5], sk[9]])
        self.add_JJ(name='J4', c=1, A=2.01, B=0, loc=[sk[6], sk[7]])
        self.add_JJ(name='J1', c=1, A=1.79, B=0, loc=[sk[8], sk[9]])
        self.add_JJ(name='J5', c=1, A=2.01, B=0, loc=[sk[12], sk[13]])

        self.add_ib(name='Ib1', val=4.1, loc=[sk[11]])

        self.add_L(name='L1', val=0.75, loc=[sk[0], sk[4]])
        self.add_L(name='L2', val=0.75, loc=[sk[1], sk[7]])
        self.add_L(name='Lp3', val=0.01, loc=[sk[3], 0])
        self.add_L(name='Lp2', val=0.25, loc=[sk[4], sk[5]])
        self.add_L(name='Lp4', val=0.01, loc=[sk[6], 0])
        self.add_L(name='Lp1', val=0.25, loc=[sk[7], sk[8]])
        self.add_L(name='L5', val=0.08, loc=[sk[9], sk[10]])
        self.add_L(name='L11', val=0.05, loc=[sk[11], sk[10]])
        self.add_L(name='L4', val=1, loc=[sk[10], sk[12]])
        self.add_L(name='Lp5', val=0.01, loc=[sk[13], 0])
        self.add_L(name='L3', val=0.75, loc=[sk[12], sk[2]])
