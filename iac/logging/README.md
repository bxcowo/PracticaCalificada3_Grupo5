## Descripción

A continuación se presenta un módulo de Terraform que gestiona la configuración completa del sistema de logging para la infraestructura. Se encarga de establecer políticas de retención de logs, definir niveles mínimos de registro y habilitar capacidades de auditoría según los requerimientos de cumplimiento. El módulo configura automáticamente grupos de logs diferenciados (aplicación, sistema, auditoría) basándose en las configuraciones establecidas. Calcula costos estimados de almacenamiento y proporciona flexibilidad para ajustar la retención de logs desde 1 hasta 365 días. Es fundamental para el monitoreo, debugging y cumplimiento de normativas en entornos productivos que requieren trazabilidad completa de eventos.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'dias_retencion_logs=60' \
    -var 'nivel_log=WARN' \
    -var 'permite_auditoria_logs=true'
```
