import unittest


class EnvironmentTest(unittest.TestCase):
    def test_sanity(self):
        self.assertEquals(1, 1, "environment does not make sense")

if __name__ == '__main__':
    unittest.main()
