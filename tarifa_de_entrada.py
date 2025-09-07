def tarifa_entrada():
    edad = int(input("Ingrese la edad: "))
    
    if edad < 12:
        print("Costo de entrada: $50")
    elif 12 <= edad <= 17:
        print("Costo de entrada: $80")
    else:
        print("Costo de entrada: $120")

tarifa_entrada()