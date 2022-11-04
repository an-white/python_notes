import unittest


class DemoTest(unittest.TestCase):
    D1 = {'a': 1, 'b': 2, 'c': [1, 2]}
    D2 = {'a': 1, 'b': 2, 'c': [3, 1]}

    def test_not_so_useful(self):
        """
        comparacion sencilla entre objetos, no hay detalle de la diferencia entre los mismos
        """
        self.assertTrue(self.D1 == self.D2)

    def test_useful(self):
        """
        muestra donde los objetos difieren entre si
        """
        self.assertDictEqual(self.D1, self.D2)


if __name__ == '__main__':
    unittest.main()
