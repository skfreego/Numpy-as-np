# HACKERRANK CHALLENGES
## Domain: Python
### SubDomain: Numpy

	The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
	To use the NumPy module, we need to import it using:
	import numpy

#### Arrays
A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
import numpy
a = numpy.array([1,2,3,4,5])
print a[1]          #2
b = numpy.array([1,2,3,4,5],float)
print b[1]          #2.0
In the above example, numpy.array() is used to convert a list into a NumPy array. The second argument (float) can be used to set the type of array elements.

#### Shape and Reshape
Shape :
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
(a). Using shape to get array dimensions

import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 

 
(b). Using shape to change array dimensions

import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]

 
Reshape
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]



#### Transpose and Flatten
Transpose

We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.

import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]

Flatten

The tool flatten creates a copy of the input array flattened to one dimension.

import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]



#### Concatenate
Concatenate:
Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined: 

import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]


if an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]  


#### Zeros and Ones
zeros
The zeros tool returns a new array with a given shape and type filled with 0's.

import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

 
ones
The ones tool returns a new array with a given shape and type filled with 1's.

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]   

##### Explanation: 
Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown. 


#### Eye and Identity
	identity :
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0. The default type of elements is float. 

import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

 
eye :
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter K. A positive K is for the upper diagonal, a negative K is for the lower, and a 0 K (default) is for the main diagonal.

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

#### Array Mathematics
 Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

#### Floor, Ceil and Rint

floor
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i <= x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

 
ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling x of is the smallest integer i where i >= x.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

 
rint
The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]


#### Sum and Prod
Sum 
The sum tool returns the sum of array elements over a given axis. 

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10


By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.
 
Prod
The prod tool returns the product of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24

 
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array. 

#### Explanation :
The sum along axis 0 = [4 6]
The product of this sum = 24


#### Min and Max
Min
The tool min returns the minimum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0


By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array. 
 
Max
The tool max returns the maximum value along a given axis. 

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7

 


#### Explanation:-
The min along axis 1 = [2, 3, 1, 0]
The max of [2, 3, 1, 0]= 3 





#### Mean Var and Std
mean
The mean tool computes the arithmetic mean along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

 
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var
The var tool computes the arithmetic variance along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

 
By default, the axis is None. Therefore, it computes the variance of the flattened array.
 
std
The std tool computes the arithmetic standard deviation along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875

 
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array. 

#### Dot and Cross


dot
The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11


Cross
The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2


#### Inner and Outer

inner
The inner tool returns the inner product of two arrays. 

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4


outer 
The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]


#### Polynomials

poly

The poly tool returns the coefficients of a polynomial with the given sequence of roots.

print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

roots

The roots tool returns the roots of a polynomial with the given coefficients.

print numpy.roots([1, 0, -1])           #Output : [-1.  1.]

polyint

The polyint tool returns an antiderivative (indefinite integral) of a polynomial.

print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]

polyder

The polyder tool returns the derivative of the specified order of a polynomial.

print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]

polyval

The polyval tool evaluates the polynomial at specific value.

print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34

polyfit

The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.

print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.


#### Linear Algebra

The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.

linalg.det

The linalg.det tool computes the determinant of an array.

print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0

linalg.eig

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print vals                                      #Output : [ 3. -1.]
print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

linalg.inv

The linalg.inv tool computes the (multiplicative) inverse of a matrix.

print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]

Other routines can be found here



#### Innominion_Oct_21
###  Innomatics Research Labs
##   Internship




