#!/usr/bin/env python3

"""
scripts/terraform_docs.py
Recorre cada módulo en iac/ y genera archivos Markdown en docs/<módulo>.md
"""
import os
import re
import json
import sys
from string import Template

def parse_variables(modulo_path):
    """
    Lee variables.tf y extrae nombre, tipo, default y descripción.
    Retorna: [{ "name": str, "type": str, "default": str, "description": str }]
    """
    variables_tf_path = os.path.join(modulo_path, "variables.tf")

    # Si no existe variables.tf, retorna lista vacía sin excepciones
    if not os.path.exists(variables_tf_path):
        return []

    try:
        with open(variables_tf_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex para extraer bloques de variables completos
        # Busca 'variable "nombre" {' hasta el cierre del bloque con '}'
        # Usa un enfoque de conteo de llaves para manejar bloques anidados
        variables = []

        # Patrón para encontrar el inicio de un bloque variable
        variable_pattern = r'variable\s+"([^"]+)"\s*\{'

        # Encontrar todas las posiciones de inicio de variables
        for match in re.finditer(variable_pattern, content):
            var_name = match.group(1)
            start_pos = match.end()

            # Encontrar el final del bloque contando llaves
            brace_count = 1
            end_pos = start_pos

            while end_pos < len(content) and brace_count > 0:
                if content[end_pos] == '{':
                    brace_count += 1
                elif content[end_pos] == '}':
                    brace_count -= 1
                end_pos += 1

            # Extraer el contenido del bloque
            block_content = content[start_pos:end_pos-1]

            # Extraer información específica del bloque
            var_info = {
                "name": var_name,
                "type": "string",  # valor por defecto
                "default": "N/A",  # valor por defecto
                "description": "No description provided"  # valor por defecto
            }

            # Extraer descripción
            desc_match = re.search(r'description\s*=\s*"([^"]*)"', block_content)
            if desc_match:
                var_info["description"] = desc_match.group(1)

            # Extraer tipo
            type_match = re.search(r'type\s*=\s*(\w+(?:\([^)]*\))?)', block_content)
            if type_match:
                var_info["type"] = type_match.group(1)

            # Extraer default (puede ser string, number, bool, list, etc.)
            # Buscar diferentes formatos de default
            default_match = re.search(r'default\s*=\s*([^}\n]*?)(?=\n|\s*validation|\s*$)', block_content, re.DOTALL)
            if default_match:
                default_value = default_match.group(1).strip()
                # Limpiar el valor (remover comentarios y espacios extra)
                default_value = re.sub(r'\s*#.*$', '', default_value, flags=re.MULTILINE)
                default_value = default_value.strip()
                if default_value:
                    var_info["default"] = default_value

            variables.append(var_info)

        return variables

    except Exception as e:
        # En caso de error al leer el archivo, retorna lista vacía
        print(f"Error leyendo {variables_tf_path}: {e}")
        return []

def parse_outputs(modulo_path):
    """
    Lee outputs.tf y extrae nombre y descripción.
    Retorna: [{ "name": str, "description": str }]
    """
    outputs_tf_path = os.path.join(modulo_path, "outputs.tf")

    # Si no existe outputs.tf, retorna lista vacía sin excepciones
    if not os.path.exists(outputs_tf_path):
        return []

    try:
        with open(outputs_tf_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex para extraer bloques de outputs completos
        outputs = []

        # Patrón para encontrar el inicio de un bloque output
        output_pattern = r'output\s+"([^"]+)"\s*\{'

        # Encontrar todas las posiciones de inicio de outputs
        for match in re.finditer(output_pattern, content):
            output_name = match.group(1)
            start_pos = match.end()

            # Encontrar el final del bloque contando llaves
            brace_count = 1
            end_pos = start_pos

            while end_pos < len(content) and brace_count > 0:
                if content[end_pos] == '{':
                    brace_count += 1
                elif content[end_pos] == '}':
                    brace_count -= 1
                end_pos += 1

            # Extraer el contenido del bloque
            block_content = content[start_pos:end_pos-1]

            # Extraer información específica del bloque
            output_info = {
                "name": output_name,
                "description": "No description provided"  # valor por defecto
            }

            # Extraer descripción
            desc_match = re.search(r'description\s*=\s*"([^"]*)"', block_content)
            if desc_match:
                output_info["description"] = desc_match.group(1)

            outputs.append(output_info)

        return outputs

    except Exception as e:
        # En caso de error al leer el archivo, retorna lista vacía
        print(f"Error leyendo {outputs_tf_path}: {e}")
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

def write_markdown():
    """
    Por cada módulo, escribe docs/<módulo>.md con:
    - Encabezado
    - Descripción placeholder (100 palabras)
    - Tabla de variables
    - Tabla de outputs
    - Lista de recursos
    """

    # Definición de rutas de interes
    root = os.path.join(os.path.dirname(__file__), "../iac")
    docs_ruta = os.path.join(os.path.dirname(__file__), "../docs")

    # Verificación de existencia de rutas
    if not os.path.isdir(root):
        print(f"ERROR: No se encontro el directorio '{root}' ")
        sys.exit(1)

    # Verificación de existencia de directorio 'docs', sino lo crea
    if not os.path.isdir(docs_ruta):
        print(f"ERROR: No se encontro el directorio '{docs_ruta}' ")
        print("Creando...")
        try:
            os.mkdir(docs_ruta)
        except PermissionError:
            print("Permisos denegados")

    # Declaración de plantilla para la documentación creada en Markdown
    template_route = os.path.join(os.path.dirname(__file__), 'templates', 'template.md')

    with open(template_route, 'r', encoding='utf-8') as temp:
        doc_template = Template(temp.read())

    # Iteración por todos los módulos dentro del directorio iac
    for nombre in os.listdir(root):
        modulo_path = os.path.join(root, nombre)

        # Descripción a realizarse por módulo (se espera una mejora en futuros avances)
        descripcion = "Descripción placeholder"

        # Obtención de información sobre variables en el módulo presente
        parsed_variables = parse_variables(modulo_path)
        filas_variables = "\n".join([f"| {var['name']} | {var['type']} | {var['default']} | {var['description']} |" for var in parsed_variables])

        # Obtención de información sobre outputs en el módulo presente
        parsed_outputs = parse_outputs(modulo_path)
        filas_outputs = "\n".join([f"| {out['name']} | {out['description']} |" for out in parsed_outputs])

        # Obtención de información sobre recursos en el módulo presente
        parsed_recursos = parse_resources(modulo_path)
        filas_recursos = "\n".join([f"{i+1}. \"{res['type']}\" \"{res['name']}\" " for i, res in enumerate(parsed_recursos)])

        # Creación y escritura de archivo Markdown en base al template y a los datos obtenidos
        with open(f'{docs_ruta}/{nombre}.md', 'w') as doc:
            contenido = doc_template.substitute(
                titulo = nombre,
                descripcion = descripcion,
                filas_variables = filas_variables,
                filas_outputs = filas_outputs,
                filas_recursos = filas_recursos
            )
            doc.write(contenido)

def create_index():
    """
    Dentro del directorio docs, escribe index.md.
    Este archivo contiene enlaces a los resúmenes de los módulos encontrados,
    también enlaza a un diagrama de red generado de estos módulos.`
    """
    root = os.path.join(os.path.dirname(__file__), '../iac')
    docs_ruta = os.path.join(os.path.dirname(__file__), "../docs")
    template_route = os.path.join(os.path.dirname(__file__), 'templates', 'template_index.md')

    with open(template_route, 'r', encoding='utf-8') as temp:
        index_template = Template(temp.read())

    enlaces_filas = "\n".join([f'- [{nombre}]({nombre}.md)' for nombre in os.listdir(root)])

    with open(os.path.join(docs_ruta, 'index.md'), 'w') as index:
        contenido = index_template.substitute(
            enlaces_filas = enlaces_filas
        )
        index.write(contenido)


def main():
    root = os.path.join(os.path.dirname(__file__), "../iac")

    # Test para función parse_resource()
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

    # Test para función write_markdown() y create_index()
    print("\n\nTesting write_markdown for modules in iac and create_index")
    write_markdown()
    create_index()
    docs_route = os.path.join(os.path.dirname(__file__), "../docs")
    print("Se han creado los siguientes archivos con el siguiente contenido:")
    markdonws_creados = [file for file in os.listdir(docs_route) if os.path.isfile(os.path.join(docs_route, file))]

    for doc in markdonws_creados:
        file_path = os.path.join(docs_route, doc)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                contenido = file.read()
                print(f"Archivo: {doc}")
                print(f"Contenido: \n{contenido}")
                print("-" * 50)
        except Exception as e:
            print(f"Error al leer el archivo {doc}: {e}")

if __name__ == "__main__":
    main()
