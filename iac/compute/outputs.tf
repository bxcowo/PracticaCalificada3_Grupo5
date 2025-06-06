output "id_config_computacional" {
  description = "Identificador del recurso computacional creado con null resource"
  value       = null_resource.config_compute.id
}

output "prefix_recurso" {
  description = "Prefijo generado para el recurso de computo"
  value       = local.prefix_recurso
}

output "resumen_recurso" {
  description = "Un resumen de la configuración del módulo de cómputo"
  value = {
    tipo_instancia  = var.tipo_instancia
    conteo_subredes = length(var.ids_subred)
  }
}
