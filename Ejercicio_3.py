import random

if __name__ == "__main__":
    Lista1 = []
    contador : int = int(input("Dijite cuantos números tendran la lista: "))
    for j in range(contador):
        Lista1.append(random.randint(0,5)) # Utilizamos números aleatorios para probar el codigo #
    Lista2 = Lista1 # Utilizamos la Lista 2 para tener un registro de la lista orginal #  
    if Lista1.count(0) == 0 :
        print(f"La lista {Lista1} no contiene el número 0 por lo tanto la lista queda igual")
    else:
        for i in range(Lista1.count(0)): 
                Lista1.remove(0) 
                Lista1.append(0) # Removemos los 0 e inmediatamente los agregamos a la lista del lado derecho #
        print(f"La lista fue modificada y quedó de esta forma {Lista1}")
        print(Lista2)