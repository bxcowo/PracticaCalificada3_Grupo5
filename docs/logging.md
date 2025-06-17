# Módulo logging

A continuación se presenta un módulo de Terraform que gestiona la configuración completa del sistema de logging para la infraestructura. Se encarga de establecer políticas de retención de logs, definir niveles mínimos de registro y habilitar capacidades de auditoría según los requerimientos de cumplimiento. El módulo configura automáticamente grupos de logs diferenciados (aplicación, sistema, auditoría) basándose en las configuraciones establecidas. Calcula costos estimados de almacenamiento y proporciona flexibilidad para ajustar la retención de logs desde 1 hasta 365 días. Es fundamental para el monitoreo, debugging y cumplimiento de normativas en entornos productivos que requieren trazabilidad completa de eventos.

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| dias_retencion_logs | number | 30 | Número de días de retención de log de aplicación |
| nivel_log | string | "INFO" | Nivel mínimo de logging definido para los logs de aplicación |
| permite_auditoria_logs | bool | false | Permite la auditoria de logs para el cumplimiento de requerimientos |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_logging | Identificador único de la configuración de logging creado por null resource |
| grupos_log | Lista de grupos log a crearse |
| resumen_logging | Un resumen de la configuración de logging |

## Lista de recursos:
1. "null_resource" "config_logging" 

## Ejemplo de uso:
```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'dias_retencion_logs=60' \
    -var 'nivel_log=WARN' \
    -var 'permite_auditoria_logs=true'
```
