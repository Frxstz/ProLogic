"""
Linear Equation Program
Intro to Pro Logic
Github:https://github.com/Frxstz/ProLogic
Author @Frxstz
"""
import numpy as np

def rows():
    num_rows = int(input("How many Rows do you want? "))
    return num_rows

def colu():
    num_colum = int(input("How many Collums do you want? "))
    return num_colum

matcount = 0
def rematrix(matcount):
    prod = np.prod(breaklist[matcount])
    return prod

fincount = 0
def finalMatCre(fincount, breaklist,numSets):
    print(f"array #{fincount} is an {breaklist[fincount]} grid. (Expecting {numSets[fincount]} numbers) ")
    fin = input("Please Input your numbers in order as such: \n C11 C12 C13 ... \n C21 C22 C23 ... \n C31 C32 C33 ... \n Please Input your numbers Now (Seperated by a space)")
    array_sets.append(fin)
    return fin

splitcount = 0 
def matsplit(splitcount):
    prod = np.prod(numSets[splitcount])
    return prod

taco = []
numSets = []
array_sets = []

Y = int(input("How many Matrix's you want? (Max 2 for now) "))
X = 0
count = 0
while True:
    if X < Y:
        X = X + 1
        taco.append(rows())
        taco.append(colu())
    else:
        mid = (taco[1:-1])
        first = mid[0]
        if all(i == first for i in mid):
            print("These matrices can be multiplied.")
            breaklist = np.array_split(taco, Y)
            print(breaklist)
            while True:
                if count < Y :
                    numSets.append(rematrix(matcount))
                    matcount = matcount + 1
                    count = count + 1
                else:
                    if fincount < matcount:
                        finalMatCre(fincount,breaklist,numSets)
                        fincount = fincount + 1
                    else:
                        while True:
                            if splitcount < Y:
                                print(matsplit(splitcount))
                                splitcount = splitcount + 1
                            else:
                                print("bruh")
                                break
                        break
        else:
            print('These Matricies can not be multiplied')
            break
        break