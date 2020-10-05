import operations
import tkinter as tk
from tkinter import ttk
import math


#This creates the main window, with the title Power Method, and dimensions: width = 800 and height = 700
root = tk.Tk()
root.title("Power Method")
root.geometry("800x700")

#This creates a label to prompt user to enter initial values
label1 = ttk.Label(root, text = "Enter the initial values:(seperate numbers by a space)")
label1.grid(row = 0, column = 0, sticky='W')

#This creates an entry box for user to enter initial values
initValues = ttk.Entry(root, width = 25)
initValues.grid(row = 1, column = 0, sticky='W')

#This creates a guide for user to enter initial values in the form of x x x
exampleLabel = tk.Label(root, text = "For example: 1 1 1")
exampleLabel.grid(row =1, column = 1, sticky = 'W')

#This creates a label to prompt user to enter the number of iterations
label2 = ttk.Label(root, text = "Enter the number of iterations:")
label2.grid(row = 2, column = 0, sticky='W')

#This creates an entry box for user to enter number of iterations
iterations = ttk.Entry(root, width = 5)
iterations.grid(row = 3, column = 0, sticky='W')

#This creates a label to prompt user to enter a square matrix
label3 = ttk.Label(root, text = "Enter your square matrix:")
label3.grid(row = 4, column = 0, sticky='W')

#This creates a label to prompt user to enter a square matrix
label4 = ttk.Label(root, text = "(Enter the numbers in the form of an array where numbers are seperated by a space)")
label4.grid(row = 5, column = 0, sticky='W')


#This creates an entry box for the user to enter the matrix 
matrix = tk.Text(root ,width=40, height = 10)
matrix.grid(row = 6, column = 0, sticky = 'W')

#This creates a label as an example to guide  the user on how to enter the matrix
exampleLabel = tk.Label(root, text = "For example: \n 1 1 1 \n 1 1 1 \n1 1 1\n or \n1 1 1 1 1 1 1 1 1")
exampleLabel.grid(row =6, column = 1, sticky = 'W')

#This function takes the input, makes sure there are no un-permitted characters,
#creates a matrix out of the input, calculates the largest eigenpair and displays to the user
def calculateHighest():
    global iterations, matrix, initValues
    try:
        noOfIterations = iterations.get() #get number of iterations
        matrixOfNumbers = matrix.get('1.0', "end") #get matrix
        initial = initValues.get().split() #create an array of initial values
        initialMatrix = [[float(x)] for x in initial]  
        array = matrixOfNumbers.split()
        intArray = [float(item) for item in array] #turn array into matrix
        
       
        if not (noOfIterations and matrixOfNumbers and initial) or array == []: #If any of the input fields are left empty
            #create a new window with the error message
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "Make sure all the fields have input")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return     
        if operations.checkSquare(len(intArray)): #check if the matrix is a square
            dimension = int(math.sqrt(len(intArray)))
            TwoDArray = [[None for x in range(dimension)] for y in range(dimension)]
            
            if dimension != len(initialMatrix): #check if initial values don't match the dimenstion of the matrix 
                errorWindow = tk.Toplevel()
                errorLabel = ttk.Label(errorWindow, text = "No of Matrix columns must match no of row in initial values")
                okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
                errorLabel.pack()
                okButton.pack()
                return   
            counter = 0

            #This turns the array into a matrix
            for i in range(0,dimension ):
                for j in range(0, dimension) :
                    TwoDArray[i][j] = intArray[counter]  
                    counter += 1

            result = operations.PowerMethod(int(noOfIterations), TwoDArray , initialMatrix)
            
            #This makes a new window to display the eigenpair
            resultWindow = tk.Toplevel()
            resultWindow.title("Result")
            resultWindow.geometry("200x200")
            
            eigenVectorLabel = tk.Label(resultWindow, text = "eigenvector is ")
            eigenVectorLabel.grid(row = 0, column = 0)
            
            #display each row of the eigenvector on a new row
            firstAvailableLength = 1
            for i in range(len(result)-1):
                newLabel = tk.Label(resultWindow, text = str(result[i]))  
                newLabel.grid(row = firstAvailableLength, column = 0)
                firstAvailableLength += 1        

            newLabel = tk.Label(resultWindow, text = "eigenvalue is ")
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            newLabel = tk.Label(resultWindow, text = str(result[len(result)-1]))
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            
            #Creates Ok button
            okButton = ttk.Button(resultWindow, text = "Ok", command = resultWindow.destroy)
            okButton.grid(row = firstAvailableLength, column = 0)
            
            
            
        #Creates an error message to prompt the user to enter square matrix
        else:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please enter a square matrix")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 
            
    except:
        #This code handles un permitted characters by displaying an error message to the user
        errorWindow = tk.Toplevel()
        errorLabel = ttk.Label(errorWindow, text = "please  enter only numbers")
        okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
        errorLabel.pack()
        okButton.pack()
        return 


#This function has the exact same flow as calculateHighest except it inverts the matrix before passing it to the PowerMethod function
def calculateLowest():
    global iterations, matrix, initValues
    try:
        noOfIterations = iterations.get()
        matrixOfNumbers = matrix.get('1.0', "end")
        initial = initValues.get().split()
        initialMatrix = [[float(x)] for x in initial]

        array = matrixOfNumbers.split()
        intArray = [float(item) for item in array]
        if not (noOfIterations and matrixOfNumbers and initial) or array == []:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "Make sure all the fields have input")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return     
        if operations.checkSquare(len(intArray)):
            dimension = int(math.sqrt(len(intArray)))
            TwoDArray = [[None for x in range(dimension)] for y in range(dimension)]
            if dimension != len(initialMatrix):
                errorWindow = tk.Toplevel()
                errorLabel = ttk.Label(errorWindow, text = "No of Matrix columns must match no of row in initial values")
                okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
                errorLabel.pack()
                okButton.pack()
                return   
            counter = 0
            for i in range(0,dimension ):
                for j in range(0, dimension) :
                    TwoDArray[i][j] = intArray[counter] 
                    counter += 1

            TwoDArray = operations.MatrixInverse(TwoDArray)

            result = operations.PowerMethod(int(noOfIterations), TwoDArray , initialMatrix)
            
            
            resultWindow = tk.Toplevel()
            resultWindow.title("Result")
            resultWindow.geometry("200x200")
            
            eigenVectorLabel = tk.Label(resultWindow, text = "eigenvector is ")
            eigenVectorLabel.grid(row = 0, column = 0)
            firstAvailableLength = 1
            for i in range(len(result)-1):
                newLabel = tk.Label(resultWindow, text = str(result[i]))  
                newLabel.grid(row = firstAvailableLength, column = 0)
                firstAvailableLength += 1        

            newLabel = tk.Label(resultWindow, text = "eigenvalue is ")
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            newLabel = tk.Label(resultWindow, text = str(result[len(result)-1]))
            newLabel.grid(row = firstAvailableLength, column = 0)
            firstAvailableLength += 1
            
            
            okButton = ttk.Button(resultWindow, text = "Ok", command = resultWindow.destroy)
            
            okButton.grid(row = firstAvailableLength, column = 0)
            
            
            
        
        else:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please enter a square matrix")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 
            
    except:
        #failure code
        errorWindow = tk.Toplevel()
        errorLabel = ttk.Label(errorWindow, text = "please make sure you enter only numbers")
        okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
        errorLabel.pack()
        okButton.pack()
        return 


#This function has the same flow as calculateHighest but it calls calculateDeflatedMatrix and displays the deflated matrix instead of displaying eigen pair
def calculateDeflatedMatrix():
    global iterations, matrix, initValues
    try:
        noOfIterations = iterations.get()
        matrixOfNumbers = matrix.get('1.0', "end")
        initial = initValues.get().split()
        initialMatrix = [[float(x)] for x in initial]
        array = matrixOfNumbers.split()
        intArray = [float(item) for item in array]
        if not (noOfIterations and matrixOfNumbers and initial) or array == []:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "Make sure all the fields have input")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return     
        
        if operations.checkSquare(len(intArray)):
            dimension = int(math.sqrt(len(intArray)))
            TwoDArray = [[None for x in range(dimension)] for y in range(dimension)]
            if dimension != len(initialMatrix):
                errorWindow = tk.Toplevel()
                errorLabel = ttk.Label(errorWindow, text = "No of Matrix columns must match no of row in initial values")
                okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
                errorLabel.pack()
                okButton.pack()
                return   
            counter = 0
            for i in range(0,dimension ):
                for j in range(0, dimension) :
                    TwoDArray[i][j] = intArray[counter]  
                    counter += 1
            result = operations.PowerMethod(int(noOfIterations), TwoDArray , initialMatrix)
            operations.printMatrix(initialMatrix[0:len(initialMatrix)-2])



            deflatedMatrix = operations.DeflatedMatrix(TwoDArray, initialMatrix[0:len(initialMatrix)-1], result[len(result)-1][0])

            
            
            
            resultWindow = tk.Toplevel()
            resultWindow.title("Result")
            resultWindow.geometry("400x400")
            
            eigenVectorLabel = tk.Label(resultWindow, text = "Deflated Matrix")
            eigenVectorLabel.grid(row = 0, column = 0)
            firstAvailableLength = 1
            for i in range(len(result)-1):
                newLabel = tk.Label(resultWindow, text = str(deflatedMatrix[i]))  
                newLabel.grid(row = firstAvailableLength, column = 0)
                firstAvailableLength += 1        

            
            okButton = ttk.Button(resultWindow, text = "Ok", command = resultWindow.destroy)
            
            okButton.grid(row = firstAvailableLength, column = 0)
            
            
            
        
        else:
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please enter a square matrix")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 
                
    except:
            #failure code
            errorWindow = tk.Toplevel()
            errorLabel = ttk.Label(errorWindow, text = "please make sure you enter only numbers")
            okButton = ttk.Button(errorWindow, text = "Ok", command = errorWindow.destroy)
            errorLabel.pack()
            okButton.pack()
            return 






#This creates a button to calculate largest eigen pair
calculateLargest = tk.Button(root, text = "Calculate largest eigen pair ", command = calculateHighest)
calculateLargest.grid(row = 7, column = 0, sticky = 'W')

#This creates a button to calculate smallest eigen pair
calculateSmallest = tk.Button(root, text = "Calculate smallest eigen pair", command = calculateLowest)
calculateSmallest.grid(row = 8, column = 0, sticky = 'W')

##This creates a button to calculate deflated matrix
calculateDeflated = tk.Button(root, text = "Calculate Deflated Matrix", command = calculateDeflatedMatrix)
calculateDeflated.grid(row = 9, column = 0, sticky = 'W')

#This creates a button to exit the app
exit = tk.Button (root, text = "Exit", command = root.destroy)
exit.grid(row = 10, column = 0 , sticky = 'W')


root.mainloop()

