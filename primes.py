"""
"primes.py" por Pedro A. Carpio

Contacteme a traves del Telefono: (416)434-7903,
o el Correo Electronico: alcarpio15@gmail.com
"""


class PrimeClass(object):
    """
    Hasta ahora, la Clase PrimeClass solo contiene la implementacion
    del Metodo de Consulta "is_prime(num_int)".
    """

    def is_prime(self, num_int):
        """
        El Metodo is_prime consiste simplemente del uso liberal de una Bandera
        Booleana, y tanto la operacion "num_int MOD num" como un 'break' dentro
        de un ciclo tipo-Para:

        Se asume que el numero puede ser primo antes de iniciar el ciclo
        (pero despues de Evaluar que el numero en cuestión no sea '1'); y si
        durante el recorrido se descubre que es multiplo de algun numero num,
        entonces la Bandera reflejara la contradiccion antes de que el ciclo
        frene por la aplicacion del break.

        Retorna: Un Valor Booleano.
        """
        # your primes code here
        prim = True

        if num_int is 1:
            return False

        else:
            for num in range(2, num_int):
                if num_int % num == 0:
                    prim = False
                    break

            return prim
