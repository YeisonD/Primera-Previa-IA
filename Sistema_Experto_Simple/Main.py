from Funciones import *
# ---- Menu Principal ------------
#Desde aquí se da inicio al programa

menuPrincipal = int(input("\n\n\t\tSistema de Diagnostico de Enfermedades  \n\n 1. Comenzar Diagnostico \n 0. Salir \n\n Elija una Opcion: "))

while menuPrincipal != 0:
    if menuPrincipal == 1:
        Preguntas()
        #print("Questionario")
    else:
        print("¡Digite una Opcion Valida!")
    menuPrincipal = int(input("\n\n\t\tSistema de Diagnostico de Enfermedades  \n\n 1. Comenzar Diagnostico \n 0. Salir \n\n Elija una Opcion: "))
