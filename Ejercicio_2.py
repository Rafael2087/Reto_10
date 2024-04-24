import random

def ProductoPunto (x : int, y : int , z : int):
    contador : int = 0
    for i in range(z):
        contador = contador + (x[i] * y[i])
    return contador
    
if __name__ == "__main__" :
    Numeros : int = int(input("Dijite el número de elementos que tendran las listas: "))
    Lista1 = []
    Lista2 = []
    for i in range(Numeros):
        Lista1.append(random.randint(-5,10))
        Lista2.append(random.randint(-5,10))
    ProductoListas : int = ProductoPunto(Lista1,Lista2,Numeros)
    print(f"Los vectores {Lista1} y {Lista2} tienen como producto punto {ProductoListas}")