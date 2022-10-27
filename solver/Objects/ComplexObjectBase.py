from Objects.ElementBase import *
from Objects.JJ import JJ
from Objects.Ib import Ib
from Objects.L import L
from Objects.R import R
from Objects.C import C
from Objects.Pulses import Pulses


class ComplexObjectBase(ElementBase):
    """A base abstract class for complex objects (subcircuits)"""
    def __init__(self, loc):
        """
        A class constructor.
        MUST be subclassed in child classes.
        A subcircuit name and a parameter N (number of nodes in a subcircuit) MUST be set there.

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        """
        super().__init__()

        self.loc = loc
        # must be set in a child class constructor
        self.N = None
        self.name = None

        self.complex = True
        self._new_names_obj = []

    def add_JJ(self, name, c, A, B, loc):
        """
        Adds a Josephson junction (JJ) to a subcircuit
        :param name: JJ name
        :param c: JJ capacitance (in normalized capacitance units)
        :param r: JJ resistance (in normalized resistance units)
        :param A: JJ critical current (in normalized Ic units)
        :param B: JJ critical current second harmonics (in normalized Ic units)
        :param loc: JJ location in a sub circuit (use sk array passed to crreate_elements function)
        """
        new_obj = JJ(loc=loc, c=c, A=A, B=B)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_ib(self, name, val, loc):
        """
        Adds a constant current source to a subcircuit
        :param name: current source name
        :param val: current amplitude (in normalized current units)
        :param loc: current source location in a subcircuit (use sk array passed to crreate_elements function)
        """
        new_obj = Ib(loc=loc, val=val)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_L(self, name, val, loc):
        """
        Adds an inductor to a subcircuit
        :param name: inductor name
        :param val: inductance (in normalized inductance units)
        :param loc: inductor location in a subcircuit (use sk array passed to crreate_elements function)
        """
        new_obj = L(loc=loc, val=val)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_R(self, name, r, loc):
        """
        Adds an resistor to a subcircuit
        :param name: resistor name
        :param r: resistance (in normalized resistance units)
        :param loc: resistor location in a subcircuit (use sk array passed to crreate_elements function)
        """
        new_obj = R(loc=loc, r=r)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_C(self, name, c, loc):
        """
        Adds a capacitor to a subcircuit
        :param name: capacitor name
        :param c: capacitance (in normalized capacitance units)
        :param loc: capacitor location in a subcircuit (use sk array passed to crreate_elements function)
        """
        new_obj = C(loc=loc, c=c)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def add_Pulses(self, name, loc, connect, type_p, t0, A, D, T, w):
        """
        Adds a pulse current source to a subcircuit
        :param name: current source name
        :param connect: not implemented yet, use 'current'
        :param type_p: 'Gauss' for a gaussian pulse, or 'Sin' for a sinusoidal wave
        :param t0: pulse time (for Gaussian pulse)
        :param A: pulse amplitude (for Gaussian pulse) (in normalized current units)
        :param D: pulse width
        :param T: pulses period
        :param w: sinusoidal wave frequency (for sinusoidal waves)
        :param loc: current source location in a subcircuit (use sk array passed to crreate_elements function)
        """
        new_obj = Pulses(loc=loc, connect=connect, type_p=type_p, t0=t0, A=A, D=D, T=T, w=w)
        new_obj.name = f'{self.name}_{name}'
        self._new_names_obj.append(new_obj)

    def create_elements(self, sk):
        """
        MUST be implemented in child classes.
        Creates all elements in a subcircuit.

        :param sk: indices of subcircuit nodes (you must use them as indices for added elements).
        The number of such indices is equal to self.N (MUST be set in a child class constructor)
        If a circuit contains k inputs, first k indices are the inputs
        :return:
        """
        raise NotImplementedError

    def unzip(self):
        """
        Unpacks a complect object (creates child elements).
        Called by FunctionCompiler, DO NOT override this method in child classes.
        :return:
        """
        sk = self.data_index
        self.create_elements(sk)

        return self._new_names_obj

    def get_data(self, kind, t, sol):
        """
        A stub for get_data() for subcircuits, because the term 'data' dor a subcircuit is not defined.
        You may define it for your subcircuit by overriding this method in child classes.
        """
        # this may be overridden in a child class, if you define any data for a subcircuit
        raise ValueError('Data for this complex object are undefined.\n'
                         'To get data of a complex object (a subcircuit), get its particular element '
                         'from FunctionCompiler.object_dict and then use its get_data method')
