"""
"calculator.py" por Pedro A. Carpio

Contacteme a traves del Telefono: (416)434-7903,
 o el Correo Electronico: alcarpio15@gmail.com
"""


class CalculatorClass(object):
    """
    Para propositos del Ejercicio, la Clase PrimeClass
    solo contiene la implementacion del Metodo de Consulta
    "sum(num_list)".
    """

    def sum(self, num_list):
        """
        El Metodo sum es una clasica Suma Acumulada.

        Retorna: El Entero Acumulado 'acum'.
        """
        acum = 0

        for num in num_list:
            acum = acum + num

        return acum
