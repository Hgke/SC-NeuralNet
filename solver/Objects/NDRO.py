from Objects.ComplexObjectBase import ComplexObjectBase


class NDRO(ComplexObjectBase):
    """
    NDRO (Non Destructive Read Out) cell
    Inputs:
    1 – clock 1 
    2 – input signal
    3 – clock 2
    4 – output signal
    5  – N/C
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 5)
        self.N = 12

        self.name = 'NDRO'
        self.description = 'NDRO cell'

    def create_elements(self, sk):
        self.add_ib(name='Ib1', val=1, loc=[sk[5]])
        self.add_ib(name='Ib2', val=1, loc=[sk[9]])
        self.add_ib(name='Ib3', val=1, loc=[sk[11]])

        self.add_JJ(name='J1', c=1,  A=1, B=0, loc=[sk[7], 0])
        self.add_JJ(name='J2', c=1,  A=1.5, B=0, loc=[sk[8], sk[11]])
        self.add_JJ(name='J3', c=1,  A=2, B=0, loc=[sk[9], 0])
        self.add_JJ(name='J4', c=1,  A=1.5, B=0, loc=[sk[11], 0])
        self.add_JJ(name='J5', c=1,  A=1.5, B=0, loc=[sk[5], sk[8]])
        self.add_JJ(name='J6', c=1,  A=1, B=0, loc=[sk[10], sk[11]])
        self.add_JJ(name='J7', c=1,  A=1, B=0, loc=[sk[6], sk[7]])

        self.add_L(name='L1', val=0.5, loc=[sk[1], sk[6]])
        self.add_L(name='L2', val=2, loc=[sk[7], sk[8]])
        self.add_L(name='L3', val=2, loc=[sk[8], sk[9]])
        self.add_L(name='L4', val=0.5, loc=[sk[2], sk[10]])
        self.add_L(name='L5', val=1, loc=[sk[9], sk[3]])
        self.add_L(name='L6', val=1, loc=[sk[11], sk[4]])
        self.add_L(name='L7', val=0.5, loc=[sk[0], sk[5]])
