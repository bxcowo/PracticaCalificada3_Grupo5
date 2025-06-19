## Descripción

El siguiente módulo de Terraform gestiona la configuración completa del sistema de almacenamiento para la infraestructura. Se encarga de establecer diferentes niveles de almacenamiento con características específicas de rendimiento, costo y IOPS según las necesidades del proyecto. El módulo administra estrategias de backup diferenciadas (básica e integral) basándose en los períodos de retención configurados, y proporciona capacidades de versionado para objetos almacenados. Define automáticamente tiers de almacenamiento con diferentes perfiles de desempeño y costo, permitiendo optimizar tanto la performance como los gastos operacionales. Es fundamental para garantizar la persistencia, disponibilidad y protección de datos críticos en entornos productivos que requieren diferentes niveles de servicio de almacenamiento.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'tipo_almacenamiento=uio' \
    -var 'dias_backup=14' \
    -var 'permite_versionado=true'
```
