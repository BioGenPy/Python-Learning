print("----------------------NumPy Array Indexing--------------------")

import numpy as np

aae = np.array([1,2,3,4,5])
print(".............Get the First element from the following array............")
print(aae[0])

print(".............Get the Second element from the following array............")
print(aae[1])

print(".............Get the Third element from the following array............")
print(aae[2])

print(aae[3])


aefs = np.array([[1,40,3,4,5],[6,7,8,9,10]])

print('2nd element on 1st row :', aefs[0,1])

print("Access the element on the 2nd row, 5th column:: 1,4")
print('5th element on 2nd row',aefs[1,3])


thirElemet = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(thirElemet[0,1,2])

print(".............Negative Indexing............")

ni = np.array([[1,2,3,4,5],[6,7,8,9,10] ])
print('Last element form 2nd dim : ',ni[1,-1])