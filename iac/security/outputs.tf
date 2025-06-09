output "id_config_seguridad" {
  description = "Identificador único de la configuración de seguridad creado por null resource"
  value       = null_resource.config_seguridad.id
}

output "resumen_seguridad" {
  description = "Un resumen de la configuración del módulo de seguridad"
  value = {
    permite_encriptacion    = var.permite_encriptacion
    nivel_seguridad         = var.nivel_seguridad
    politica_activa         = local.politica_activa
    numero_politicas        = length(local.politica_activa)
    acceso_abierto_internet = local.acceso_abierto
    numero_CIDR_permitidos  = length(var.bloques_CIDR_permitidos)
  }
}

output "requerimientos_politicas" {
  description = "Políticas de seguridad requeridas para el actual nivel de seguridad"
  value       = local.politica_activa
}
