import unittest
import sqlite3
import os
import MYtest_commands

from collections import OrderedDict
from datetime import datetime
from database import DatabaseManager

class Test_Barky(unittest.TestCase):
    def test_print_bookmarks(self):
        bookmark = print_bookmarks()
        self.assertEqual(message, message, msg=None)