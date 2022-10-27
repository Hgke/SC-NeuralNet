from Objects.ComplexObjectBase import ComplexObjectBase
import numpy as np


class Adder1Bit_HA2(ComplexObjectBase):
    def __init__(self, loc):
        super().__init__(loc=loc)

        self.N = 6

        self.name = 'Adder1Bit_HA2'
        self.description = '1-bit adder version HA2'

    def create_elements(self, sk):
        self.add_JJ(name='Jin1', A=1, B=0, r=1, c=1, loc=[sk[0], 0])
        self.add_JJ(name='Jin2', A=1, B=0, r=1, c=1, loc=[sk[1], 0])
        self.add_JJ(name='Jm', A=0, B=0.7, r=1, c=1, loc=[sk[5], 0])
        self.add_JJ(name='Jv1', A=0, B=0.1, r=1, c=1, loc=[sk[0], sk[5]])
        self.add_JJ(name='Jv2', A=0, B=0.1, r=1, c=1, loc=[sk[1], sk[5]])
        self.add_JJ(name='Jrs', A=0.1, B=0, r=1, c=1, loc=[sk[2], sk[4]])
        self.add_JJ(name='Jlc', A=0.4, B=0, r=1, c=1, loc=[sk[3], sk[5]])
        self.add_JJ(name='Jls', A=0.5, B=0, r=1, c=1, loc=[sk[4], sk[5]])
        self.add_JJ(name='Joutc', A=1, B=0, r=1, c=1, loc=[sk[3], 0])
        self.add_JJ(name='Jouts', A=1.5, B=0, r=1, c=1, loc=[sk[4], 0])
        self.add_JJ(name='Jrc1', A=0.1, B=0, r=1, c=1, loc=[sk[0], sk[3]])
        self.add_JJ(name='Jrc2', A=0.1, B=0, r=1, c=1, loc=[sk[1], sk[3]])

        self.add_ib('ibJin1', val=0.9, loc=[sk[0]])
        self.add_ib('ibJin2', val=0.9, loc=[sk[1]])
        self.add_ib('ibJm', val=0.65, loc=[sk[5]])
        self.add_ib('ibJoutc', val=0.9, loc=[sk[3]])
        self.add_ib('ibJouts', val=1.1, loc=[sk[4]])

    def get_phase(self, mas_phases, mode):
        X = np.zeros((mas_phases.shape[0], 3))
        F = np.zeros((mas_phases.shape[0], 10))

        X[:, 0] = mas_phases[:, self.loc[0] - 1]  # loc is 1-based, but arrays in Python are 0-based
        X[:, 1] = mas_phases[:, self.loc[1] - 1]
        X[:, 2] = mas_phases[:, self.loc[2] - 1]

        F[:, 0] = mas_phases[:, self.loc[3] - 1]
        F[:, 1] = mas_phases[:, self.loc[4] - 1]
        F[:, 2] = mas_phases[:, self.loc[5] - 1]

        F[:, 3] = X[:, 0] - F[:, 2]
        F[:, 4] = X[:, 1] - F[:, 2]
        F[:, 5] = X[:, 0] - F[:, 0]
        F[:, 6] = X[:, 1] - F[:, 0]
        F[:, 7] = F[:, 0] - F[:, 2]
        F[:, 8] = F[:, 1] - F[:, 2]
        F[:, 9] = X[:, 2] - F[:, 1]

        if mode == 0:
            return F
        else:
            return np.hstack((X, F[:, :2]))





