# Módulo storage

Descripción placeholder

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| tipo_almacenamiento | string | "rty" | Tipo de almacenamiento primario para consistencia de datos |
| dias_backup | number | 7 | Número de días de retención de backups |
| permite_versionado | bool | false | Permitir versionamiento para objetos almacenados |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_almacenamiento | Identificador único de la configuración de almacenamiento creado por null resource |
| resumen_almacenamiento | Un resumen de la configuración del módulo de almacenamiento |
| proteccion_datos | Protección de datos y configuración de backups |

## Lista de recursos:
1. "null_resource" "config_almacenamiento" 
