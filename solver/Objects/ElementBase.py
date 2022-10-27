import numpy as np
import warnings


class ElementBase:
    """A base abstract class for circuit non-complex elements"""
    def __init__(self):
        self.data_index = None
        self.current_index = []
        self.var_index = None
        self.name = None
        self.complex = False

        self.contains_current = False
        self.contains_variable = False
        self.double_current = False

    def get_matrix_stamp(self, h):
        """
        MUST be implemented in child classes.

        Returns a matrix stamp for this element.

        A stamp must have a correct size, depending on contains_current, contains_variable, and double_current
        parameters and grounded nodes (rows and columns corresponding to a grounded node must be removed).

        :param h: an integration time step
        :return: a matrix stamp (as a 2D numpy array).
        """
        raise NotImplementedError

    def get_right_side(self, sol, i, h):
        """
        MUST be implemented in child classes.

        Returns a right side for matrix-form equation for this element.

        :param sol: a solution array (as is on a current step)
        :param i: a number of a current integration step
        :param h: an integration time step size
        :return: a right side (as an 1D numpy array)
        """
        raise NotImplementedError

    def check_loc(self, loc, len_required):
        """
        Checks the element location specified by user

        :param loc: user-specified location
        :param len_required: a required length of this location
        :return: True if everything is correct, False otherwise
        """
        if np.all(np.array(loc) == 0):
            warnings.warn(f'{self.name} is grounded at each output')

        if len(loc) != len_required:
            raise ValueError(f'Number of connections for {self.name} is {len_required},'
                             f' but actually {len(loc)} was specified')

    def get_data(self, kind, t, sol):
        """
        Gets the simulation result for this element

        :param kind: data kind: 'P' - phase; 'V' - voltage; 'I' - current
        :param t: original time array passed to FunctionCompiler constructor
        :param sol: solution array returned by FunctionCompiler.solve() method
        :return: 1-D data array
        """
        if kind == 'V':  # return V+ - V-
            voltage_index = self.data_index
            if voltage_index[0] == 0:  # V+ is missing
                return -sol[voltage_index[1] - 1, :]
            elif voltage_index[1] == 0:  # V- is missing
                return sol[voltage_index[0] - 1, :]
            else:  # everything is present
                return sol[voltage_index[0] - 1, :] - sol[voltage_index[1] - 1, :]
        elif kind == 'I':
            current_index = self.current_index
            return sol[current_index[0], :]
        else:
            raise ValueError(f'Data kind {kind} is not supported')
