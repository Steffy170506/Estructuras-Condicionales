def conversor_calificaciones():
    calificacion = int(input("Ingrese la calificación (0-100): "))
    
    if 90 <= calificacion <= 100:
        print("Calificación: A")
    elif 80 <= calificacion <= 89:
        print("Calificación: B")
    elif 70 <= calificacion <= 79:
        print("Calificación: C")
    elif 60 <= calificacion <= 69:
        print("Calificación: D")
    elif 0 <= calificacion < 60:
        print("Calificación: F")
    else:
        print("Calificación fuera de rango")

conversor_calificaciones()