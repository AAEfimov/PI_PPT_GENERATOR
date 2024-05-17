"""
test_addphoto.py
test addphoto module
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import os

import addphoto
import unittest


class TestAddphoto(unittest.TestCase):
    def test_get_images(self):
        filenames = addphoto.get_images("Test", 1)
        image_path = os.path.join("images", filenames[0])
        self.assertTrue(os.path.exists(image_path))
        os.remove(image_path)
        os.rmdir("images")
