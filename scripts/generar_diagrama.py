#!/usr/bin/env python3
"""
scripts/generar_diagrama.py
- Genera docs/diagrama_red.dot a partir de los .tfstate en cada módulo
"""
import os
import json
import re

def generate_dot():
    """
    Lee terraform.tfstate de cada módulo (iac/<módulo>/terraform.tfstate)
    y extrae dependencies para formar un grafo DOT.
    """
    lineas=["digraph G {","rankdir=LR"]

    root = os.path.join(os.path.dirname(__file__), "../iac")
    patron = re.compile(r'^(?:data\.)?(.*)$')

    if not os.path.isdir(root):
        lineas.append("}")
        return "\n".join(lineas)

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

        for recurso in data.get('resources', []):
            type= recurso.get('type')
            name = recurso.get('name')
            id_recurso = f"{type}.{name}"
            lineas.append(f'    "{id_recurso}" [label="{type}.{name}"]')

            for instance in recurso.get('instances', []):
                for dep in instance.get('dependencies', []):
                    match = patron.match(dep)
                    if not match:
                        continue
                    dep_id = match.group(1)
                    lineas.append(f'    "{dep_id}" -> "{id_recurso}"')

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