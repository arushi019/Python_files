#Arushi Chauhan
#2016019
#Section-A
#Kunal Dahiya
#2016156
#Section-A
from a4 import *
import unittest
class sample(unittest.TestCase):
    def testMatrix(self):
        self.assertEqual(MatrixRank([[1,2,3,9],[0,0,1,5],[0,1,0,9]]),2)
        self.assertEqual(MatrixRank([[0,2,3,0],[0,0,1,5],[0,1,0,9]]),0)
        self.assertEqual(MatrixRank([[9,6,3,4],[0,0,4,5],[2,1,0,8]]),2)
        self.assertEqual(MatrixRank([[6,7,2,9],[3,2,1,8],[5,9,1,8]]),3)
        self.assertEqual(MatrixRank([[6,8,2,2],[3,4,1,1],[5,9,1,8]]),2)
if __name__=='__main__':
    unittest.main()
