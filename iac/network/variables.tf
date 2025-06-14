variable "vpc_cidr" {
  description = "Bloque CIDR declarada para una VPC(Virtual Private Cloud)"
  type        = string
  default     = "10.0.0.0/16"

  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0))
    error_message = "El CIDR de la VPC debe ser un bloque CIDR IPv4 válido."
  }
}

variable "zonas_disponibilidad" {
  description = "Lista de zonas de disponibilidad a donde redistribuir los recursos existentes"
  type        = list(string)
  default     = ["Canada", "USA", "Australia", "Peru"]

  validation {
    condition     = length(var.zonas_disponibilidad) >= 2
    error_message = "Se deben especificar al menos 2 zonas de disponibilidad para garantizar alta disponibilidad"
  }
}

variable "permitir_nat_gateway" {
  description = "Habilitar Gateway NAT para permitir acceso a internet desde subredes privadas."
  type        = bool
  default     = true
}
