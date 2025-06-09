locals {
  hash_config         = md5("${var.dias_retencion_logs}-${var.nivel_log}-${var.permite_auditoria_logs}")
  grupos_log          = var.permite_auditoria_logs ? ["aplicación", "auditoría", "sistema"] : ["aplicación", "sistema"]
  costo_logging_total = var.dias_retencion_logs * 0.50
}

resource "null_resource" "config_logging" {
  triggers = {
    dias_retencion_logs    = var.dias_retencion_logs
    nivel_log              = var.nivel_log
    permite_auditoria_logs = var.permite_auditoria_logs
    hash_config            = local.hash_config
  }

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de logging:"
      echo "Retención de logs: ${var.dias_retencion_logs} días"
      echo "Nivel mínimo de logging: ${var.nivel_log}"
      echo "Auditoría de logs: ${var.permite_auditoria_logs ? "Permitido" : "No permitido"}"
    EOT
  }
}
