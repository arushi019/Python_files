import unittest
from a4 import *

class testpoint(unittest.TestCase):

	def testMatrixRank(self):
		self.assertEqual(MatrixRank([[3,3,4,5],[1,1,0,3],[1,1,-1,3],[-1,2,4,2],[6,1,-1,3]]),2)
	def testMatrixRank1(self):
		self.assertEqual(MatrixRank([[1,2,3,2],[3,5,7,5],[3,3,3,3],[4,8,0,1]]),3)
	def testMatrixRank2(self):
		self.assertEqual(MatrixRank([[1,2,3],[11,15,12],[9,2,4]]),3)
	def testMatrixRank3(self):
		self.assertEqual(MatrixRank([[1,23,15],[2,46,30],[3,69,45]]),1)
	def testMatrixRank4(self):
		self.assertEqual(MatrixRank([[4,8,0],[44,23,1],[9,17,1],[54,41,3],[2,22,20]]),3)

	def testswapRows(self):
		A=[[2,8,6,7,2],[3,2,1,5,99],[3,54,23,77,8],[88,23,1,1,0]]
		swapRow(A,1,0)		
		self.assertEqual(A,[[3,2,1,5,99],[2,8,6,7,2],[3,54,23,77,8],[88,23,1,1,0]])
		
	def testswapRows1(self):
		A=[[3,2,1,5,99],[2,8,6,7,2],[3,54,23,77,8],[88,23,1,1,0]]
		swapRow(A,3,3)		
		self.assertEqual(A,[[3,2,1,5,99],[2,8,6,7,2],[3,54,23,77,8],[88,23,1,1,0]])
		
	def testswapRows2(self):
		A=[[3,2,1,5,99],[2,8,6,7,2],[3,54,23,77,8],[88,23,1,1,0]]
		swapRow(A,2,1)		
		self.assertEqual(A,[[3,2,1,5,99],[3,54,23,77,8],[2,8,6,7,2],[88,23,1,1,0]])
	
	
	def testRowTransformation(self):
		A=[[1,2,1],[-2,-3,1],[3,5,0]]
		Row_Transformation(A,2,0,1)		
		self.assertEqual(A,[[1,2,1],[0,1,3],[3,5,0]])
		
	def testRowTransformation1(self):
		A=[[1,2,1],[0,1,3],[3,5,0]]
		Row_Transformation(A,-3,0,2)		
		self.assertEqual(A,[[1,2,1],[0,1,3],[0,-1,-3]])
		
	def testRowTransformation2(self):
		A=[[1,2,1],[0,1,3],[0,-1,-3]]
		Row_Transformation(A,1,1,2)		
		self.assertEqual(A,[[1,2,1],[0,1,3],[0,0,0]])
	
if __name__=='__main__':
	
	unittest.main()
