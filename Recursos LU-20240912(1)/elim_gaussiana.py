#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(n) #inciamos L de nxn

    #Gaussian Elimination
    for i in range(n):
        if Ac[i,i]==0:
            # ...
            # aca supongo q tengo q hacer la permutacion ||| NO!!!!!!!! ES SIN PERMUTACION
            print(f"Pivote {i} es nulo")
            return


        for j in range(i+1, n):
            factor = Ac[j,i] / Ac[i,i]#aca va q multiplico entre las matrices para q de 0.
            L[j,i] = factor # guardamos el factor en la matriz L 
            Ac[j,i:] = Ac[j,i:]  - factor*Ac[i,i:]
            #cant_operaciones #... n por algo
            print(f"Matriz L despuse del paso ({j},{i})")
            print(L) 

    ## hasta aqui
            
    #L = np.tril(Ac,-1) + np.eye(A.shape[0]) 
    print("esto queda despues de todos los pasos --->\n",Ac)
    U = np.triu(Ac)
    
    return L, U, cant_op


def main():
        
    matriz = np.array([[2,1,2,3],[4,3,3,4],[-2,2,-4,-12],[4,1,8,-3]])


    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) #triangular lower
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()


def ejMatriz():
        
    matriz = np.array([[2,1,2,3],[4,3,3,4],[-2,2,-4,-12],[4,1,8,-3]])


    print('Matriz B \n', matriz)
    
    L,U,cant_oper = elim_gaussiana(matriz)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(matriz - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

ejMatriz()

