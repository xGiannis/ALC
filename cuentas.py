import numpy as np
import matplotlib.pyplot as plt

"""# Coefficient matrix A
A = np.array([[1j, -(1j + 1), 0],
              [1, -2, 1],
              [1, 2j, -1]])

# Solution vector x
x = np.array([1j, 0, -1j])

# Calculate b = A @ x
b_calculated = np.dot(A, x)

#print("Calculated b:", b_calculated)


"""

#resolviendo el sistema en mi hoja me quedo
a=-3/2
b=11/2
c=-3


C= np.array([[1,1,1],[4,2,1],[9,3,1]])

xx = np.array ( [ 1 , 2 , 3 ] )
yy = np.array ( [ 1 , 2 , 0 ] )

x = np.linspace(0,4,100)

f = lambda t: a* t**2 + b* t + c

plt.plot(xx,yy,"*")

plt.plot(x,f(x))

plt.show()







