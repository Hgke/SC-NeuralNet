import math
import numpy as np
from scipy.integrate import simpson
from Objects.ElementBase import ElementBase


class MutualInductance(ElementBase):
    """A mutual inductance object"""
    def __init__(self, loc, L1, L2, k):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param L1: a first inductance
        :param L2: a second inductance
        :param k: a mutual inductance parameter, M = k * sqrt(L1 * L2)
        """
        super().__init__()
        self.loc = loc
        self.check_loc(loc, 4)
        self.name = 'MutualInductance'
        self.complex = False

        self.L1 = L1
        self.L2 = L2
        self.M = k * math.sqrt(L1 * L2)

        self.contains_current = True
        self.contains_variable = False
        self.double_voltage = True
        self.double_current = True

    @staticmethod
    def _remove_row_and_col(matr, rows, cols):
        return np.delete(np.delete(matr, cols, axis=1), rows, axis=0)

    def get_matrix_stamp(self, h):
        L1 = self.L1
        L2 = self.L2
        M = self.M

        base_matrix = np.array([[0, 0, 0, 0, 1, 0],
                                [0, 0, 0, 0, -1, 0],
                                [0, 0, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0, -1],
                                [1, -1, 0, 0, -(3 * L1) / (2 * h), -(3 * M) / (2 * h)],
                                [0, 0, 1, -1, -(3 * M) / (2 * h), -(3 * L2) / (2 * h)]])

        to_remove = np.nonzero(np.array(self.loc) == 0)
        base_matrix = self._remove_row_and_col(base_matrix, to_remove, to_remove)

        return base_matrix

    def get_right_side(self, sol, i, h):
        L1 = self.L1
        L2 = self.L2
        M = self.M
        index_current = self.current_index

        I1_n1 = sol[index_current[0], i - 1] if i != 0 else 0
        I2_n1 = sol[index_current[1], i - 1] if i != 0 else 0
        I1_n2 = sol[index_current[0], i - 2] if i > 1 else 0
        I2_n2 = sol[index_current[1], i - 1] if i > 1 else 0

        right_side = np.zeros(np.count_nonzero(self.loc) + 2)
        rhs1 = -(2 * L1 / h) * I1_n1 + (L1 / (2 * h)) * I1_n2 - (2 * M / h) * I2_n1 + (M / (2 * h)) * I2_n2
        rhs2 = -(2 * L2 / h) * I2_n1 + (L2 / (2 * h)) * I2_n2 - (2 * M / h) * I1_n1 + (M / (2 * h)) * I1_n2

        right_side[-2] = rhs1
        right_side[-1] = rhs2

        return right_side

    def get_data(self, kind, t, sol):
        error = 'Please use format like <kind><number of coil>, for example, "I1" or "V2"'
        if kind in ['I', 'V', 'P']:
            raise ValueError(f'For mutual inductances, please specify one of two coils (use {kind}1 or {kind}2)')
        try:
            idx = int(kind[1]) - 1
        except ValueError:
            raise ValueError(error)

        if kind[0] == 'P':
            voltage = self.get_data('V', t, sol)
            new_data = np.zeros_like(t)
            for i, ti in enumerate(t):
                new_data[i] = simpson(voltage[:i + 1], t[:i + 1])
            return new_data
        elif kind[0] == 'V':
            volt_index = self.data_index
            if volt_index[idx * 2] == 0:  # no V+
                return - sol[volt_index[idx * 2 + 1] - 1, :]
            elif volt_index[idx * 2 + 1] == 0:  # no V-
                return sol[volt_index[idx * 2] - 1, :]
            else:
                return sol[volt_index[idx * 2] - 1, :] - sol[volt_index[idx * 2 + 1], :]
        elif kind[0] == 'I':
            curr_index = self.current_index
            return sol[curr_index[idx], :]
        else:
            raise ValueError('Invalid data kind\n' + error)
