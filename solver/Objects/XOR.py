from Objects.ComplexObjectBase import ComplexObjectBase


class XOR(ComplexObjectBase):
    """
    RSFQ logic exclusive OR (XOR) gate

    Inputs:
    1 - first input signal
    2 - clock
    3 - second input signal
    4 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 4)
        self.N = 16

        self.name = 'XOR'
        self.description = 'Exclusive OR'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=8.67/5, loc=[sk[8]])

        self.add_JJ(name='J0', c=1, r=1, A=1.96, B=0, loc=[sk[4], sk[5]])
        self.add_JJ(name='J1', c=1, r=1, A=1.37, B=0, loc=[sk[5], sk[6]])
        self.add_JJ(name='J2', c=1, r=1, A=1.37, B=0, loc=[sk[5], 0])
        self.add_JJ(name='J3', c=1, r=1, A=1.37, B=0, loc=[sk[9], sk[11]])
        self.add_JJ(name='J4', c=1, r=1, A=1.37, B=0, loc=[sk[11], 0])
        self.add_JJ(name='J5', c=1, r=1, A=1.96, B=0, loc=[sk[11], sk[12]])
        self.add_JJ(name='J6', c=1, r=1, A=1.54, B=0, loc=[sk[13], sk[14]])
        self.add_JJ(name='J7', c=1, r=1, A=1.77, B=0, loc=[sk[15], sk[14]])
        self.add_JJ(name='J8', c=1, r=1, A=1.37, B=0, loc=[sk[14], 0])

        self.add_L(name='L0', val=1, loc=[sk[0], sk[4]])
        self.add_L(name='L1', val=1.92*2, loc=[sk[6], sk[10]])
        self.add_L(name='L2', val=1.92*2, loc=[sk[10], sk[9]])
        self.add_L(name='L3', val=1, loc=[sk[1], sk[12]])
        self.add_L(name='L4', val=0.15, loc=[sk[10], sk[13]])
        self.add_L(name='L5', val=0.4, loc=[sk[2], sk[15]])
        self.add_L(name='L6', val=1.8, loc=[sk[14], sk[3]])
        
        self.add_R(name='R1', r=5, loc=[sk[6], sk[7]])
        self.add_R(name='R2', r=2.5, loc=[sk[7], sk[9]])
        self.add_R(name='R3', r=2.5, loc=[sk[8], sk[7]])
