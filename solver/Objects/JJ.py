import numpy as np
from Objects.ElementBase import ElementBase


class JJ(ElementBase):
    """
    A Josephson junction simulated with a RCSJ model
    """
    def __init__(self, loc, c, A, B=1):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param c: junction normalized capacity
        :param r: junction normalized resistance
        :param A: junction normalized critical current
        :param B: junction normalized second harmonic of the critical current
        """
        # TODO: add B support
        super().__init__()
        self.check_loc(loc, 2)
        self.loc = loc
        self.r = 1 / A
        self.c = c
        
        self.A = A

        self.name = 'JJ'
        self.complex = False

        self.contains_current = True
        self.contains_variable = True

    def get_matrix_stamp(self, h):
        R = self.r
        C = self.c

        if self.loc[0] == 0:  # no V+
            A = np.array([[0, 0, -1],
                          [-1, -3/(2 * h), 0],
                          [-((2 * h + 3 * C * R) / (2 * R * h)), 0, -1]])
        elif self.loc[1] == 0:  # no V-
            A = np.array([[0, 0, 1],
                          [1, -3/(2 * h), 0],
                          [((2 * h + 3 * C * R) / (2 * R * h)), 0, -1]])
        else:

            A = np.array([[0, 0, 0, 1],
                          [0, 0, 0, -1],
                          [1, -1, -3 / (2 * h), 0],
                          [((2 * h + 3 * C * R) / (2 * R * h)), -((2 * h + 3 * C * R) / (2 * R * h)), 0, -1]])

        return A

    def get_right_side(self, sol, i, h):
        index_voltage = self.data_index
        index_phase = self.var_index

        fn_1 = sol[index_phase, i - 1] if i != 0 else 0  # phi+ - phi-
        fn_2 = sol[index_phase, i - 2] if i > 1 else 0  # phi+ - phi-

        if self.data_index[0] == 0:   # no V+
            vn_1 = - sol[index_voltage[1] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = - sol[index_voltage[1] - 1, i - 2] if i > 1 else 0  # V+ - V-
            vn_3 = - sol[index_voltage[1] - 1, i - 3] if i > 2 else 0  # V+ - V-
        elif self.data_index[1] == 0:  # no V-
            vn_1 = sol[index_voltage[0] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = sol[index_voltage[0] - 1, i - 2] if i > 1 else 0  # V+ - V-
            vn_3 = sol[index_voltage[0] - 1, i - 3] if i > 2 else 0  # V+ - V-
        else:
            vn_1 = sol[index_voltage[0] - 1, i - 1] - sol[index_voltage[1] - 1, i - 1] if i != 0 else 0  # V+ - V-
            vn_2 = sol[index_voltage[0] - 1, i - 2] - sol[index_voltage[1] - 1, i - 2] if i > 1 else 0  # V+ - V-
            vn_3 = sol[index_voltage[0] - 1, i - 3] - sol[index_voltage[1] - 1, i - 3] if i > 2 else 0  # V+ - V-

        v0 = (5 / 2) * vn_1 - 2 * vn_2 + (1 / 2) * vn_3
        phi_0 = (4 / 3) * fn_1 - (1 / 3) * fn_2 + (2 * h / 3) * v0
        # print('V0', v0, 'phi_0', phi_0, 'vn-1', vn_1, 'vn_2', vn_2, 'vn-3', vn_3, 'fn_1', fn_1, 'fn_2', fn_2)

        A = self.A
        C = self.c
        R = self.r

        rhs = (-(2 / h) * fn_1 + (1 / (2 * h)) * fn_2)
        Is = -A * np.sin(phi_0) + (2 * C / h) * vn_1 - (C / (2 * h)) * vn_2
        B = np.zeros(3) if 0 in self.loc else np.zeros(4)
        B[-1] = Is
        B[-2] = rhs
        return B

    def get_data(self, kind, t, sol):
        if kind == 'P':
            phase_index = self.var_index
            return sol[phase_index, :]
        else:
            return super().get_data(kind, t, sol)
