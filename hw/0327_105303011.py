clc()
import numpy as np
g0=np.loadtxt("g0t.txt")
g1=np.loadtxt("g1t.txt")
g2=np.loadtxt("g2t.txt")
g3=np.loadtxt("g3t (1).txt")
g4=np.loadtxt("g4t.txt")
g5=np.loadtxt("g5t.txt")
h=np.array([1,-1])
gh0=np.convolve(g0,h)
gh1=np.convolve(g1,h)
gh2=np.convolve(g2,h)
gh3=np.convolve(g3,h)
gh4=np.convolve(g4,h)
gh5=np.convolve(g5,h)
print("g3t (1).txt is the most clear picture!")