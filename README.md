# Nombre del proyecto: **Sistema de documentación automática de módulos IaC y diagrama de red**

Este pequeño proyecto consiste en la creación de un generador automático de documentación local para un conjunto de módulos Terraform dummy.

Para este 1º sprint hemos desarrollado la siguiente estructura de directorios y archivos:

```
├─ iac/
│   ├─ compute/
│   │   ├ main.tf
│   │   ├ variables.tf
│   │   └ outputs.tf
│   ├─ logging/
│   ├─ monitoring/
│   ├─ network/
│   ├─ security/
│   └─ storage/
├─ scripts/
│   ├─ generar_diagrama.py
│   ├─ terraform_docs.py
│   ├─ update_docs.sh
│   └─ verificar_nomenclatura.py
├─ docs/
├─ README.md
├─ LICENSE
└─ .gitignore
```

## 1. Avances desarrollados:
Nuestro alcance establecido en este 1º sprint fue la de cimentar la estructura del proyecto a desarrollar. Se dio una división estructural entre los módulos de Terraform correspondientes y los scripts principales en sus respectivos directorios.
Dentro de la carpeta `iac/` se tienen divididos 6 módulos principales:
|  |  |
|---|---|
| compute   | storage   |
| logging  | security   |
| monitoring   | network   |

Cada uno de estos módulos se descompone en 3 archivos Terraform estándar:

- **main.tf**: Contiene la lógica principal del módulo utilizando `null_resource` con provisioners `local-exec` para simular la configuración de infraestructura. Incluye bloques `locals` que realizan cálculos específicos como:
  - Generación de hashes MD5 para triggers de configuración
  - Cálculos de costos estimados (NAT Gateway, monitoreo, logging)
  - Lógica condicional para configuraciones (alertas, políticas de seguridad, estrategias de backup)
  - Procesamiento de listas y mapas (subredes, políticas, tiers de almacenamiento)

- **variables.tf**: Define las variables de entrada con validaciones robustas específicas para cada dominio:
  - **_compute**: Comprobación de tipos de instancia e IDs de subred
  - **_logging_**: Rangos de retención y niveles de log válidos
  - **_monitoring_**: Chequeo de formato de email y rangos de retención de métricas
  - **_network_**: Validación de bloques CIDR y zonas de disponibilidad mínimas
  - **_security_**: Revisión de bloque CIDR para VPC y niveles de seguridad predefinidos
  - **_storage_**: Inspección de tipos de almacenamiento codificados y días de backup

- **outputs.tf**: Expone información estructurada post-configuración, incluyendo:
  - IDs únicos de recursos creados por `null_resource`
  - Resúmenes de configuración con datos computados
  - Datos derivados de los cálculos en `locals` (direcciones de subredes, políticas de seguridad, estimaciones de costo)

Dentro de la carpeta `scripts/` encontraremos 4 scripts fundamentales de nuestro proyecto:
- **generar_diagrama.py**: Genera un diagrama de red en formato DOT mediante la función `generate_dot()` leyendo los archivos de Terraform de estado `(.tfstate)` de cada módulo. Se espera crear una representación visual de la infraestructura y generar una salida en el directorio `docs/`.
- **terraform_docs.py**: Script python principal con 4 funciones fundamentales de operación:
  - **_parse_variables()_**: Analiza el archivo `variables.tf` de cada módulo y extrae los nombres, tipos, valores predeterminados y descripciones de las variables.
  - **_parse_outputs()_**: Lee el archivo `outputs.tf` de cada módulo y extrae los nombres y descripciones de las salidas definidas.
  - **_parse_resources()_**: Examina el archivo `main.tf` para identificar y extraer los recursos de Terraform (tipo y nombre) que se crean en el módulo.
  - **_write_markdown()_**: Genera archivos de documentación en formato Markdown para cada módulo, estructurando la información en secciones con encabezado, descripción, tablas de variables, de outputs y listas de recursos.
- **update_docs.sh**: Script bash principal para la automatización de documentación iterando sobre cada módulo de IaC, ejecutando los comandos `terraform init` y `terraform apply` para luego ejecutar los scripts `terraform_docs.py` y `generar_diagrama.py` para finalizar con el ciclo de ejecución principal de nuestro proyecto.
- **verificar_nomenclatura.py**: Validador de nombres de módulos en el directorio `iac/` siguiendo un patrón de nomenclatura establecido, escanea e identifica posibles violaciones de nomenclatura y reporta cualquier nombre no conforme en la consola.

## 2. Instrucciones básicas de reproducibilidad:
Aunque no haya aún una funcionalidad establecida, es posible acceder a este proyecto mediante los siguientes pasos:
```bash
git clone https://github.com/bxcowo/PracticaCalificada3_Grupo5.git
cd PracticaCalificada3_Grupo5
```


# Entregables por sprint
Aquí se encuentran los videos explicativos sobre la colaboración de cada uno de los integrantes, además de la sustentación de cada modificación, mencionando también posibles retos que se encuentren durante el desarrollo

- **Video Sprint 1**: https://unipe-my.sharepoint.com/:v:/g/personal/a_flores_a_uni_pe/EaUcPsK_EINJk2p2Pyk5JXIBswQuvG7-clWvL5UooLAjYQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=zwEeWw


