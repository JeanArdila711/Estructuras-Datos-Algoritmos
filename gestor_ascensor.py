import random
from trabajador import Trabajador
from ascensor import Ascensor

def calcular_distancia(piso1, piso2):
    return abs(piso1 - piso2)

def main():
    num_pisos = 120

    posibles_pisos = list(range(1, num_pisos + 1))
    posibles_estados = [True, False]

    posiciones_aleatorias = random.sample(posibles_pisos, 20)
    ascensores = [Ascensor(1, posicion, random.choice(posibles_estados)) for posicion in posiciones_aleatorias]

    # Seleccionar 10 ascensores aleatoriamente para ser de emergencia
    ascensores_emergencia = random.sample(ascensores, 10)
    for ascensor in ascensores_emergencia:
        ascensor.emergencia = True

    num_trabajadores = random.randint(100, 200)
    trabajadores = [Trabajador(random.randint(1, num_pisos), random.randint(1, num_pisos)) for _ in range(num_trabajadores)]

    fallo_electricidad = False  # Simula el estado de la electricidad

    trabajadores_procesados = set()  # Crear un conjunto para rastrear trabajadores procesados

    while True:
        for trabajador in trabajadores:
            if trabajador not in trabajadores_procesados:
                print(f"Trabajador: Piso {trabajador.piso_actual} -> Piso {trabajador.piso_destino}")

                ascensor_mas_cercano = None
                ascensor_libre_cerca = None

                distancia_minima = float('inf')

                rango_inferior = max(1, trabajador.piso_actual - 60)
                rango_superior = min(120, trabajador.piso_actual + 60)

                ascensores_cerca_ocupados = []

                for ascensor in ascensores:
                    if ascensor.emergencia or (not ascensor.ocupado and not fallo_electricidad):
                        ascensor.piso_actual = ascensor.piso_destino
                    distancia = calcular_distancia(ascensor.piso_actual, trabajador.piso_actual)
                    if distancia < distancia_minima:
                        if rango_inferior <= ascensor.piso_actual <= rango_superior:
                            distancia_minima = distancia
                            if not ascensor.ocupado:
                                ascensor_libre_cerca = ascensor
                            ascensor_mas_cercano = ascensor
                        if ascensor.ocupado:
                            if (ascensor.piso_actual <= 60 and trabajador.piso_actual <= 60) or (ascensor.piso_actual > 60 and trabajador.piso_actual > 60):
                                ascensores_cerca_ocupados.append(ascensor)


                if ascensor_mas_cercano:
                    if ascensor_mas_cercano.ocupado:
                        print(f"Ascensor en piso {ascensor_mas_cercano.piso_actual}: Ocupado y se mueve hacia el piso {ascensor_mas_cercano.piso_destino}")
                    else:
                        print(f"Ascensor en piso {ascensor_mas_cercano.piso_actual}: Disponible y se mueve hacia el piso {trabajador.piso_destino}")
                        ascensor_mas_cercano.ocupado = True
                        ascensor_mas_cercano.piso_destino = trabajador.piso_actual
                else:
                    print("No hay ascensores disponibles. Por favor, espera.")

                for ascensor in ascensores:
                    if ascensor.ocupado and ascensor.piso_actual == trabajador.piso_destino:
                        ascensor.ocupado = False
                        print(f"Ascensor en piso {ascensor.piso_actual}: Libre")

                if ascensor_libre_cerca and ascensor_libre_cerca.piso_actual != trabajador.piso_actual:
                    ascensor_libre_cerca.piso_destino = trabajador.piso_actual

                trabajadores_procesados.add(trabajador)  # Agregar al trabajador a la lista de procesados

        # Verificar si todos los trabajadores han sido procesados al menos una vez
        if len(trabajadores_procesados) == len(trabajadores):
            break

if __name__ == "__main__":
    main()
