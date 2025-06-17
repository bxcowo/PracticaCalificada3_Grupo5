#!/usr/bin/env python3
"""
scripts/generar_diagrama.py
- Genera docs/diagrama_red.dot a partir de los .tfstate en cada módulo
- Colorea nodos según tipo de módulo y etiqueta dependencias
"""
import os
import json
import re

def get_module_color(module_name):
    """
    Retorna el color DOT apropiado para cada tipo de módulo.
    """
    color_map = {
        'network': 'blue',
        'compute': 'green', 
        'storage': 'orange',
        'security': 'red',
        'logging': 'purple',
        'monitoring': 'yellow'
    }
    return color_map.get(module_name, 'gray')

def generate_dot():
    """
    Lee terraform.tfstate de cada módulo (iac/<módulo>/terraform.tfstate)
    y extrae dependencies para formar un grafo DOT con colores y etiquetas.
    """
    lineas=["digraph G {","rankdir=LR"]

    root = os.path.join(os.path.dirname(__file__), "../iac")
    patron = re.compile(r'^(?:data\.)?(.*)$')

    if not os.path.isdir(root):
        lineas.append("}")
        return "\n".join(lineas)

    recurso_a_modulo = {}

    for modulo in os.listdir(root):
        modulo_dir=os.path.join(root, modulo)
        tfstate=os.path.join(modulo_dir, "terraform.tfstate")

        if not os.path.isfile(tfstate):
            continue

        try:
            with open(tfstate, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (IOError, json.JSONDecodeError):
            continue

        color = get_module_color(modulo)

        for recurso in data.get('resources', []):
            type= recurso.get('type')
            name = recurso.get('name')
            id_recurso = f"{type}.{name}"
            
            recurso_a_modulo[id_recurso] = modulo
            
            lineas.append(f'    "{id_recurso}" [label="{type}.{name}", color={color}]')

            for instance in recurso.get('instances', []):
                for dep in instance.get('dependencies', []):
                    match = patron.match(dep)
                    if not match:
                        continue
                    dep_id = match.group(1)
                    
                    lineas.append(f'    "{dep_id}" -> "{id_recurso}" [label="depends_on"]')

    lineas.append("}")
    return "\n".join(lineas)


def main():
    
    dot= generate_dot()
    os.makedirs("docs", exist_ok=True)
    output="docs/diagrama_red.dot"
    with open(output, 'w', encoding='utf-8') as f:
        f.write(dot)
    print(f"Diagrama generado en {output}")

if __name__ == "__main__":
    main() 