from Objects.ComplexObjectBase import ComplexObjectBase


class SFQ_DC(ComplexObjectBase):
    """
    A converter from SFQ pulses to DC pulses

    Inputs:
    1 - SFQ pulse input
    2 - DC pulse output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 30

        self.name = 'SFQ_DC'
        self.description = 'SFQ to DC converter'

    def create_elements(self, sk):
        self.add_JJ(name='J0', A=2.42, B=0, c=1, loc=[sk[3], sk[4]])
        self.add_JJ(name='J1', A=1.77, B=0, c=1, loc=[sk[7], sk[11]])
        self.add_JJ(name='J2', A=1.77, B=0, c=1, loc=[sk[8], sk[7]])
        self.add_JJ(name='J3', A=1.37, B=0, c=1, loc=[sk[9], sk[10]])
        self.add_JJ(name='J4', A=1.37, B=0, c=1, loc=[sk[12], sk[13]])
        self.add_JJ(name='J5', A=2.7, B=0,  c=1, loc=[sk[15], 0])
        self.add_JJ(name='J6', A=2.7, B=0,  c=1, loc=[sk[23], sk[25]])
        self.add_JJ(name='J7', A=1, B=0, c=1, loc=[sk[16], sk[20]])
        self.add_JJ(name='J8', A=1.77, B=0,  c=1, loc=[sk[21], sk[22]])
        self.add_JJ(name='J9', A=1.96, B=0, c=1, loc=[sk[27], sk[28]])

        self.add_L(name='L0', val=0.75, loc=[sk[0], sk[3]])
        self.add_L(name='L1', val=0.04, loc=[sk[4], 0])
        self.add_L(name='L2', val=0.19, loc=[sk[3], sk[5]])
        self.add_L(name='L3', val=0.03, loc=[sk[6], sk[5]])
        self.add_L(name='L4', val=0.47, loc=[sk[5], sk[7]])
        self.add_L(name='L5', val=0.05, loc=[sk[13], 0])
        self.add_L(name='L6', val=0.19, loc=[sk[12], sk[11]])
        self.add_L(name='L7', val=0.92, loc=[sk[12], sk[14]])
        self.add_L(name='L8', val=0.7, loc=[sk[15], sk[14]])
        self.add_L(name='L9', val=0.71, loc=[sk[16], sk[14]])
        self.add_L(name='L10', val=0.04, loc=[sk[10], 0])
        self.add_L(name='L11', val=0.21, loc=[sk[8], sk[9]])
        self.add_L(name='L12', val=0.06, loc=[sk[9], sk[18]])
        self.add_L(name='L13', val=0.2, loc=[sk[19], sk[18]])
        self.add_L(name='L14', val=0.51, loc=[sk[18], sk[17]])
        self.add_L(name='L15', val=0.76, loc=[sk[16], sk[17]])
        self.add_L(name='L16', val=0.41, loc=[sk[17], sk[23]])
        self.add_L(name='L17', val=0.2, loc=[sk[23], sk[24]])
        self.add_L(name='L18', val=0.06, loc=[sk[25], 0])
        self.add_L(name='L19', val=0.17, loc=[sk[20], sk[21]])
        self.add_L(name='L20', val=0.15, loc=[sk[22], 0])
        
        self.add_L(name='L21', val=0.26, loc=[sk[21], sk[26]])
        self.add_L(name='L22', val=4.29, loc=[sk[26], sk[27]])
        self.add_L(name='L23', val=0.24, loc=[sk[28], sk[2]])
        self.add_L(name='L24', val=0.1, loc=[sk[28], sk[29]])
        self.add_L(name='L25', val=0.09, loc=[sk[26], sk[1]])

        self.add_ib(name='Ib1', val=2.6, loc=[sk[6]])
        self.add_ib(name='Ib2', val=1.4, loc=[sk[19]])
        self.add_ib(name='Ib3', val=1.8, loc=[sk[24]])
        self.add_ib(name='Ib4', val=3, loc=[sk[29]])
