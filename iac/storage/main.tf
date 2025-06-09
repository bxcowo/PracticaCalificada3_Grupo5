locals {
  tiers_almacenamiento = {
    qwe = { desempeño = "básico", costo = "estándar", iops = 3000 }
    rty = { desempeño = "básico", costo = "optimizado", iops = 3000 }
    uio = { desempeño = "alto", costo = "premium", iops = 64000 }
    asd = { desempeño = "alto", costo = "premium", iops = 256000 }
    fgh = { desempeño = "alto", costo = "bajo", iops = 500 }
    jkl = { desempeño = "bajo", costo = "bajo", iops = 250 }
  }

  tier_elegida        = local.tiers_almacenamiento[var.tipo_almacenamiento]
  estrategia_backup   = var.dias_backup > 7 ? "integral" : "básica"
  hash_almacenamiento = md5("${var.tipo_almacenamiento}-${var.dias_backup}-${var.permite_versionado}")
}

resource "null_resource" "config_almacenamiento" {
  triggers = {
    tipo_almacenamiento = var.tipo_almacenamiento
    dias_backup         = var.dias_backup
    permite_versionado  = var.permite_versionado
    hash_almacenamiento = local.hash_almacenamiento
  }

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de almacenamiento:"
      echo "Tipo: ${var.tipo_almacenamiento}"
      echo "Retención de backups: ${var.dias_backup} días"
      echo "Versionado: ${var.permite_versionado ? "Permitido" : "No permitido"}"
    EOT
  }
}
