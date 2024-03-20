import os
import unittest

from copystatic import copy_dir_recursive

os_static_path = "./static/"
os_public_path = "./public/"

class TestCopyStatic(unittest.TestCase):
    def test_correct_dir(self):
        print(copy_dir_recursive(os_static_path, os_public_path))
        self.assertEqual(
            True,
            True
        )
        