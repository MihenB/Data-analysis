import numpy as np
#a1x+b1y=c1; a2x+b2y=c2
#x-y=0; -x-y=-1
M=np.matrix([[1, -1]])
C=np.matrix([0, -1])
print(M.I.dot(C.T))