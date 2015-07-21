"""
"primes.py" por Pedro A. Carpio

Contacteme a través del Teléfono: (416)434-7903, o el Correo Electrónico: alcarpio15@gmail.com
"""


class CalculatorClass(object):
    """
    Para propósitos del Ejercicio, la Clase PrimeClass solo contiene la implementación
    del Método de Consulta "sum(num_list)".
    """

    def sum(self, num_list):
        """
        El Método sum es una clásica Suma Acumulada.
        """
        # your sum code here
        a=0

        for i in num_list:
        	a = a + i

        return a
        