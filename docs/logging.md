# Módulo logging

Descripción placeholder

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
