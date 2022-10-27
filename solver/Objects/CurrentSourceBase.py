import numpy as np
from Objects.ElementBase import ElementBase


class CurrentSourceBase(ElementBase):
    """A base abstract class for current sources"""
    def __init__(self, loc):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        """
        super().__init__()

        if len(loc) == 1:
            loc = [loc[0], 0]
        self.loc = loc

        self.complex = False

        self.contains_current = False
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        return np.zeros((2, 2)) if 0 in self.loc else np.zeros((1, 1))

    def get_current_from_time(self, t):
        """
        Gets a current value of this source at arbitrary time moment.
        MUST be overridden in child classes.

        :param t: a time moment
        :return: a current value
        """
        raise NotImplementedError

    def get_right_side(self, sol, i, h):
        t = i * h

        val = self.get_current_from_time(t)

        if self.loc[0] == 0:  # no V+
            return np.array([-val])
        elif self.loc[1] == 0:  # no V-
            return np.array([val])
        else:
            return np.array([-val, val])

    def get_data(self, kind, t, sol):
        if kind == 'I':
            return np.array([self.get_current_from_time(i) for i in t])
        else:
            raise ValueError('Only I(t) data are avaliable for current sources')
