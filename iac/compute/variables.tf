variable "tipo_instancia" {
  description = "Tipo/tamaño de instancia computacional según proveedor"
  type        = string
  default     = "pequeño"
  validation {
    condition     = contains(["pequeño", "mediano", "grande"], var.tipo_instancia)
    error_message = "El tipo de instancia debe de ser pequeño, mediano o grande"
  }
}

variable "ids_subred" {
  description = "Lista de ids de subredes donde los recursos computacionales serán desplegados"
  type        = list(string)
  default     = ["1234", "2345", "3456"]
  validation {
    condition     = length(var.ids_subred) > 0
    error_message = "Al menos un id de una subred debe de ser dado"
  }
}
