locals {
  hash_subredes  = md5(join(", ", sort(var.ids_subred)))
  prefix_recurso = "compute-${substr(local.hash_subredes, 0, 8)}"
}

resource "null_resource" "config_compute" {
  triggers = {
    tipo_instancia  = var.tipo_instancia
    conteo_subredes = length(var.ids_subred)
    hash_subredes   = local.hash_subredes
  }

  provisioner "local-exec" {
    command = <<-EOT
      echo "Configuración de instancia computacional"
      echo "Tipo de instancia: ${var.tipo_instancia}"
      echo "Subredes: ${join(", ", var.ids_subred)}"
    EOT
  }

  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Limpiando recursos computacionales...'"
  }
}
