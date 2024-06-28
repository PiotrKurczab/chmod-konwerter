import unittest
import chmodconverter_functions as chmodconverter

class TestChmodConverter(unittest.TestCase):
    def test_symbolic_to_numeric(self):
        self.assertEqual("777", chmodconverter.symbolic_to_numeric("rwxrwxrwx"))
        self.assertEqual("770", chmodconverter.symbolic_to_numeric("rwxrwx---"))
        self.assertEqual("700", chmodconverter.symbolic_to_numeric("rwx------"))
        self.assertEqual("400", chmodconverter.symbolic_to_numeric("r--------"))
        self.assertEqual("444", chmodconverter.symbolic_to_numeric("r--r--r--"))
        self.assertEqual("000", chmodconverter.symbolic_to_numeric("---------"))

    def test_numeric_to_symbolic(self):
        self.assertEqual("rwxrwxrwx", chmodconverter.numeric_to_symbolic("777"))
        self.assertEqual("rwxrwx---", chmodconverter.numeric_to_symbolic("770"))
        self.assertEqual("rwx------", chmodconverter.numeric_to_symbolic("700"))
        self.assertEqual("r--------", chmodconverter.numeric_to_symbolic("400"))
        self.assertEqual("r--r--r--", chmodconverter.numeric_to_symbolic("444"))
        self.assertEqual("---------", chmodconverter.numeric_to_symbolic("000"))

if __name__ == '__main__':
    unittest.main()