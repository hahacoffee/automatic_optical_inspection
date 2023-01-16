import numpy as np
fx=100
fy=120
L1=np.array([[1,0],[(-1/fx),1]])
L2=np.array([[1,0],[(-1/fy),1]])
T=np.array([[1,1],[0,1]])
P1=T*L1
P2=T*L2
