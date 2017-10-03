import unittest

from he.bv.basic import BVTensor
from he.keys import KeyPair
import numpy as np


class addition_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(addition_test, self).__init__(*args, **kwargs)
        self.keys = KeyPair()
        self.keys.generate()

    def test_add(self):
        a = BVTensor(self.keys.pk(), np.asarray([40,2]), True, self.keys.sk())

        # integers only, for now!
        b = a + 2
        # TODO decrypt, check plaintext result


class multiplication_test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(multiplication_test, self).__init__(*args, **kwargs)
        self.keys = KeyPair()
        self.keys.generate()

    def test_mul_by_scalar(self):
        a = BVTensor(self.keys.pk(), np.asarray([21]), True, self.keys.sk())

        # Integers only, for now!
        b = a * 2
        # TODO decrypt, check plaintext result

if __name__ == "__main__":
    unittest.main()