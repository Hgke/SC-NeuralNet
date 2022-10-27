from Objects.CurrentSourceBase import CurrentSourceBase


class Ib(CurrentSourceBase):
    """
    A constant current source: I(t)=I0
    """
    def __init__(self, loc, val):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param val: normalized current value (I0)
        """
        super().__init__(loc=loc)

        self.val = val
        self.name = 'Ib'

    def get_current_from_time(self, t):
        return self.val
