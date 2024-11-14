import numpy as np
#ejer 9

x = [0,1,2,4,6]
y=[200,195,180,120,25]

coef=np.polyfit(x,y,2)
print(coef)

#como yo necesito f(t) =at^2 + b, polyfit no me sirve
# habria q agregarle un coeficiente mas

