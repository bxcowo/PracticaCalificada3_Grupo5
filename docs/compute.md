# Módulo compute

El siguiente módulo de Terraform se encarga de gestionar la configuración de recursos computacionales en la infraestructura como código. Se encarga de establecer y configurar instancias computacionales según el tipo especificado, distribuyéndolas a través de múltiples subredes para garantizar alta disponibilidad y redundancia. El módulo permite definir el tamaño de las instancias (pequeño, mediano, grande) y especificar las subredes donde serán desplegados los recursos. Utiliza un enfoque basado en hash para generar identificadores únicos y asegurar la consistencia en el despliegue. Es ideal para entornos que requieren escalabilidad y distribución geográfica de cargas de trabajo computacionales.

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| tipo_instancia | string | "pequeño" | Tipo/tamaño de instancia computacional según proveedor |
| ids_subred | list(string) | ["1234", "2345", "3456"] | Lista de ids de subredes donde los recursos computacionales serán desplegados |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_computacional | Identificador del recurso computacional creado con null resource |
| prefix_recurso | Prefijo generado para el recurso de computo |
| resumen_recurso | Un resumen de la configuración del módulo de cómputo |

## Lista de recursos:
1. "null_resource" "config_compute" 

## Ejemplo de uso:
```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'tipo_instancia=mediano' \
    -var 'ids_subred=["123", "456", "789"]'
```
