# Módulo storage

El siguiente módulo de Terraform gestiona la configuración completa del sistema de almacenamiento para la infraestructura. Se encarga de establecer diferentes niveles de almacenamiento con características específicas de rendimiento, costo y IOPS según las necesidades del proyecto. El módulo administra estrategias de backup diferenciadas (básica e integral) basándose en los períodos de retención configurados, y proporciona capacidades de versionado para objetos almacenados. Define automáticamente tiers de almacenamiento con diferentes perfiles de desempeño y costo, permitiendo optimizar tanto la performance como los gastos operacionales. Es fundamental para garantizar la persistencia, disponibilidad y protección de datos críticos en entornos productivos que requieren diferentes niveles de servicio de almacenamiento.

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

## Ejemplo de uso:
```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'tipo_almacenamiento=uio' \
    -var 'dias_backup=14' \
    -var 'permite_versionado=true'
```
