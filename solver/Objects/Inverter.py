from Objects.ComplexObjectBase import ComplexObjectBase


class Inverter(ComplexObjectBase):
    """
    Inverter (RSFQ logic NOT gate)

    Inputs:
    1 - input signal
    2 - clock
    3 - output signal
    """
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 27

        self.connect = connect
        self.type_p = type_p
        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w

        self.name = 'Inverter'
        self.description = 'RSFQ inverter'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=2.01, loc=[sk[5]])
        self.add_ib(name='Ib2', val=1.24, loc=[sk[18]])
        self.add_ib(name='Ib3', val=1.92, loc=[sk[13]])
        self.add_ib(name='Ib4', val=1.48, loc=[sk[24]])

        self.add_JJ(name='J1', A=2.01, B=0, r=1, c=1, loc=[sk[3], sk[4]])
        self.add_JJ(name='J2', A=2.48, B=0, r=1, c=1, loc=[sk[7], sk[8]])
        self.add_JJ(name='J3', A=1.12, B=0, r=1, c=1, loc=[sk[7], sk[9]])
        self.add_JJ(name='J4', A=1.4, B=0, r=1, c=1, loc=[sk[10], sk[11]])
        self.add_JJ(name='J5', A=2.35, B=0, r=1, c=1, loc=[sk[15], sk[16]])
        self.add_JJ(name='J6', A=2.84, B=0, r=1, c=1, loc=[sk[19], sk[20]])
        self.add_JJ(name='J7', A=2.35, B=0, r=1, c=1, loc=[sk[21], sk[22]])
        self.add_JJ(name='J8', A=2.11, B=0, r=1, c=1, loc=[sk[25], sk[26]])

        self.add_L(name='L1', val=0.75, loc=[sk[0], sk[3]])
        self.add_L(name='L2', val=0.011, loc=[sk[4], 0])
        self.add_L(name='L3', val=0.392, loc=[sk[3], sk[6]])
        self.add_L(name='L4', val=0.133, loc=[sk[5], sk[6]])
        self.add_L(name='L5', val=0.371, loc=[sk[6], sk[7]])
        self.add_L(name='L6', val=0.033, loc=[sk[8], 0])
        self.add_L(name='L7', val=0.369, loc=[sk[9], sk[10]])
        self.add_L(name='L8', val=0.124, loc=[sk[10], sk[12]])
        self.add_L(name='L9', val=0.217, loc=[sk[13], sk[12]])
        self.add_L(name='L10', val=2.23, loc=[sk[15], sk[12]])
        self.add_L(name='L11', val=0.396, loc=[sk[11], sk[14]])
        self.add_L(name='L12', val=0.215, loc=[sk[16], sk[14]])
        self.add_L(name='L13', val=0.492, loc=[sk[17], sk[15]])
        self.add_L(name='L14', val=0.127, loc=[sk[18], sk[17]])
        self.add_L(name='L15', val=0.386, loc=[sk[19], sk[17]])
        self.add_L(name='L16', val=0.008, loc=[sk[20], 0])
        self.add_L(name='L17', val=0.3, loc=[sk[1], sk[19]])
        self.add_L(name='L18', val=0.332, loc=[sk[14], sk[21]])
        self.add_L(name='L19', val=0.055, loc=[sk[22], 0])
        self.add_L(name='L20', val=0.646, loc=[sk[21], sk[23]])
        self.add_L(name='L21', val=0.192, loc=[sk[24], sk[23]])
        self.add_L(name='L22', val=0.423, loc=[sk[23], sk[25]])
        self.add_L(name='L23', val=0.011, loc=[sk[26], 0])
        self.add_L(name='L24', val=0.9, loc=[sk[25], sk[2]])

        self.add_R(name='R', r=5, loc=[sk[6], 0])
