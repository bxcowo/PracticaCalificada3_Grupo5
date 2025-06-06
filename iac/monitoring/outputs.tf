output "id_config_monitoreo" {
  description = "Identificador único de la configuración de monitorización creado por null resource"
  value       = null_resource.config_monitoreo.id
}

output "config_alertas" {
  description = "Detalles de configuración para alertas de monitoreo"
  value = {
    permite_monitoreo = var.permite_monitoreo
    email_alertas     = var.email_alertas
    tipo_alertas      = local.tipo_alertas
  }
}

output "estimacion_costo" {
  description = "Estimado del costo total por días de monitoreo"
  value = {
    costo_monitoreo_total   = local.costo_monitoreo_total
    dias_retencion_metricas = var.dias_retencion_metricas
  }
}
