variable "tipo_almacenamiento" {
  description = "Tipo de almacenamiento primario para consistencia de datos"
  type        = string
  default     = "rty"

  validation {
    condition     = contains(["qwe", "rty", "uio", "asd", "fgh", "jkl"], var.tipo_almacenamiento)
    error_message = "El almacenamiento debe de pertenecer a los tipos: qwe, rty, uio, asd, fgh, jkl"
  }
}

variable "dias_backup" {
  description = "Número de días de retención de backups"
  type        = number
  default     = 7

  validation {
    condition     = var.dias_backup >= 1 && var.dias_backup <= 35
    error_message = "El número de días debe ser entre 1 a 35 días"
  }
}

variable "permite_versionado" {
  description = "Permitir versionamiento para objetos almacenados"
  type        = bool
  default     = false
}
