import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Dungeon import *

class TestDungeon(unittest.TestCase):

    def test_something(self):
        pass
        
        
if __name__ =='__main__':
    unittest.main()