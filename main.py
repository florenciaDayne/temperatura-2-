from typing import List

class AnalizadorTemperaturas:
    def __init__(self, dias: int = 7):
        self.dias = dias
        self.dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
        self.temperaturas: List[float] = []

    def solicitar_temperatura(self):
        print("Ingreso de temperaturas diarias\n")
        for dia in range(self.dias):
            while True:
                try:
                    entrada = input(f"Ingrese temperatura del día {self.dias_semana[dia % 7]}: °")
                    temperatura = float(entrada)
                    if temperatura < -100:
                        raise ValueError("La temperatura no es válida")
                    if temperatura < 0:
                        print("¡Extremo!! Frío")
                    if temperatura > 40:
                        print("¡Extremo!! Calor")
                    self.temperaturas.append(temperatura)
                    break
                except ValueError as e:
                    print(f"Entrada no válida: {e}")

    def analizar_temperatura(self):
        if not self.temperaturas:
            print("No hay temperaturas registradas.")
            return

        print("\nResumen de temperaturas\n")
        total = sum(self.temperaturas)
        promedio = total / self.dias
        maxima = max(self.temperaturas)
        minima = min(self.temperaturas)
        dia_max = self.temperaturas.index(maxima)
        dia_min = self.temperaturas.index(minima)

        print(f"Promedio: {promedio:.1f}°C")
        print(f"Máxima: {maxima:.1f}°C (Día: {self.dias_semana[dia_max % 7]})")
        print(f"Mínima: {minima:.1f}°C (Día: {self.dias_semana[dia_min % 7]})")

def main():
    analizador = AnalizadorTemperaturas()
    analizador.solicitar_temperatura()
    analizador.analizar_temperatura()

if __name__ == "__main__":
    main()
