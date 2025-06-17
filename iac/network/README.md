## Descripción

El módulo descrito a continuación gestiona la configuración completa de la infraestructura de red en la nube. Se encarga de crear y configurar una VPC (Virtual Private Cloud) con su bloque CIDR correspondiente, estableciendo automáticamente subredes públicas y privadas distribuidas across múltiples zonas de disponibilidad para garantizar alta disponibilidad y redundancia. El módulo calcula dinámicamente la segmentación de subredes basándose en el número de zonas disponibles, creando una arquitectura de red escalable y bien distribuida. Incluye soporte para NAT Gateway que permite conectividad a internet desde subredes privadas. Es fundamental para establecer una base de red sólida y segura para toda la infraestructura.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'vpc_cidr=10.2.0.0/16' \
    -var 'zonas_disponibilidad=["USA", "Canada", "Mexico"]' \
    -var 'permitir_nat_gateway=true'
```
