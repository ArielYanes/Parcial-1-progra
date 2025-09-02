from consumo import ConsumoEnergia

def main():
    precio = float(input("Ingrese el precio del kWh en $: "))
    sistema = ConsumoEnergia(precio)

    while True:
        nombre = input("\nNombre del aparato: ")
        potencia = float(input("Potencia en watts: "))
        horas = float(input("Horas de uso al día: "))

        sistema.agregar_aparato(nombre, potencia, horas)

        cont = input("¿Desea ingresar otro aparato? (s/n): ")
        if cont.lower() != "s":
            break

    sistema.reporte()

if __name__ == "__main__":
    main()