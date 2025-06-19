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
  - **_create_index()_**: Genera el archivo índice principal `docs/index.md` que contiene enlaces a todos los módulos documentados y referencia al diagrama de red, proporcionando un punto de entrada unificado para toda la documentación.
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

### Implementación de create_index() para generación automática del índice

Desarrollo de la función `create_index()` que automatiza la creación del archivo índice principal:
- Utiliza plantilla `template_index.md` para estructura consistente
- Escaneo automático del directorio `iac/` para detectar módulos disponibles
- Generación dinámica de enlaces Markdown a cada archivo de documentación
- Integración con el flujo de trabajo de automatización
- Creación de `docs/index.md` con navegación centralizada y referencia al diagrama de red

### Punto de entrada unificado con docs/index.md

El archivo índice generado automáticamente proporciona:
- Encabezado estándar "Documentación de Módulos IaC"
- Enlaces dinámicos a cada archivo de documentación individual
- Referencia al diagrama de red (diagrama_red.svg)
- Estructura de navegación centralizada para acceso directo a cualquier módulo


### Interpretacion del Diagrama de Red

En el archivo `diagrama_red.svg` se logra vizualizar las dependencias entre los modulos de terraform que se tiene siguiendo las siguientes conveciones.

#### **Colores por Modulo**

- **Azul**: compute
- **Verde**: logging
- **Naranja**: monitoreo
- **Rojo**: network
- **Purpura**: seguridad
- **Amarillo**: almacenamiento

#### **Conexiones y Etiquetas**

- **Flechas**: Indica la dependencia entre recursos
- **Etiqueta "depends_on"**: Muestra que un recurso depende de otro
- **Dirección**: La flecha que apunta desde la dependencia hacia el recurso dependiente


## 3. Avances desarrollados en Sprint 3
Dentro del alcance determinado para el sprint 3 se realizaron los siguiente cambios en el proyecto:

### Mejoría en `update_docs.sh`
Se dio una modificación en el archivo `update_docs.sh` para realizar una limpieza final de todas las ejecuciones de `terraform apply` mediante el comando `terraform destroy`. Esta implementación fue necesaria para asegurar que el proceso de documentación sea completamente reproducible y no deje archivos de estado residuales que puedan interferir con futuras ejecuciones. El script ahora garantiza un entorno limpio después de cada ciclo de generación de documentación, eliminando cualquier recurso temporal creado durante el proceso de apply.

### Estilizar nodos y etiquetas en `diagrama_red.dot`

Se implementaron mejoras visuales significativas en la generación del diagrama de red mediante la aplicación de estilos diferenciados por módulo. Cada nodo del diagrama ahora presenta colores específicos facilitando la identificación visual de los componentes de infraestructura. Las conexiones entre recursos se representan mediante flechas etiquetadas que indican claramente las dependencias. Esta estilización permite una interpretación más intuitiva de las relaciones entre módulos y mejora sustancialmente la legibilidad del diagrama generado.

### Completitud de módulos mediante `README.md`

Para la construcción correcta de la documentación automatizada, se expandieron los módulos de Terraform definidos mediante un archivo `README.md` incluido dentro de cada uno que incluyese una descripción de su utilidad y un ejemplo de uso mediante un comando bash con declaración de variables. Estos añadidos dieron los toques finales para la documentación automatizada de cada uno de los archivo Markdown dentro de `docs/**` fundamentalmente completando con el objetivo deseado del proyecto.

### Guía de instalación de Graphviz y nomenclatura definida

Los últimos cambios se realizaron dentro del archivo principal de `README.md` donde se amplió la sección de "Instrucciones básicas de reproduciibilidad" para corresponder a instrucciones de instalación del software Graphviz en sistemas Linux (Debian, Ubuntu y Arch) que serían de utilidad para la generación final del archivo `.svg` en el directorio `docs/**`. Así mismo también se añadió una sección de guia al usuario para que se entienda la correcta nomenclatura de los módulos IaC y que sean reconocidos mediante el script `verificar_nomenclatura.py`.


## 4. Instrucciones básicas de reproducibilidad:

Aunque no haya aún una funcionalidad establecida, es posible acceder a este proyecto mediante los siguientes pasos:
```bash
# 1. Clonar el repositorio
git clone https://github.com/bxcowo/PracticaCalificada3_Grupo5.git
cd PracticaCalificada3_Grupo5

# 2. Verificar nomenclatura de módulos (opcional)
python3 scripts/verificar_nomenclatura.py

# 3.Instalación de Graphviz

Dado que el proyecto corre en linux instalaremos la dependencia mediante los siguientes comando pues solo usando esta dependencia podremos crear el SVG a partir del archivo .dot generado

# Debian / Ubuntu

sudo apt update
sudo apt install graphviz

# Arch Linux / Manjaro

sudo pacman -S graphviz

# 4. Ejecutar el proceso completo de documentación
chmod +x scripts/update_docs.sh
./scripts/update_docs.sh

# 5. Ver la documentación generada
cd docs/
ls -la  # Verás todos los archivos .md generados
```

### Archivos generados:
- `docs/index.md` - Índice principal con enlaces a todos los módulos
- `docs/<módulo>.md` - Documentación individual de cada módulo
- `docs/diagrama_red.dot` - Diagrama de red en formato DOT
- `docs/diagrama_red.svg` - Diagrama de red en formato SVG



### Ejecución individual de componentes:
```bash
# Solo generar documentación Markdown
python3 scripts/terraform_docs.py

# Solo generar diagrama de red
python3 scripts/generar_diagrama.py

# Solo verificar nomenclatura
python3 scripts/verificar_nomenclatura.py

# Solo generar el archivo svg a partir de el archivo diagrama_red.dot
dot -Tsvg docs/diagrama_red.dot -o docs/diagrama_red.svg

```


### Convenciones de Nomenclatura para Módulos

El script `verificar_nomenclatura.py` valida que los nombres de módulos en `iac/` cumplan con el patrón establecido: `^[a-z][a-z0-9_]+$`

#### **Ejemplos de nombres CORRECTOS:**
```
compute          # OK: minúsculas
storage          # OK: minúsculas
network          # OK: minúsculas
monitoring       # OK: minúsculas
security         # OK: minúsculas
logging          # OK: minúsculas
api_gateway      # OK: minúsculas con guión bajo
data_pipeline    # OK: minúsculas con guión bajo
web_server       # OK: minúsculas con guión bajo
database_primary # OK: minúsculas con guión bajo
cache_redis      # OK: minúsculas con guión bajo
load_balancer    # OK: minúsculas con guión bajo
backup_s3        # OK: minúsculas con números y guión bajo
```

#### **Ejemplos de nombres INCORRECTOS:**
```
Compute          # ERROR: Contiene mayúsculas
STORAGE          # ERROR: Todo en mayúsculas
Network-VPC      # ERROR: Contiene guión (-)
api.gateway      # ERROR: Contiene punto (.)
_monitoring      # ERROR: Comienza con guión bajo
9security        # ERROR: Comienza con número
web server       # ERROR: Contiene espacio
database@prod    # ERROR: Contiene carácter especial (@)
load-balancer    # ERROR: Contiene guión (-)
API_Gateway      # ERROR: Contiene mayúsculas
```

#### **Reglas de nomenclatura:**
- Debe comenzar con una letra minúscula (`a-z`)
- Puede contener letras minúsculas, números y guiones bajos (`a-z`, `0-9`, `_`)
- No puede contener mayúsculas, guiones (-), puntos (.), espacios o caracteres especiales
- No puede comenzar con números o guiones bajos

#### **Verificación:**
```bash
# Validar nomenclatura de todos los módulos
python3 scripts/verificar_nomenclatura.py
```


# Entregables por sprint
Aquí se encuentran los videos explicativos sobre la colaboración de cada uno de los integrantes, además de la sustentación de cada modificación, mencionando también posibles retos que se encuentren durante el desarrollo

- **Video Sprint 1**: https://unipe-my.sharepoint.com/:v:/g/personal/a_flores_a_uni_pe/EaUcPsK_EINJk2p2Pyk5JXIBswQuvG7-clWvL5UooLAjYQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=zwEeWw

- **Video Sprint 2**:
https://unipe-my.sharepoint.com/:v:/g/personal/a_flores_a_uni_pe/EQx9SrEyp8tOjemAQ_W-fCYB6dVzZJMCIkIJDNh6bvSbYA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=3Yco2v
