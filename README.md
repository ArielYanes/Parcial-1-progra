Integrantes: 
Marielena Velasquez Escobar
Ariel Esau Yanes Quintanilla


pregunta 1
Ventajas de usar módulos vs un solo archivo

Organización del código: Separar el proyecto en varios módulos hace que cada archivo tenga una responsabilidad clara (ejemplo: uno para los aparatos, otro para los cálculos, otro para la ejecución).

Mantenimiento más fácil: Si hay un error, es más sencillo localizarlo en el módulo correspondiente sin revisar todo el programa.

Reutilización: Podemos importar un módulo en otro proyecto sin necesidad de copiar todo el código.

Escalabilidad: Si el sistema crece, es más simple añadir nuevas funciones o clases en archivos separados.



pregunta 2

Uso de la Programación Orientada a Objetos (POO)

Aplicamos POO creando clases que representan elementos del problema real.

Ejemplo en la primera versión:

La clase Aparato modela un electrodoméstico, con atributos (nombre, potencia, horas de uso) y métodos para calcular su consumo y costo.

La clase GestorAparatos administra varios aparatos, suma consumos, calcula totales y genera el reporte.

Ejemplo en la segunda versión:

Una sola clase ConsumoEnergia que encapsula tanto el registro de aparatos como los cálculos.



pregunta 3
Uso de GitHub en el trabajo colaborativo:
GitHub permite que cada integrante trabaje en su parte sin sobrescribir el código del otro. Por ejemplo, un integrante pudo trabajar en la clase Aparato mientras otro avanzaba en GestorAparatos, y luego se integraron los cambios mediante pull requests.
