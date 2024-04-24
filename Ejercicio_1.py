import random

if __name__ == "__main__":
    cantidad_datos : int = int(input("Dijite el número de datos que tendra la lista: "))
    Numeros = []
    Contador : int = 0
    for i in range(cantidad_datos):
        Numeros.append(random.randint(0,200))

    for j in Numeros:
        Contador = Contador + j
    
    Promedio : float = Contador / cantidad_datos

    print(f"El promedio de los números {Numeros} es {Promedio}")
        
