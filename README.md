# Reto_10 #

En este repositorio vamos a explicar detalladamente los ejercicios resueltos en el reto 10

# Ejercicio 1 #

Se nos pide desarrollar un algoritmo que permita calcular el promedio aritmetico de los datos de una sobra decir que la lista o arreglo necesariamente debe ser de datos estrictamente numericos

```python
# Declaramos la lista #
Lista_1 = [1,2,3,4]
# Variable que permita almacenar los datos #
Contador : int = 0
# Se recorren los datos de la lista #
for i in range(len(Lista_1)):
    Contador = i + Contador # 10 #
Promedio : float = Contador / len(Lista_1)
print(Promedio) # 2.5 #
```
# Ejercicio 2 #

Se nos pide calcular el punto producto entre 2 vectores tomando los arreglos como vectores que obligatoriamente deben tener el mismo tamaño, para poder calcular el punto producto entre 2 vectores se deben multiplicar las componentes entre vectores y despues sumarse todas las multiplicaciones de tal forma que tenemos.
a = [a1 , a2, a3, ..., an-1] y b = [b1, b2, b3, ..., bn-1] entonces a x b = [a1*b1 + a2*b2 + a3*b3 + ... + an-1*bn-1], sabiendo eso ya podemos ir a programar nuestro codigo.

```python
Lista1 = [1,2,3,4]
Lista2 = [4,3,2,1]
Producto : int = 0 
for i in range(len(Lista1)) # Recorremos las listas #
    Producto = Producto + (Lista1[i]*Lista2[i]) # Sumamos los valores de las multiplicaciones #
print(Producto)
# 20 #
```
# Ejercicio 3 #

Se nos pide que en una lista organizemos los números de tal forma que los valores que sean igual a 0 queden a la derecha del todo

```python
Lista_1 = [0,1,0,2,0,3,0,4]
contador = Lista_1.count(0) # Contamos cuantos 0 hay en la lista #
for i in range(contador)
    Lista_1.remove(0) # Removemos los 0 de la lista #
    Lista_1.append(0) # Agregamos los 0 al final de la lista #
print(Lista_1)
# [1,2,3,4,0,0,0,0] # 
```
Ese seria el codigo solicitado igual se dejaran en el repo los archivos para probarlos, muchisimas gracias (Aún sigo aprendiendo a subir cosas en Markdown)