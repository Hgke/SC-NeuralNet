import numpy as np
from scipy.integrate import simpson
from Objects.ElementBase import ElementBase


class C(ElementBase):
    """
    Capacitor
    """
    def __init__(self, loc, c):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param c: normalized capacitance
        """
        super().__init__()
        self.check_loc(loc, 2)
        self.loc = loc
        self.c = c

        self.name = 'C'
        self.complex = False

        self.contains_current = True
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        c = self.c
        loc = self.data_index

        if loc[0] == 0:  # no V+
            A = np.array([[0, -1],
                         [-1, -(2 * h) / (3 * c)]])
        elif loc[1] == 0:  # no V-
            A = np.array([[0, 1],
                         [1, -(2 * h) / (3 * c)]])
        else:
            A = np.array([[0, 0, 1],
                          [0, 0, -1],
                          [1, -1, -(2 * h) / (3 * c)]])

        return A

    def get_right_side(self, sol, i, h):
        index_voltage = self.data_index

        if index_voltage[0] == 0:   # no V+
            vn_1 = - sol[index_voltage[1] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = - sol[index_voltage[1] - 1, i - 2] if i > 1 else 0  # V+ - V-
        elif index_voltage[1] == 0:  # no V-
            vn_1 = sol[index_voltage[0] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = sol[index_voltage[0] - 1, i - 2] if i > 1 else 0  # V+ - V-
        else:
            vn_1 = sol[index_voltage[0] - 1, i - 1] - sol[index_voltage[1] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = sol[index_voltage[0] - 1, i - 2] - sol[index_voltage[1] - 1, i - 2] if i > 1 else 0  # V+ - V-

        rhs = (4 / 3) * vn_1 - (1 / 3) * vn_2

        res = np.zeros(2 if 0 in self.data_index else 3)
        res[-1] = rhs

        return res

    def get_data(self, kind, t, sol):
        if kind == 'P':  # phi(t) = int_0^t V(t) dt
            new_data = np.zeros_like(t)
            volt = super().get_data('I', t, sol)
            for i, ti in enumerate(t):
                new_data[i] = simpson(volt[:i+1], t[:i+1])
            return new_data
        else:
            return super().get_data(kind, t, sol)

