def clasificacion_triangulos():
    a = float(input("Ingrese la longitud del primer lado: "))
    b = float(input("Ingrese la longitud del segundo lado: "))
    c = float(input("Ingrese la longitud del tercer lado: "))
    
    if a == b == c:
        print("Triángulo equilátero")
    elif a == b or a == c or b == c:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")

clasificacion_triangulos()