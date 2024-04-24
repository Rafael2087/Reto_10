import random

if __name__ == "__main__":
    cantidad_datos : int = int(input("Dijite el número de datos que tendra la lista: ")) # Solicitamos al usuario para saber cuantos números desea que tenga la lista #
    Numeros = []
    Contador : int = 0 # Declaramos está variable para que nos permita almacenar en ella la suma de los datos de la lista #
    for i in range(cantidad_datos):
        Numeros.append(random.randint(0,200)) # Agregamos los números a nuestra lista #
    for j in Numeros:
        Contador = Contador + j # Nos permite recorrer los datos de la lista y sumarlos #   
    Promedio : float = Contador / cantidad_datos # Formula para calcular el promedio #
    print(f"El promedio de los números {Numeros} es {Promedio}")
        