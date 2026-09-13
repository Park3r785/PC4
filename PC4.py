def Calcular_promedio(numeros: list[int]) -> float:
    suma = 0
    for numero in numeros:
        suma += numero
    promedio = suma / len(numeros)
    return promedio

ingreso: list[int] = [int(x) for x in input("Ingrese las notas separadas por comas: ").split(",")]
print(f"El promedio del estudiante es de: {Calcular_promedio(ingreso)}")