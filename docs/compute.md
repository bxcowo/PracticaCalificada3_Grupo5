# Módulo compute

Descripción placeholder

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
