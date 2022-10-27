from Objects.ComplexObjectBase import ComplexObjectBase


class NIJTL(ComplexObjectBase):
    """
        A Josephson transmission line without inductors
        Inputs:
        1 - input signal
        2 - output signal
        """
    def __init__(self, loc, N, ib_val=0.75, jj_c=1, jj_r=1, jj_a=1, jj_b=0, jj_c_c=1, jj_c_r=1, jj_c_a=0.7, jj_c_b=0):
        """
        A class constructor

        :param loc: nodes in a circuit to what the element is connected (zero is a ground)
        :param N: a length of a line (a number of Josephson junctions)
        :param ib_val: a value of current biases (in normalized current units)
        :param jj_c: a value of Josephson junction capacitances (in normalized capacitance units)
        :param jj_r: a value of Josephson junction resistances (in normalized resistance units)
        :param jj_a: a value of Josephson junction critical currents (in normalized Ic units)
        :param jj_b: a value of Josephson junction critical currents second harmonics (in normalized Ic units)
        """
        super().__init__(loc=loc)
        self.check_loc(loc, 2)

        # numeric parameters
        self.N = N
        self.ib_val = ib_val
        self.jj_a = jj_a
        self.jj_b = jj_b
        self.jj_c = jj_c
        self.jj_r = jj_r

        self.jj_c_a = jj_c_a
        self.jj_c_b = jj_c_b
        self.jj_c_c = jj_c_c
        self.jj_c_r = jj_c_r

        self.name = 'NIJTL'
        self.description = 'Josephson transmission line without L'

    def create_elements(self, sk):
        sk = [sk[0]] + sk[2:] + [sk[1]]

        # generate objects
        for i in range(self.N):
            # Josephson junction
            name = f'JJ_{i + 1}'
            self.add_JJ(name=name, loc=[sk[i], 0], c=self.jj_c, r=self.jj_r, A=self.jj_a, B=self.jj_b)

            # Current bias
            name = f'Ib_{i + 1}'
            self.add_ib(name=name, loc=[sk[i]], val=self.ib_val)

            # Inductor
            if i == self.N - 1:  # inductors are only between JJ's
                continue
            name = f'JJc_{i + 1}'
            self.add_JJ(name=name, loc=[sk[i], 0], c=self.jj_c_c, r=self.jj_c_r, A=self.jj_c_a, B=self.jj_c_b)
