from Objects.ComplexObjectBase import ComplexObjectBase


class Async_AND(ComplexObjectBase):
    """
    RSFQ logic asynchronous AND gate

    Inputs:
    1 - first input signal
    2 - second input signal
    3 - output
    """
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.check_loc(loc, 3)
        self.N = 7

        self.name = 'Async_AND'
        self.description = 'Asynchronous AND gate'

    def create_elements(self, sk):

        self.add_ib(name='Ib1', val=0.56, loc=[sk[2]])

        self.add_JJ(name='J1', c=1, r=0.5, A=0.672, B=0, loc=[sk[3], sk[2]])
        self.add_JJ(name='J2', c=1, r=0.5, A=0.672, B=0, loc=[sk[5], sk[2]])
        self.add_JJ(name='J3', c=1, r=0.25, A=1.5, B=0, loc=[sk[2], 0])
        self.add_JJ(name='JD1', c=1, r=0.5, A=0.48, B=0, loc=[sk[4], sk[2]])
        self.add_JJ(name='JD2', c=1, r=0.5, A=0.48, B=0, loc=[sk[6], sk[2]])

        self.add_L(name='L1', val=4.545, loc=[sk[0], sk[3]])
        self.add_L(name='L2', val=4.545, loc=[sk[1], sk[5]])

        self.add_R(name='RD1', r=2.79, loc=[sk[3], sk[4]])
        self.add_R(name='RD2', r=2.79, loc=[sk[5], sk[6]])
