data "terraform_remote_state" "network" {
  backend = "local"
  config = {
    path = "../network/terraform.tfstate"
  }
}

locals {
  def_politica = {
    basico   = ["contraseña_requerida", "mfa_habilitado"]
    estandar = ["contraseña_requerida", "mfa_habilitado", "encriptacion_al_suspendido", "acceso_log"]
    alto     = ["contraseña_requerida", "mfa_habilitado", "encriptacion_al_suspendido", "acceso_log", "escaneo_vulnerabilidades"]
    critico  = ["contraseña_requerida", "mfa_habilitado", "encriptacion_al_suspendido", "acceso_log", "escaneo_vulnerabilidades", "deteccion_intruso", "clasificacion_datos"]
  }

  hash_seguridad  = md5("${var.permite_encriptacion}-${join(", ", sort(var.bloques_CIDR_permitidos))}-${var.nivel_seguridad}")
  politica_activa = local.def_politica[var.nivel_seguridad]
  acceso_abierto  = contains(var.bloques_CIDR_permitidos, "0.0.0.0/0")
}

resource "null_resource" "config_seguridad" {
  triggers = {
    permite_encriptacion = var.permite_encriptacion
    CIDR_permitidos      = join(", ", sort(var.bloques_CIDR_permitidos))
    nivel_seguridad      = var.nivel_seguridad
    security_hash        = local.hash_seguridad
    network_config_id    = data.terraform_remote_state.network.outputs.id_config_red
  }

  depends_on = [
    data.terraform_remote_state.network
  ]

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de seguridad:"
      echo "Encriptación: ${var.permite_encriptacion ? "Permite" : "No permite"}"
      echo "Nivel de seguridad: ${var.nivel_seguridad}"
      echo "Bloques CIDR permitidos: ${length(var.bloques_CIDR_permitidos)} configurados"
    EOT
  }
}
