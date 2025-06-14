#!/usr/bin/env python3

import os
import re
import sys


PATRON_VALIDO =re.compile(r'^[a-z][a-z0-9_]+$')


def main():
    errores = []

    ruta=os.path.join(os.path.dirname(__file__), "../iac")
    if not os.path.isdir(ruta):
        print(f"ERROR: No se encontro el directorio '{ruta}' ")
        sys.exit(1)

    for nombre in os.listdir(ruta):
        ruta_mod = os.path.join(ruta, nombre)
        if os.path.isdir(ruta_mod):
            if PATRON_VALIDO.match(nombre):
                print(f"OK: {nombre} ")
            else:
                print(f"ERROR: {nombre} no cumple el patro designado")
                errores.append(nombre)

    if errores:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()