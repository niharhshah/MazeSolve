import matplotlib.pyplot as pl
import numpy as np
n = int(input("Enter map width: "))
m = int(input("Enter map length: "))

#init Array of m x n

Arr=[]
# n, m=4,4
for i in range(n+2):
	col = []
	for j in range(m+2):
		col.append(0)
	Arr.append(col)

def boundry(Arr):
    length = len(Arr[0])
    width = len(Arr)
    print(length,width)
    for i in range(length):
        # pass
        print("length=",i)
        Arr[0][i] = 1
        Arr[length-1][i] = 1
        print(Arr)
    for i in range(width):
        Arr[i][0] = 1
        Arr[i][width-1] = 1

boundry(Arr)
print(Arr)
pl.grid()
pl.imshow(Arr)
# pl.
pl.show()