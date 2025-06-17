## Descripción

El siguiente módulo de Terraform se encarga de gestionar la configuración de recursos computacionales en la infraestructura como código. Se encarga de establecer y configurar instancias computacionales según el tipo especificado, distribuyéndolas a través de múltiples subredes para garantizar alta disponibilidad y redundancia. El módulo permite definir el tamaño de las instancias (pequeño, mediano, grande) y especificar las subredes donde serán desplegados los recursos. Utiliza un enfoque basado en hash para generar identificadores únicos y asegurar la consistencia en el despliegue. Es ideal para entornos que requieren escalabilidad y distribución geográfica de cargas de trabajo computacionales.

## Ejemplo de uso

```bash
#!/bin/bash
terraform apply -auto-approve \
    -var 'tipo_instancia=mediano' \
    -var 'ids_subred=["123", "456", "789"]'
```
