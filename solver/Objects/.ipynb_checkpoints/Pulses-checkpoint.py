import numpy as np
from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import gauss_I


class Pulses(CurrentSourceBase):
    """Gaussian current pulse"""
    def __init__(self, loc, connect='Current', type_p='Gauss', t0=50, A=1, D=15, T=500, w=1):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param connect: not implemented yet, use 'current'
        :param type_p: 'Gauss' for a gaussian pulse, or 'Sin' for a sinusoidal wave
        :param t0: pulse time (for Gaussian pulse)
        :param A: pulse amplitude (for Gaussian pulse) (in normalized current units)
        :param D: pulse width
        :param T: pulses period
        :param w: sinusoidal wave frequency (for sinusoidal waves)
        """
        super().__init__(loc=loc)

        # numeric parameters
        if connect not in ['Current', 'Phase']:
            raise ValueError('Connect must be "Current" or "Phase"')
        self.connect = connect

        if type_p not in ['Gauss', 'Sin']:
            raise ValueError('type_p must be "Gauss" or "Sin"')
        self.type_p = type_p

        self.t0 = t0
        self.A = A
        self.D = D
        self.T = T
        self.w = w
        self.name = "Pulses"

    def get_current_from_time(self, t):
        sA = self.A
        if self.connect == 'Current' and self.type_p == 'Gauss':
            st0 = self.t0
            sD = self.D
            sT = self.T
            val = gauss_I(t, st0, sA, sD, sT)
        else:
            sw = self.w
            val = np.sin(sw * t)

        return val
