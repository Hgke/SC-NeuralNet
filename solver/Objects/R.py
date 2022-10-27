import numpy as np
from scipy.integrate import simpson
from Objects.ElementBase import ElementBase


class R(ElementBase):
    """
    Resistor
    """
    def __init__(self, loc, r):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param r: normalized resistance
        """
        super().__init__()
        self.check_loc(loc, 2)
        self.loc = loc
        self.r = r

        self.name = 'R'
        self.complex = False

        self.contains_current = True
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        r = self.r

        if self.loc[0] == 0:  # no V+
            A = np.array([[0, -1],
                          [-1, -r]])
        elif self.loc[1] == 0:  # no V-
            A = np.array([[0, 1],
                          [1, -r]])
        else:
            A = np.array([[0, 0,  1],
                          [0, 0, -1],
                          [1, -1, -r]])

        return A

    def get_right_side(self, sol, i, h):
        return np.zeros(2) if 0 in self.data_index else np.zeros(3)

    def get_data(self, kind, t, sol):
        if kind == 'P':  # phi(t) = int_0^t V(t) dt
            new_data = np.zeros_like(t)
            volt = super().get_data('I', t, sol)
            for i, ti in enumerate(t):
                new_data[i] = simpson(volt[:i + 1], t[:i + 1])
            return new_data
        else:
            return super().get_data(kind, t, sol)


