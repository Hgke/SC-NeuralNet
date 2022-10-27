from Objects.ComplexObjectBase import ComplexObjectBase


class PMerger2to1(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)
        self.N = 6

        self.name = 'SPL1to4'
        self.description = 'Split 1 to 4'

    def create_elements(self, sk):
        self.add_L(name='Lin', val=1.5, loc=[sk[0], sk[5]])

        self.add_JJ(name='Jm', A=1, B=0, r=1, c=1, loc=[sk[5], 0])
        self.add_JJ(name='Jo1', A=0.5, B=0, r=1, c=1, loc=[sk[5], sk[1]])
        self.add_JJ(name='Jo2', A=0.5, B=0, r=1, c=1, loc=[sk[5], sk[2]])
        self.add_JJ(name='Jo3', A=0.5, B=0, r=1, c=1, loc=[sk[5], sk[3]])
        self.add_JJ(name='Jo4', A=0.5, B=0, r=1, c=1, loc=[sk[5], sk[4]])

        self.add_ib(name='ibJm', val=0.75, loc=[sk[5]])
