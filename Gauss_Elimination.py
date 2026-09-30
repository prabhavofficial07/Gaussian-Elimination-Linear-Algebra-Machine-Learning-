##Solve Matrices Of The Form Ax = B And Find x
import numpy as np
def Gauss_ell(A,B):
    # check if Enetred Matrix is correct form or not 
    if (A.shape[0] == A.shape[1]) and (B.shape[1] == 1 and B.shape[0]==A.shape[0]):


        # Making Augmented Matrix
        a = np.concatenate((A,B),dtype = float,axis = 1)

        # swapping Rows Largest up smallest down by col  as pivot
        for i in range (A.shape[0]):
            #suppose P is biggest then
            p = i  
            for j in range(i+ 1 , A.shape[1]):
                if (abs(a[j][i]) > abs(a[p][i])):
                    p = j 
                else :
                    continue
            a[[i,p]] = a[[p,i]]

        #Forward Elimination
        n = A.shape[0]
        for i in range (n):
            for j in range (i +1,n):
                factor = a[j][i]/a[i][i]
                a[j] = a[j] - factor*a[i]

        #BackSubstitution
        x = np.zeros(n)

        for i in range(n-1, -1, -1):
            x[i] = (a[i, -1] - np.dot(a[i, i+1:n], x[i+1:n])) / a[i, i]
        return x
    else:
        raise Exception("Incorrect Form of Matrices entered")


###    TestCases





# A = np.array([
#     [0, 2, 3],
#     [4, 5, 6],
#     [7, 8, 10]
# ], dtype=float)

# B = np.array([
#     [13],
#     [25],
#     [39]
# ], dtype=float)
# print(Gauss_ell(A,B))


# A = np.array([
#     [2, 1, -1],
#     [1, -1, 2],
#     [3, 2, 1]
# ], dtype=float)

# B = np.array([
#     [3],
#     [2],
#     [8]
# ], dtype=float)

# print(Gauss_ell(A, B))


A = np.array([
    [0, 2, 3],
    [1, 1, 1],
    [2, 3, 4]
], dtype=float)

B = np.array([
    [13],
    [6],
    [13]
], dtype=float)

print(Gauss_ell(A, B))














                    
            
            
    





























