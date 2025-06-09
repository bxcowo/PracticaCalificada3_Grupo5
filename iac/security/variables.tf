variable "permite_encriptacion" {
  description = "Permite encriptacion para todos los recursos disponibles"
  type        = bool
  default     = true
}

variable "bloques_CIDR_permitidos" {
  description = "Lista de bloques CIDR permitidos a tener acceso a recursos"
  type        = list(string)
  default     = []

  validation {
    condition     = alltrue([for cidr in var.bloques_CIDR_permitidos : can(cidrhost(cidr, 0))])
    error_message = "Todos los bloques CIDR deben tener una notación IPv4 válida."
  }
}

variable "nivel_seguridad" {
  description = "Nivel de seguridad establecida (basico, estandar, alto, critico)"
  type        = string
  default     = "estandar"

  validation {
    condition     = contains(["basico", "estandar", "alto", "critico"], var.nivel_seguridad)
    error_message = "El nivel de seguridad establecido debe ser: basico, estandar, alto o critico."
  }
}
