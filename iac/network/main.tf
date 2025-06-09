locals {
  hash_red = md5("${var.vpc_cidr}-${join(",", sort(var.zonas_disponibilidad))}-${var.permitir_nat_gateway}")
  # Una subred pública y privada por zona de disponibilidad
  numero_subredes = length(var.zonas_disponibilidad) * 2
  # Cálculo de bits disponibles para la creación de subredes
  cidr_newbits = ceil(log(local.numero_subredes, 2)) + 2

  subredes_publicas = [
    for i, zd in var.zonas_disponibilidad : cidrsubnet(var.vpc_cidr, local.cidr_newbits, i)
  ]
  subredes_privadas = [
    for i, zd in var.zonas_disponibilidad : cidrsubnet(var.vpc_cidr, local.cidr_newbits, i + length(var.zonas_disponibilidad))
  ]

  costo_nat_gateway_total = var.permitir_nat_gateway ? length(var.zonas_disponibilidad) * 45.0 : 0.0
}

resource "null_resource" "red_config" {
  triggers = {
    vpc_cidr                    = var.vpc_cidr
    numero_zonas_disponibilidad = length(var.zonas_disponibilidad)
    zonas_disponibilidad        = join(",", sort(var.zonas_disponibilidad))
    permitir_nat_gateway        = var.permitir_nat_gateway
    network_hash                = local.hash_red
  }

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de red:"
      echo "VPC CIDR: ${var.vpc_cidr}"
      echo "Zonas de disponibilidad: ${join(", ", var.zonas_disponibilidad)}"
      echo "NAT Gateway: ${var.permitir_nat_gateway ? "Permitido" : "No permitido"}"
    EOT
  }
}
