## Descripción

El presente módulo de Terraform administra la configuración integral del sistema de monitoreo y alertas para la infraestructura. Se encarga de habilitar el monitoreo detallado de recursos críticos incluyendo CPU, memoria, almacenamiento y red, proporcionando alertas automáticas a través de email cuando se detectan anomalías. El módulo permite configurar períodos de retención de métricas flexibles entre 7 y 730 días, calculando automáticamente los costos asociados al monitoreo. Incluye validación de direcciones de email para garantizar la entrega correcta de notificaciones. Es esencial para mantener la salud operacional, detectar problemas proactivamente y asegurar la disponibilidad continua de servicios en entornos productivos.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'permite_monitoreo=true' \
    -var 'email_alertas=dummy@email.com' \
    -var 'dias_retencion_metricas=180'
```
