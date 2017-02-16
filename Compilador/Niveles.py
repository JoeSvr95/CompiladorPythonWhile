import libreriaCompilador as compiler
import libreriaFunciones as libreria
import re

opciones="0"
while opciones!="3":
    libreria.logo()
    libreria.menu_Juego()
    opciones=input("☺→")
    if opciones=="1":
        niveles=10
        print("PD: Escriba Salir como escape")
        while niveles<11:
            print("Presione enter para empezar el Nivel : "+str(niveles)+" .")
            escape = input("☺→")
            escape.strip()
            if(escape.lower()=="salir"):
                break
            # Niveles ---------------------------------------------------------------------------------------------
            print('Nivel ' + str(niveles))
            libreria.Descripcion_Nivel(niveles)
            libreria.requerimiento(niveles)
            texto = compiler.compilador()
            #texto = libreria.trampita_Salto_de_linea(texto)
            #texto= libreria.trampita_Tabulacion(texto)
            aprobo = libreria.regularExpresion(niveles, texto)
            if aprobo:
                print("Nivel " + str(niveles) + " logrado")
                niveles += 1
            else:
                print("Intentelo de nuevo")

    elif opciones=="2":
        libreria.Ayuda()

    elif opciones=="3":
        break
    else:
        print("Ingrese una opcion correcta")

#texto= compiler.compilador()
#print(texto)