import unittest
from mdls import sort_string


class TestSort(unittest.TestCase):

    def test_mandatory(self):
        self.assertEqual(True, True)

    def test_basic(self):
        asis = """
* 1
* 3
* 2
"""
        tobe = """
* 1
* 2
* 3
"""
        self.assertEqual(sort_string(asis), tobe)

    def test_2nd_only(self):
        asis = """
* 1
  * 3
  * 2
  * 1
* 3
* 2
"""
        tobe = """
* 1
  * 1
  * 2
  * 3
* 3
* 2
"""
        self.assertEqual(sort_string(asis, [0, 1]), tobe)

    def test_3rd_only(self):
        asis = """
* 2
  * 3
  * 2
  * 1
    * B
    * A
    * C
* 3
* 1
"""
        tobe = """
* 2
  * 3
  * 2
  * 1
    * A
    * B
    * C
* 3
* 1
"""
        self.assertEqual(sort_string(asis, [0, 0, 1]), tobe)

if __name__ == '__main__':
    unittest.main()
