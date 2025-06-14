# Módulo monitoring

Descripción placeholder

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| permite_monitoreo | bool | true | Permite un monitoreo detallado con alarmas |
| email_alertas | string | "dummy123@gmail.com" | Dirección de email para recibir alertas por monitoreo |
| dias_retencion_metricas | number | 90 | Número de días de retención de métricas de recursos |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_monitoreo | Identificador único de la configuración de monitorización creado por null resource |
| config_alertas | Detalles de configuración para alertas de monitoreo |
| estimacion_costo | Estimado del costo total por días de monitoreo |

## Lista de recursos:
1. "null_resource" "config_monitoreo" 
