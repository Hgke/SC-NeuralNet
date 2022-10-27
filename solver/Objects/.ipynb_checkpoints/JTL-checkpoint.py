from Objects.ComplexObjectBase import ComplexObjectBase


class JTL(ComplexObjectBase):
    """
    A Josephson transmission line
    Inputs:
    1 - input signal
    2 - output signal
    """
    def __init__(self, loc, N, ib_val=0.75, l_val=3, jj_c=1, jj_a=1, jj_b=0):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param N: a length of a line (a number of Josephson junctions)
        :param ib_val: a value of current biases (in normalized current units)
        :param l_val: a value of inductances (in normalized inductance units)
        :param jj_c: a value of Josephson junction capacitances (in normalized capacitance units)
        :param jj_r: a value of Josephson junction resistances (in normalized resistance units)
        :param jj_a: a value of Josephson junction critical currents (in normalized Ic units)
        :param jj_b: a value of Josephson junction critical currents second harmonics (in normalized Ic units)
        """
        super().__init__(loc=loc)
        self.check_loc(loc, 2)

        self.N = N
        self.ib_val = ib_val
        self.l_val = l_val
        self.jj_c = jj_c
        self.jj_a = jj_a
        self.jj_r = 1/jj_a
        self.jj_b = jj_b

        self.name = 'JTL'
        self.description = 'Josephson transmission line'

    def create_elements(self, sk):
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'JJ{i + 1}'
            self.add_JJ(name=name, loc=[sk[i], 0], c=self.jj_c, A=self.jj_a, B=self.jj_b)

            # Current bias
            name = f'Ib{i + 1}'
            self.add_ib(name=name, val=self.ib_val, loc=[sk[i]])

            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'L{i + 1}'
            self.add_L(name=name, val=self.l_val, loc=[sk[i], sk[i+1]])
