"""
"primes.py" por Pedro A. Carpio

Contacteme a través del Teléfono: (416)434-7903, o el Correo Electrónico: alcarpio15@gmail.com
"""


class PrimeClass(object):
    """
    Hasta ahora, la Clase PrimeClass solo contiene la implementación
    del Método de Consulta "is_prime(num_int)".
    """

    def is_prime(self, num_int):
        """
        El Método is_prime consiste simplemente del uso liberal de una Bandera Booleana,
        y tanto la operación "num_int MOD i" como un 'break' dentro de un ciclo tipo-Para:
        
        Se asume que el número puede ser primo antes de iniciar el ciclo; y si durante el
        recorrido se descubre que es multiplo de algún número i, entonces la Bandera reflejará
        la contradicción antes de que el ciclo frene por la aplicación del break.

        Retorna: la Bandera Booleana 'prim'.
        """
        # your primes code here
        prim = True

        for i in range(2, num_int):
        	if (num_int%i == 0):
        		prim = False
        		break

        return prim
