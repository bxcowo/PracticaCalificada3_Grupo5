output "id_config_logging" {
  description = "Identificador único de la configuración de logging creado por null resource"
  value       = null_resource.config_logging.id
}

output "grupos_log" {
  description = "Lista de grupos log a crearse"
  value       = local.grupos_log
}

output "resumen_logging" {
  description = "Un resumen de la configuración de logging"
  value = {
    dias_retencion_logs    = var.dias_retencion_logs
    nivel_log              = var.nivel_log
    permite_auditoria_logs = var.permite_auditoria_logs
    costo_estimado_logging = local.costo_logging_total
  }
}
