output "id_config_red" {
  description = "Identificador único de la configuración de red creada por null resource"
  value       = null_resource.red_config.id
}

output "resumen_red" {
  description = "Un resumen de la configuración del módulo de red"
  value = {
    vpc_cidr             = var.vpc_cidr
    zonas_disponibilidad = var.zonas_disponibilidad
    public_subnets       = local.subredes_publicas
    private_subnets      = local.subredes_privadas
    permitir_nat_gateway = var.permitir_nat_gateway
    total_subnets        = local.numero_subredes
  }
}

output "direccion_subredes" {
  description = "Direcciones de subredes de CIDR por zona de disponibilidad"
  value = {
    for i, zd in var.zonas_disponibilidad : zd => {
      subred_publica = local.subredes_publicas[i]
      subred_privada = local.subredes_privadas[i]
    }
  }
}
