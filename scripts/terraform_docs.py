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
    Retorna: [{ "type": "<tipo>", "name": "<nombre>" }]
    """
    main_tf_path = os.path.join(modulo_path, "main.tf")
    
    # Si no existe main.tf, retorna lista vacía sin excepciones
    if not os.path.exists(main_tf_path):
        return []
    
    try:
        with open(main_tf_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex para extraer resource "<tipo>" "<nombre>"
        # El patrón busca 'resource' seguido de dos strings entre comillas
        pattern = r'resource\s+"([^"]+)"\s+"([^"]+)"'
        matches = re.findall(pattern, content)
        
        # Convertir a formato de diccionarios
        resources = []
        for tipo, nombre in matches:
            resources.append({
                "type": tipo,
                "name": nombre
            })
        
        return resources
        
    except Exception as e:
        # En caso de error al leer el archivo, retorna lista vacía
        print(f"Error leyendo {main_tf_path}: {e}")
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
    
    # Test específico para el módulo network
    network_path = os.path.join(root, "network")
    print("Testing parse_resources for network module:")
    print(f"Module path: {network_path}")
    
    network_resources = parse_resources(network_path)
    print(f"Resources found in network module: {len(network_resources)}")
    for resource in network_resources:
        print(f"  - Type: {resource['type']}, Name: {resource['name']}")
    
    print("\nTesting parse_resources for all modules:")
    # Detectar carpetas de módulo y probar parse_resources
    if os.path.exists(root):
        for item in os.listdir(root):
            module_path = os.path.join(root, item)
            if os.path.isdir(module_path):
                print(f"\nModule: {item}")
                resources = parse_resources(module_path)
                if resources:
                    for resource in resources:
                        print(f"  - {resource['type']}.{resource['name']}")
                else:
                    print("  No resources found or main.tf not exists")

if __name__ == "__main__":
    main() 