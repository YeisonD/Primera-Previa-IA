# Preguntas: Rondas de preguntas para dar un diagnostico predictivo

def Preguntas():
    covid19 = 0
    diabetes = 0
    anemia = 0

    print("\n\t\tPreguntas de Diagnostico")
    Ronda1 = int(input("\n 1. Fiebre \n 2. Hambre Extrema \n 3. Mareos \n Seleccione una opcion: "))

    if Ronda1 == 1:
        covid19 += 1
    elif Ronda1 == 2:
        diabetes += 1
    elif Ronda1 == 3:
        anemia += 1
    else:
        print ("\n¡Lo sentimos, Ha Ocurrido un Error!")
    
    Ronda2 = int(input("\n 1. Dificultad para Respirar \n 2. Miccion frecuente \n 3. Fatiga \n Seleccione una opcion: "))

    if Ronda2 == 1:
        covid19 += 1
        anemia += 1
    elif Ronda2 == 2:
        diabetes += 1
    elif Ronda2 == 3:
        covid19 += 1
        diabetes += 1
        anemia += 1
    else:
        print ("\n¡Lo sentimos, Ha Ocurrido un Error!")
    
    Ronda3 = int(input("\n 1. Molestias y dolores \n 2. Vision Borrosa \n 3. Piel Palida o Amarillenta \n Seleccione una opcion: "))

    if Ronda3 == 1:
        covid19 += 1
    elif Ronda3 == 2:
        diabetes += 1
    elif Ronda3 == 3:
        anemia += 1
    else:
        print ("\n¡Lo sentimos, Ha Ocurrido un Error!")

    Ronda4 = int(input("\n 1. Perdida del Gusto o el Olfato \n 2. Perdida de Peso sin Razon \n 3. Dolor en el Pecho \n Seleccione una opcion: "))

    if Ronda4 == 1:
        covid19 += 1
    elif Ronda4 == 2:
        diabetes += 1
    elif Ronda4 == 3:
        covid19 += 1
        anemia += 1
    else:
        print ("\n¡Lo sentimos, Ha Ocurrido un Error!")
    
    print("\n")
    #print("Covid 19: ", covid19)
    #print("Diabetes: ", diabetes)
    #print("Anemia: ", anemia)

    if diabetes < covid19 > anemia:
        print("\n")
        print("Existe una alta posibilidad de que usted tenga Covid-19")
    elif covid19 < diabetes > anemia:
        print("\n")
        print("Existe una alta posibilidad de que usted tenga Diabetes")
    elif covid19 < anemia > diabetes:
        print("\n")
        print("Existe una alta posibilidad de que usted tenga Anemia")