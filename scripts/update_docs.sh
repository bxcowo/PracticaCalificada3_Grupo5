#!/usr/bin/env bash

ROOT=$(pwd)

echo " Gneracndo documentacion y diagramas de los modulos de Terraform..."

for modulo_dir in iac/*/; do 
    if [ -d "$modulo_dir" ];then 
        echo "Procesando modulo: $modulo_dir"
        cd "$modulo_dir" || continue

        echo "Ejecutando terraform init en $modulo_dir"
        terraform init

        echo "Ejecutando terraform apply --auto-approve en $modulo_dir"
        if ! terraform apply --auto-approve; then
            echo "Error: terraform apply falló en $modulo_dir"
            exit 1
        fi

        cd "$ROOT"
    else
    echo "Carpeta $modulo_dir no es un directorio valido, omitiendo"
    fi
done

echo "Generando documentaci+on con terraform_docs.py"
python3 scripts/terraform_docs.py

echo "Gnerando diagrama de red con generar_diagrama.py"
python3 scripts/generar_diagrama.py

echo "Generacion de documentacion completada."