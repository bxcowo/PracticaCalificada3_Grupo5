variable "dias_retencion_logs" {
  description = "Número de días de retención de log de aplicación"
  type        = number
  default     = 30

  validation {
    condition     = var.dias_retencion_logs >= 1 && var.dias_retencion_logs <= 365
    error_message = "La retención de logs debe ser de entre 1 a 365 días."
  }
}

variable "nivel_log" {
  description = "Nivel mínimo de logging definido para los logs de aplicación"
  type        = string
  default     = "INFO"

  validation {
    condition     = contains(["DEBUG", "INFO", "WARN", "ERROR", "FATAL"], var.nivel_log)
    error_message = "El nivel de logging debe de ser: DEBUG, INFO, WARN, ERROR, FATAL."
  }
}

variable "permite_auditoria_logs" {
  description = "Permite la auditoria de logs para el cumplimiento de requerimientos"
  type        = bool
  default     = false
}
