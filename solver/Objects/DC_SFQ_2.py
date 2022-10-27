from Objects.ComplexObjectBase import ComplexObjectBase


class DC_SFQ_2(ComplexObjectBase):
    """
    A converter from DC pulses to SFQ pulses

    Inputs:
    1 - DC pulse input
    2 - SFQ pulse output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 2)
        self.N = 13

        self.name = 'DC_SFQ'
        self.description = 'DC to SFQ converter'

    def create_elements(self, sk):

        self.add_ib(name='Ib1', val=-2.98, loc=[sk[10]])

        self.add_JJ(name='J1', c=1, r=1, A=1.18, B=0, loc=[sk[3], sk[4]])
        self.add_JJ(name='J2', c=1, r=1, A=1.37, B=0, loc=[sk[7], sk[8]])
        self.add_JJ(name='J3', c=1, r=1, A=1.37, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J4', c=1, r=1, A=1.96, B=0, loc=[sk[11], sk[12]])

        self.add_L(name='L2', val=1.27, loc=[sk[0], sk[2]])
        self.add_L(name='L8', val=1.36, loc=[sk[5], 0])
        self.add_L(name='L4', val=0.49, loc=[sk[2], sk[3]])
        self.add_L(name='Lp3', val=0.26, loc=[sk[6], sk[7]])
        self.add_L(name='L5', val=0.49, loc=[sk[2], sk[5]])
        self.add_L(name='Lp2', val=0.07, loc=[sk[8], 0])
        self.add_L(name='L10', val=0.08, loc=[sk[4], sk[7]])
        self.add_L(name='L6', val=0.43, loc=[sk[4], sk[9]])
        self.add_L(name='Lp11', val=0.03, loc=[sk[10], sk[9]])
        self.add_L(name='L13', val=0.66, loc=[sk[9], sk[11]])
        self.add_L(name='Lp4', val=0.05, loc=[sk[12], 0])
        self.add_L(name='L15', val=0.8, loc=[sk[11], sk[1]])

