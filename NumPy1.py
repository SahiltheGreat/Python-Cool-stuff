import numpy as np
from numpy import pi

# inserting 0 to 14 in array of dimensions 3x5 
a = np.arange(15).reshape(3,5)

print(a,end='\n\n') 
# printing the dimensions of the array
print(a.shape,end='\n\n')
# printing the number of dimensions
print(a.ndim,end='\n\n')
# printing the data type
print(a.dtype.name,end='\n\n')
# printing size of each array element
print(a.itemsize,end='\n\n')
# printing total number of array elements
print(a.size,end='\n\n')
# printing the type of array 
print(type(a),end='\n\n')

# creating array from a list
b = np.array([(1,3),(2,4)])
print(b,end='\n\n')

# declaring datatype of array explicitly
c = np.array([3,6,8,1],dtype=complex)
print(c,end='\n\n')

# inserting all odd numbers from 1 to 20 in array
d = np.arange(1,20,2)
print(d,end='\n\n')

e = np.linspace(0,2,9)
print(e,end='\n\n')
f = np.linspace(0,2*pi,100)
print(f,end='\n\n')
g = np.sin(f)
print(g,end='\n\n')

print(e<1, end='\n\n')

matrixone = np.array([[1,2],[3,4]])
matrixtwo = np.array([[5,6],[7,8]])

# element wise product
print(matrixone*matrixtwo,end='\n\n')

# matrix product
print(matrixone @ matrixtwo,end='\n\n')
print(matrixone.dot(matrixtwo),end='\n\n')




