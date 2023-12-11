#!/usr/bin/python3
""" test_pep8 """

import unittest
import pycodestyle
import os


class TestPycodestyle(unittest.TestCase):
    """Test for PEP-8"""

    def test_pep8(self):
        """Test for PEP-8"""
        style = pycodestyle.StyleGuide(quit=True)
        # Get a list of all Python files in the project
        python_files = [f for f in self.get_all_files() if f.endswith('.py')]
        results = style.check_files(python_files)
        self.assertEqual(results.total_errors, 0,
                         "Found pycodestyle errors.")
        for result in results.messages:
            print(result)

    def get_all_files(self):
        """Get a list of all files in the project."""
        files = []
        for root, dirs, filenames in os.walk('.'):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files


if __name__ == '__main__':
    unittest.main()
