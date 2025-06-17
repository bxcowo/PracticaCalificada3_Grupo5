# Módulo network

El módulo descrito a continuación gestiona la configuración completa de la infraestructura de red en la nube. Se encarga de crear y configurar una VPC (Virtual Private Cloud) con su bloque CIDR correspondiente, estableciendo automáticamente subredes públicas y privadas distribuidas across múltiples zonas de disponibilidad para garantizar alta disponibilidad y redundancia. El módulo calcula dinámicamente la segmentación de subredes basándose en el número de zonas disponibles, creando una arquitectura de red escalable y bien distribuida. Incluye soporte para NAT Gateway que permite conectividad a internet desde subredes privadas. Es fundamental para establecer una base de red sólida y segura para toda la infraestructura.

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| vpc_cidr | string | "10.0.0.0/16" | Bloque CIDR declarada para una VPC(Virtual Private Cloud) |
| zonas_disponibilidad | list(string) | ["Canada", "USA", "Australia", "Peru"] | Lista de zonas de disponibilidad a donde redistribuir los recursos existentes |
| permitir_nat_gateway | bool | true | Habilitar Gateway NAT para permitir acceso a internet desde subredes privadas. |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_red | Identificador único de la configuración de red creada por null resource |
| resumen_red | Un resumen de la configuración del módulo de red |
| direccion_subredes | Direcciones de subredes de CIDR por zona de disponibilidad |

## Lista de recursos:
1. "null_resource" "red_config" 

## Ejemplo de uso:
```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'vpc_cidr=10.2.0.0/16' \
    -var 'zonas_disponibilidad=["USA", "Canada", "Mexico"]' \
    -var 'permitir_nat_gateway=true'
```
