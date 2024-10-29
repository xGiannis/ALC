import numpy as np
"""
7) 
a)
p = 1e34
q = 1

p + q - p = 0.0, esperabamos que salga 1.
El problema se debe a q el epsilon de maquina es mas chico
que el numero dado, por lo cual la resta del mismo numero
al sumarle el 1 q en maginutd es muchisimo mas chico, solo me da 0,
q entra en el margen de error

b)
p= 100
q= 1e-15

b=(p+q)+q=100 , espero que de 100 + 2e-15. 
veo q si solo veo q, entra en el error del epsilon, pero al tener
2 0s mas el 100, ahi se va.

efectivamente si multiplioco q*100, el resultado es 100.0000000000002


b2= ((p+q)+q)+q = 100, esperamos 100 + 3e-15

b2.1 = p + 2q =100 , espero b2

b2.2= p + 3q = 100 ,espero b2

Ademas,
In [20]: (((p+q)+q)+q) - (p+3*q)
Out[20]: 0.0

In [21]: (((p+q)+q)+q) - (p+2*q)
Out[21]: 0.0



c) 
0.1+0.2 == 0.3 ---> False
esperaba claramente True, pero (0.1+0.2 = 0.30000000000000004)
aca si no se el error. Por lo que vi, 0.1 y 0.2 tienen reprs binaria
inf, por lo que amvos estan redondeados, y dan ese error.

d)
0.1 + 0.3 == 0.4 ----> True.

e)y f) veo que 1e323 = 1e323 pero 1e324 = 0.

g) epsilon / 2 dio correctamente. esto es porque tiene un 2 adelante
y dividirlo por 2 era sacar ese 2 y poner un 1.

h) (1 + ε/2) + ε/2 = 1.0. esto es porque epsilon es el nmumero
mas chico q si le sumo 1 cambia, pero al sumar el espilon separado,
esyoy sumando algo mas chico, por lo q 1 no cambia.

l) 
 senDe1a25()
-1.2246467991473533e-15
1.964386723728472e-15
-3.2141664592756335e-13
-4.85682353956849e-13
-3.3960653996302193e-11
-2.231912181360871e-10
5.620555424855643e-10
-3.9082928156687315e-08
-3.3201412914529495e-08
-2.2393627619559233e-06
-1.4764233087791559e-05
-0.00026971264011324254
-0.0026971231637969895
-0.011346020891205282
-0.2362090532517409
-0.3752128900123344
-0.8479696810401983
-0.6416534819105048
0.7463367130158111
-0.3940709604247648
-0.5808054397535704
-0.6886746870200211
-0.7965162588457232
0.9301407542552305

a medida q crece el 10 se pierde precision, y el resultado q
deberia ser 0 va incrementando por los errores de coma, hasta
casi llegar al resultado opuesto de seno(0) = 0

"""

#hago codigo poara l)


def senDe1a25():
    for j in range(1,25):
        l= np.sin((10**(j))*np.pi)
        print(l)

#8)

def serie(n:int):
    res = 0
    for i in range(1,n):
        res = res + 1/n

    return res

