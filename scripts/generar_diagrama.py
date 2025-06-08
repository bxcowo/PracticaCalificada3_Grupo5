#!/usr/bin/env python3
"""
scripts/generar_diagrama.py
- Genera docs/diagrama_red.dot a partir de los .tfstate en cada módulo
"""
import os
import json

def generate_dot():
    """
    Lee terraform.tfstate de cada módulo (iac/<módulo>/terraform.tfstate)
    y extrae dependencies para formar un grafo DOT.
    """
    # TODO: implementar lectura de JSON y generar líneas DOT
    return

def main():
    # TODO: invocar generate_dot() y escribir docs/diagrama_red.dot
    pass

if __name__ == "__main__":
    main() 