from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import periodic_square


class PeriodicPulses(CurrentSourceBase):
    """
    A constant current source: I(t)=I0
    """
    def __init__(self, loc, t0, pulse_length, total_length, freq, A):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param val: normalized current value (I0)
        """
        super().__init__(loc=loc)

        self.name = 'PeriodicPulses'
        self.t0 = t0
        self.pulse_length = pulse_length
        self.total_length = total_length
        self.freq = freq
        self.A = A

    def get_current_from_time(self, t):
        return periodic_square(t, self.t0, self.pulse_length, self.total_length, self.freq, self.A)