function confirmarEliminacion(id){
  Swal.fire({
  title: '¿Estas Seguro?',
  text: "No podrás deshacer estos cambios!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Si, Eliminar!',
  cancelButtonText:'Cancelar'
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href = "/eliminar_cafe/"+id+"/";
  }
})
}
