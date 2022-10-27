from Objects.CurrentSourceBase import CurrentSourceBase
from Functions import pulse_I


class pulse_generator(CurrentSourceBase):
    """Rectangular pulse from t0 to t0+length"""
    def __init__(self, loc, t0=10, T=100, A=0.5, T0 = 10, N = 1):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param t0: current start time
        :param T: current length
        :param A: pulse amplitude (in normalized current units)
        
        :param T0: one pulse time
        :param N: count pulses
        """
        super().__init__(loc=loc)

        self.t0 = t0
        self.T = T
        self.A = A
        self.T0 = T0
        self.N = N

        self.name = "Pulse_Generator"
        
        

    def get_current_from_time(self, t):
        tau = (self.T - self.N*self.T0)/(self.N+1)
        if tau>0:
            s=0
            for i in range(0, self.N+1):
                if (self.t0+i*tau <= t <= self.t0+i*tau + tau):
                    s = 0
                elif (self.t0+i*(tau+self.T0) <= t <= self.t0+i*(tau+self.T0) + self.T0):
                    s = self.A
                return s

        else:
            print('False tau !!!!')
