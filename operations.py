#Ahmed A.Allam & Ahmad Nader Adel & Eslam Wael Reda & Hazem Mohamed & Ahmad Mostafa El Matbaagy
import numpy as numb
import math


#Multiply MatrixA by MatrixB and return the result
#Error checking is done in the GUI
def MatrixMultiplication( MatrixA,MatrixB ):
   MatrixC=[]
   if len(MatrixA[0])==len(MatrixB):
     for h in range(len(MatrixA)):
        MatrixC.append([0] * len(MatrixB[0]))
     for i in range(len(MatrixA)):  
        for j in range (len(MatrixB[0])):
            for k in range(len(MatrixA[0])):
                MatrixC[i][j]=round(MatrixC[i][j]+MatrixA[i][k]*MatrixB[k][j], 4)
   return MatrixC


#This function inverts Matrix A and returns the result
def MatrixInverse( MatrixA):
   A=numb.array(MatrixA)
   x=numb.linalg.det(A)
   if (x==0):
     MatrixC=None
   else:  
    MatrixC=numb.linalg.inv(MatrixA) 
   return MatrixC


#This function checks if the dimension of a matrix is square to make sure we can perform the power method
def checkSquare(number):
    root = math.sqrt(number)
    if int( root+0.5 ) ** 2 == number:
        return True
    else:
        return False

#This functions takes the number of iterations, the matrix to calculate eigenpair for, and the initial values
#It returns EigenVector with the eigenValue appended at the end
def PowerMethod(noOfIterations, Matrix, initialValues):
         eigenValue = []
         eigenVector = []
         for i in range(noOfIterations):
            eigenVector = MatrixMultiplication(Matrix, initialValues)
            eigenValue = max(eigenVector)
            newEigenVector = [[]]
            newEigenVector[0] = [round(x[0] /  eigenValue[0],4) for x in eigenVector]
            for i in range(len(newEigenVector[0])):
                  initialValues[i] = [newEigenVector[0][i]]
                  

         initialValues.append(eigenValue)
         return initialValues


#This function returns the tranpose of a matrix
def transpose(Matrix):
   return [[Matrix[j][i] for j in range(len(Matrix))] for i in range(len(Matrix[0]))] 


#This function prints a matrix for debugging purposes    
def printMatrix(Matrix):
   for row in range(len(Matrix)):
      print(Matrix[row])

#This function returns the difference of 2 matrices
def subtractMatrix(MatrixA, MatrixB):
   result = [[0]*len(MatrixA) for i in range(len(MatrixA[0]))];  
   for row in range(len(MatrixA)):
      for column in range(len(MatrixA[0])):
         result[row][column] = MatrixA[row][column] - MatrixB[row][column]

   return result



#This function calculates the deflated matrix given the original matrix, and the eigen pair
def DeflatedMatrix(Matrix, eigenVector, eigenValue):
   result = 0
   for row in range(len(eigenVector)):
      for column in range(len(eigenVector[0])):
         result += eigenVector[row][column] ** 2
   number = eigenValue/result
   newMatrix = MatrixMultiplication(eigenVector, transpose(eigenVector))
   for row in range(len(newMatrix)):
      for column in range(len(newMatrix[0])):
         newMatrix[row][column] *= number
   return subtractMatrix(Matrix, newMatrix)





