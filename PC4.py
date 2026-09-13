# Función para calcular el promedio de una lista de notas
def Calcular_promedio(notas: list[int]) -> float:
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return promedio

notas: list[int] = [int(x) for x in input("Ingrese las notas separadas por comas: ").split(",")]
print(f"El promedio del estudiante es de: {Calcular_promedio(notas)}")