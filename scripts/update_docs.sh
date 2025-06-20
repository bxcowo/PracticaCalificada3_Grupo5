#!/usr/bin/env bash

ROOT=$(pwd)

echo " Generando documentacion y diagramas de los modulos de Terraform..."
#Aplicar Terraform init y terraform apply a cada modulo, abortar si es que falla.
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
# Generar documentacion 
echo "Generando documentacion con terraform_docs.py"
python3 scripts/terraform_docs.py
# Generar diagrama de red
echo "Generando diagrama de red con generar_diagrama.py"
python3 scripts/generar_diagrama.py

# Limpiar de archivos realizando terraform destroy en cada modulo
echo "Iniciando limpieza de recursos de cada modulo..."
for modulo_dir in $(ls -1d iac/*/ | sort -r); do
    if [ -d "$modulo_dir" ]; then
        echo "Destruyendo recursos en $modulo_dir"
        cd "$modulo_dir" 

        echo "Ejecutando terraform destroy --auto-approve en $modulo_dir"
        if ! terraform destroy --auto-approve; then
            echo "Error: terraform destroy falló en $modulo_dir"
            exit 1
        fi
        cd "$ROOT"
    else
        echo "Carpeta $modulo_dir no es un directorio valido, omitiendo"
    fi
done
echo "Limpieza de modulos completada"
