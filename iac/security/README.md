## Descripción

Este módulo presenta una implementación completa de Terraform para administrar la configuración integral de seguridad en toda la infraestructura. Se encarga de establecer políticas de seguridad diferenciadas por niveles (básico, estándar, alto, crítico), cada uno con controles específicos como autenticación multifactor, encriptación, logging de accesos y detección de intrusiones. El módulo gestiona la habilitación de encriptación para todos los recursos, define bloques CIDR permitidos para controlar el acceso de red, y implementa automáticamente las políticas de seguridad correspondientes al nivel seleccionado. Incluye detección de configuraciones de acceso abierto y genera identificadores únicos para garantizar la consistencia. Es esencial para mantener la postura de seguridad y cumplimiento normativo en entornos productivos.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'permite_encriptacion=true' \
    -var 'bloques_CIDR_permitidos=["10.0.0.0/16", "172.16.0.0/12"]' \
    -var 'nivel_seguridad=alto'
```
