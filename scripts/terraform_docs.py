#!/usr/bin/env python3
"""
scripts/terraform_docs.py
Recorre cada módulo en iac/ y genera archivos Markdown en docs/<módulo>.md
"""
import os
import re
import json

def parse_variables(modulo_path):
    """
    Lee variables.tf y extrae nombre, tipo, default y descripción.
    """
    # TODO: implementar parsing con regex
    return []

def parse_outputs(modulo_path):
    """
    Lee outputs.tf y extrae nombre y descripción.
    """
    # TODO: implementar parsing con regex
    return []

def parse_resources(modulo_path):
    """
    Lee main.tf y extrae recursos (tipo, nombre).
    """
    # TODO: implementar parsing con regex
    return []

def write_markdown(modulos):
    """
    Por cada módulo, escribe docs/<módulo>.md con:
    - Encabezado
    - Descripción placeholder (100 palabras)
    - Tabla de variables
    - Tabla de outputs
    - Lista de recursos
    """
    # TODO: recorrer lista de módulos y generar Markdown
    pass

def main():
    root = os.path.join(os.path.dirname(__file__), "../iac")
    # TODO: detectar carpetas de módulo y llamar a parse_*/write_markdown
    pass

if __name__ == "__main__":
    main() 