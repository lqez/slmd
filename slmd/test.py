import os
import sys
import unittest
from slmd import sort_string
from .cmd import main


class TestSort(unittest.TestCase):

    def test_mandatory(self):
        self.assertEqual(True, True)

    def test_basic(self):
        asis = """
normal paragraph

- 2
  - C
  - A
    - 6
      indented text
    - 4
  - B
- 1
  - F
  - A

- k
- j

normal text
"""
        tobe = """
normal paragraph

- 1
  - A
  - F
- 2
  - A
    - 4
    - 6
      indented text
  - B
  - C

- j
- k

normal text
"""
        self.assertEqual(sort_string(asis), tobe)

    def test_descending(self):
        asis = """
* 1
* 3
* 2
"""
        tobe = """
* 3
* 2
* 1
"""
        self.assertEqual(sort_string(asis, [-1]), tobe)

    def test_1st_only(self):
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
  * 3
  * 2
  * 1
* 2
* 3
"""
        self.assertEqual(sort_string(asis, [1]), tobe)

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

    def test_case_sensitive(self):
        asis = """
- C
  - A
  - d
  - b
- b
  - Z
  - 12
  - a
- a
"""
        tobe = """
- a
- b
  - 12
  - a
  - Z
- C
  - A
  - b
  - d
"""
        self.assertEqual(sort_string(asis, case_sensitive=False), tobe)



class TestCmd(unittest.TestCase):
    def setUp(self):
        self.sample = 'fixtures/source.md'

        # Do not print out anything
        f = open(os.devnull, 'w')
        sys.stdout = f
        sys.stderr = f

    def test_run(self):
        try:
            main([])
        except SystemExit:
            pass

    def test_simple(self):
        argv = '{}'.format(self.sample)
        main(argv.split(' '))


if __name__ == '__main__':
    unittest.main()
