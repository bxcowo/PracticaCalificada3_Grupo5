variable "permite_monitoreo" {
  description = "Permite un monitoreo detallado con alarmas"
  type        = bool
  default     = true
}

variable "email_alertas" {
  description = "Dirección de email para recibir alertas por monitoreo"
  type        = string
  default     = "dummy123@gmail.com"

  validation {
    condition     = can(regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", var.email_alertas))
    error_message = "La dirección de email debe ser válida"
  }
}

variable "dias_retencion_metricas" {
  description = "Número de días de retención de métricas de recursos"
  type        = number
  default     = 90

  validation {
    condition     = var.dias_retencion_metricas >= 7 && var.dias_retencion_metricas <= 730
    error_message = "La retención de métricas debe ser de entre 7 a 730 días."
  }
}
