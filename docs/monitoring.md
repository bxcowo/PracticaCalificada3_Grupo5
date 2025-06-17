# Módulo monitoring

El presente módulo de Terraform administra la configuración integral del sistema de monitoreo y alertas para la infraestructura. Se encarga de habilitar el monitoreo detallado de recursos críticos incluyendo CPU, memoria, almacenamiento y red, proporcionando alertas automáticas a través de email cuando se detectan anomalías. El módulo permite configurar períodos de retención de métricas flexibles entre 7 y 730 días, calculando automáticamente los costos asociados al monitoreo. Incluye validación de direcciones de email para garantizar la entrega correcta de notificaciones. Es esencial para mantener la salud operacional, detectar problemas proactivamente y asegurar la disponibilidad continua de servicios en entornos productivos.

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

## Ejemplo de uso:
```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'permite_monitoreo=true' \
    -var 'email_alertas=dummy@email.com' \
    -var 'dias_retencion_metricas=180'
```
