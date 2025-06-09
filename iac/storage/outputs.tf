output "id_config_almacenamiento" {
  description = "Identificador único de la configuración de almacenamiento creado por null resource"
  value       = null_resource.config_almacenamiento.id
}

output "resumen_almacenamiento" {
  description = "Un resumen de la configuración del módulo de almacenamiento"
  value = {
    tipo               = var.tipo_almacenamiento
    desempeño_tier     = local.tier_elegida.desempeño
    costo_tier         = local.tier_elegida.costo
    iops_tier          = local.tier_elegida.iops
    dias_backup        = var.dias_backup
    estrategia_backup  = local.estrategia_backup
    permite_versionado = var.permite_versionado
  }
}

output "proteccion_datos" {
  description = "Protección de datos y configuración de backups"
  value = {
    dias_backup        = var.dias_backup
    estrategia_backup  = local.estrategia_backup
    permite_versionado = var.permite_versionado
  }
}
