import numpy as np
from Objects.ElementBase import ElementBase


class L(ElementBase):
    """
    Inductor
    """
    def __init__(self, loc, val):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param val: normalized inductance
        """
        super().__init__()
        self.check_loc(loc, 2)
        self.loc = loc
        self.val = val

        self.name = 'L'
        self.complex = False

        self.contains_current = True
        self.contains_variable = False

    def get_matrix_stamp(self, h):
        l = self.val
        loc = self.data_index

        if loc[0] == 0:  # no V+
            A = np.array([[0, -1],
                          [-1, -(3 * l) / (2 * h)]])
        elif loc[1] == 0:  # no V-
            A = np.array([[0, 1],
                          [1, -(3 * l) / (2 * h)]])
        else:
            A = np.array([[0, 0, 1],
                          [0, 0, -1],
                          [1, -1, -(3 * l) / (2 * h)]])

        return A

    def get_right_side(self, sol, i, h):
        loc = self.data_index
        index_current = self.current_index[0]
        l = self.val

        In_1 = sol[index_current, i - 1] if i > 0 else 0
        In_2 = sol[index_current, i - 2] if i > 1 else 0

        curr = -(2 * l / h) * In_1 + (l / (2 * h)) * In_2
        if 0 in loc:
            return np.array([0, curr])
        else:
            return np.array([0, 0, curr])

    def get_data(self, kind, t, sol):
        if kind == 'P':
            l = self.val
            return super().get_data('I', t, sol) * l
        else:
            return super().get_data(kind, t, sol)
