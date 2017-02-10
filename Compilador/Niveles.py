import libreriaCompilador as compiler
import libreriaFunciones as libreria

opciones="0"
while opciones!="3":
    libreria.logo()
    libreria.menu_Juego()
    opciones=input("☺→")
    if opciones=="1":
        niveles=1
        print("PD: Escriba Salir como escape")
        while niveles<11:
            print("Presione enter para empezar el Nivel : "+str(niveles)+" .")
            escape = input("☺→")
            escape.strip()
            if(escape.lower()=="salir"):
                break
            if niveles == 1:
                print('Nivel 1')
                texto=compiler.compilador()
                print(texto)
                print(len(texto))
                niveles+=1
            elif niveles == 2:
                print('Nivel 2')
                niveles += 1
            elif niveles == 3:
                print('Nivel 3')
                niveles += 1
            elif niveles == 4:
                print('Nivel 4')
                niveles += 1
            elif niveles == 5:
                print('Nivel 5')
                niveles += 1
            elif niveles == 6:
                print('Nivel 6')
                niveles += 1
            elif niveles == 7:
                print('Nivel 7')
                niveles += 1
            elif niveles == 8:
                print('Nivel 8')
                niveles += 1
            elif niveles == 9:
                print('Nivel 9')
                niveles += 1
            elif niveles == 10:
                print('Nivel 10')
                niveles += 1
    elif opciones=="2":
        libreria.Ayuda()

    elif opciones=="3":
        break
    else:
        print("Ingrese una opcion correcta")

#texto= compiler.compilador()
#print(texto)