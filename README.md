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

## 2. Avances desarrollados en Sprint 2:

Durante este segundo sprint hemos completado la funcionalidad principal del sistema de documentación automática, implementando las funciones de parsing y automatización que constituyen el núcleo operativo del proyecto.

### Implementación completa de funciones de parsing en terraform_docs.py

Se completaron las funciones fundamentales que permiten la extracción automática de información desde los archivos Terraform:

**parse_resources(modulo_path)**: 
- Analiza archivos `main.tf` utilizando expresiones regulares para identificar declaraciones de recursos
- Extrae patrones `resource "<tipo>" "<nombre>"` y los estructura en diccionarios con claves "type" y "name"
- Implementa manejo robusto de errores, retornando lista vacía cuando no existe el archivo main.tf
- Probado exitosamente en todos los módulos, identificando recursos tipo `null_resource` en cada uno

**parse_variables(modulo_path)**:
- Lee archivos `variables.tf` implementando parsing avanzado con regex y conteo de llaves para manejar bloques anidados
- Extrae información completa de variables: nombre, tipo, valor por defecto y descripción
- Maneja bloques de validación anidados sin interferir con la extracción principal
- Retorna estructura de diccionarios con claves "name", "type", "default", "description"
- Procesamiento exitoso de 18 variables distribuidas entre los 6 módulos

**parse_outputs(modulo_path)**:
- Procesa archivos `outputs.tf` utilizando técnicas similares de parsing con conteo de llaves
- Extrae nombre y descripción de cada output definido
- Estructura los datos en diccionarios con claves "name" y "description"
- Manejo graceful de archivos inexistentes mediante retorno de listas vacías
- Procesamiento exitoso de 18 outputs distribuidos entre los 6 módulos

### Validación de nomenclatura con verificar_nomenclatura.py

Se implementó el sistema de validación de convenciones de nomenclatura:
- Escaneo automático del directorio `iac/` aplicando regex
- Reporte estructurado con mensajes "OK: <módulo>" para nombres válidos
- Identificación de violaciones con "ERROR: <módulo> no cumple convención"
- Terminación con código de error apropiado usando `sys.exit(1)` cuando detecta fallos
- Validación exitosa de los 6 módulos existentes: compute, logging, monitoring, network, security, storage

### Generación automatizada de documentación Markdown

La función `write_markdown()` produce documentación estructurada para cada módulo:
- Encabezados consistentes con formato `# Módulo <nombre>`
- Secciones organizadas: descripción placeholder, tablas de variables, tablas de outputs, lista de recursos
- Integración completa con las funciones de parsing implementadas
- Generación de 6 archivos de documentación correspondientes a cada módulo
- Formato de tablas Markdown estándar con encabezados apropiados

### Automatización completa con update_docs.sh

Script de automatización que ejecuta el flujo completo:
- Iteración sobre cada módulo en `iac/` ejecutando `terraform init` y `terraform apply -auto-approve`
- Manejo de errores con terminación apropiada en caso de fallos de Terraform
- Ejecución secuencial de `terraform_docs.py` y `generar_diagrama.py`
- Retorno al directorio raíz para mantener consistencia de rutas
- Preparación del entorno para la generación automatizada de documentación

### Punto de entrada unificado con docs/index.md

Creación del archivo índice principal que proporciona:
- Encabezado estándar "Documentación de Módulos IaC"
- Enlaces Markdown a cada archivo de documentación individual
- Referencia preparatoria al diagrama de red (diagrama_red.svg)
- Estructura de navegación centralizada para acceso directo a cualquier módulo


## 3. Instrucciones básicas de reproducibilidad:
Aunque no haya aún una funcionalidad establecida, es posible acceder a este proyecto mediante los siguientes pasos:
```bash
git clone https://github.com/bxcowo/PracticaCalificada3_Grupo5.git
cd PracticaCalificada3_Grupo5
```


# Entregables por sprint
Aquí se encuentran los videos explicativos sobre la colaboración de cada uno de los integrantes, además de la sustentación de cada modificación, mencionando también posibles retos que se encuentren durante el desarrollo

- **Video Sprint 1**: https://unipe-my.sharepoint.com/:v:/g/personal/a_flores_a_uni_pe/EaUcPsK_EINJk2p2Pyk5JXIBswQuvG7-clWvL5UooLAjYQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=zwEeWw


