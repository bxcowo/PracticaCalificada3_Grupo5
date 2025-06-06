locals {
  tipo_alertas          = var.permite_monitoreo ? ["cpu", "memoria", "almacenamiento", "red"] : []
  costo_monitoreo_total = var.permite_monitoreo ? var.dias_retencion_metricas * 0.55 : 0
  hash_config           = md5("${var.permite_monitoreo}-${var.email_alertas}-${var.dias_retencion_metricas}")
}

resource "null_resource" "config_monitoreo" {
  triggers = {
    permite_monitoreo       = var.permite_monitoreo
    email_alertas           = var.email_alertas
    dias_retencion_metricas = var.dias_retencion_metricas
    setup_hash              = local.hash_config
  }

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de monitorización:"
      echo "Estado: ${var.permite_monitoreo ? "Permitido" : "No permitido"}"
      echo "Email para alertas: ${var.email_alertas}"
      echo "Retención de métricas: ${var.dias_retencion_metricas} días"
    EOT
  }
}
