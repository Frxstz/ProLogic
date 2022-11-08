"""
Linear Equation Program
Intro to Pro Logic
Github:https://github.com/Frxstz/ProLogic
Author @Frxstz
"""
import numpy as np

#rows inputs, Runs on Y value
def rows():
    num_rows = int(input(f"How many Rows do you want in matrix {X}? "))
    return num_rows
#column inputs, Runs on Y value
def colu():
    num_colum = int(input(f"How many Collums do you want in matrix {X}? "))
    return num_colum
#Seeing how many #'s are expected in each Matrix
matcount = 0
def rematrix(matcount):
    prod = np.prod(breaklist[matcount])
    return prod
#User Input for each Matrix, Sends it to array_sets
fincount = 0
def finalMatCre(fincount, breaklist,numSets):
    print(f"array # {fincount} is an {breaklist[fincount]} grid. (Expecting {numSets[fincount]} numbers) ")
    fin = input("Please Input your numbers in order as such: \n C11 C12 C13 ... \n C21 C22 C23 ... \n C31 C32 C33 ... \n Please Input your numbers Now (Seperated by a space)")
    array_sets.append(fin)
    return fin

#List Creation
rowColu = []
numSets = []
array_sets = []
nums = []
nums2 = []


# Y = int(input("How many Matrix's you want? (Max 2 for now) "))
Y = (int(2))    #For this code, you can only multiply two matrices. Will update to do as many as you want
print("Multiplying two Matrices")
X = 0
count = 0
while True:
    if X < Y:   #Repeating as many times as you have Matrices
        X = X + 1
        #def rows(): num_rows = int(input() return num_rows Impacted by Y
        rowColu.append(rows())
        #def colu(): num_colu = int(input() return num_colu Impacted by Y
        rowColu.append(colu())
    else:
        mid = (rowColu[1:-1])
        first = mid[0]  #Reason I cant do 3 Matrices
        if all(i == first for i in mid):    #Well Defined Check
            print("These matrices can be multiplied.")
            breaklist = np.array_split(rowColu, Y)  #Spliting the main List into each matrix dimensions
            while True:
                if count < Y :
                    #Rematrix into Numsets Operation
                    numSets.append(rematrix(matcount)) 
                    matcount = matcount + 1
                    count = count + 1
                else:
                    if fincount < matcount:
                        #User input for each Matrix. FinalMatrixCreation
                        finalMatCre(fincount,breaklist,numSets)
                        fincount = fincount + 1
                    else:
                        #Seperating into Matrix 1-2
                        array1 = array_sets[0]
                        array2 = array_sets[1]
                        #turning the string int seperate numbers
                        for num in array1.split(" "):
                            nums.append(int(num))
                        for num in array2.split(" "):
                            nums2.append(int(num))
                        #Reshaping into the arrays for .matmul
                        aNums = np.array(nums).reshape(breaklist[0])
                        aNums2 = np.array(nums2).reshape(breaklist[1])
                        final_ans = np.matmul(aNums,aNums2)
                        print(final_ans) # FINAL LETS GOOO!!!!!!!!!
                        break
        else:
            print('These Matricies can not be multiplied')
            break
        break
