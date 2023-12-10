#!/usr/bin/pyhton3
""" test_pep8 """

import unittest
import pycodestyle


class TestPycodestyle(unittest.TestCase):
    """Test for PEP-8"""

    def test_pep8(self):
        """Test for PEP-8"""
        style = pycodestyle.StyleGuide(quit=True)
        results = style.check_files(['models'])
        self.assertEqual(results.total_errors, 0,
                         "Found pycodestyle errors.")
        for result in results.messages:
            print(result)

if __name__ == '__main__':
    unittest.main()
