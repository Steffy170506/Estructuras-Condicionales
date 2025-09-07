def comparacion_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

comparacion_numeros()