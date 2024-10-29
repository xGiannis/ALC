import numpy as np
import matplotlib.pyplot as plt
#ejer 18)

def estimacion_norma_2(A):
    V = np.random.rand(3,100)
    
    
    for i in range(V.shape[1]):
        x = V[0,i]
        y= V[1,i]
        z= V[2,i]

        norma = np.sqrt(x**2 + y**2+z**2)

        V[0,i] = V[0,i] / norma
        V[1,i] = V[1,i] / norma
        V[2,i] = V[2,i] / norma

    AX= A@V

    normas_AX = []

    sk=[0]

    for i in range(AX.shape[1]):
        norma_Avi = np.linalg.norm(AX[:, i])  # ||A vi||

        normas_AX.append(norma_Avi)

    


        sk.append(max(sk[i],norma_Avi))
    
    return sk



        


    



A=np.array([[1,1,1],[5,1,3],[2,1,2]])
#A@V pertenece a n x 100

a=estimacion_norma_2(A)


valor_manual = np.linalg .norm(A) 

# Graficar las normas calculadas sin el índice
plt.scatter(a, np.zeros_like(a), label='Normas calculadas ||A v_i||', marker='o')

# Añadir una línea vertical para el valor calculado a mano
plt.axvline(x=valor_manual, color='r', linestyle='--', label=f'Valor manual = {valor_manual}')


plt.xlabel('Norma ||A v_i||')
plt.title('Comparación de normas calculadas vs valor manual')
plt.legend()
plt.yticks([])  # Eliminar el eje y, porque no es relevante en 1D
plt.show()