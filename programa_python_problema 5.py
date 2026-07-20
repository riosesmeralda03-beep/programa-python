# ------------------------------------------
# nombre del estudiante:Yeny Esmeralda Rios orozco
# grupo: 213022_94
# Fase 5 - Evaluación Final POA
# Problema 5
# Curso: Fundamentos de Programación
# codigo fuente autoria propia
# ------------------------------------------

# Función para calcular el total de horas y clasificar la jornada
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz con los recursos y horas trabajadas
recursos = [
    ["Juan Pérez", 8, 8, 9, 8, 8],
    ["Ana López", 7, 8, 8, 8, 8],
    ["Carlos Ruiz", 10, 9, 9, 8, 8],
    ["Laura Gómez", 6, 7, 8, 7, 7]
]


print("=" * 60)
print("      REPORTE DE HORAS TRABAJADAS")
print("=" * 60)

for recurso in recursos:

    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print(f"\nRecurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")

print("\nFin del reporte.")