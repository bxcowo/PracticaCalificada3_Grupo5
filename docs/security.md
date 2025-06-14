# Módulo security

Descripción placeholder

## Tabla de variables:
| Nombre | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| permite_encriptacion | bool | true | Permite encriptacion para todos los recursos disponibles |
| bloques_CIDR_permitidos | list(string) | [] | Lista de bloques CIDR permitidos a tener acceso a recursos |
| nivel_seguridad | string | "estandar" | Nivel de seguridad establecida (basico, estandar, alto, critico) |

## Tabla de outputs:
| Nombre | Descripción |
|--------|-------------|
| id_config_seguridad | Identificador único de la configuración de seguridad creado por null resource |
| resumen_seguridad | Un resumen de la configuración del módulo de seguridad |
| requerimientos_politicas | Políticas de seguridad requeridas para el actual nivel de seguridad |

## Lista de recursos:
1. "null_resource" "config_seguridad" 
