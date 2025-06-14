# Módulo network

Descripción placeholder

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
