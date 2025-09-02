class ConsumoEnergia:
    def __init__(self, precio_kwh):
        self.precio_kwh = precio_kwh
        self.aparatos = []

    def agregar_aparato(self, nombre, potencia_w, horas_dia):
        """Registra un aparato en la lista"""
        self.aparatos.append({
            "nombre": nombre,
            "potencia_w": potencia_w,
            "horas_dia": horas_dia
        })

    def calcular_consumo(self, aparato):
        """Devuelve consumo mensual en kWh"""
        return (aparato["potencia_w"] * aparato["horas_dia"] * 30) / 1000

    def calcular_costo(self, aparato):
        """Devuelve costo mensual en $"""
        return self.calcular_consumo(aparato) * self.precio_kwh

    def reporte(self):
        print("\n===== REPORTE DE CONSUMO ENERGÉTICO =====")
        consumo_total = 0
        costo_total = 0

        for a in self.aparatos:
            consumo = self.calcular_consumo(a)
            costo = self.calcular_costo(a)
            consumo_total += consumo
            costo_total += costo
            print(f"{a['nombre']}: {consumo:.2f} kWh | ${costo:.2f}")

        print("\n--- RESUMEN ---")
        print(f"Consumo total: {consumo_total:.2f} kWh")
        print(f"Gasto mensual: ${costo_total:.2f}")