"""
test_gpt.py
test gpt module
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import unittest

import gpt


class TestGpt(unittest.TestCase):
    def test_sber(self):
        retval = gpt.gpt_summarise("test", 0)
        self.assertTrue(isinstance(retval, str))

    def test_llama(self):
        retval = gpt.gpt_summarise("test", 1)
        self.assertTrue(isinstance(retval, str))

    def test_wrong(self):
        retval = gpt.gpt_summarise("test", 999)
        self.assertEqual(retval, "Wrong Model")
