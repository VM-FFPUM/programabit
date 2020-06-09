function confirmarEliminacion(id) {
  Swal.fire({
    title: '¿Estas seguro de eliminarlo?',
    text: "No serás capaz de revertir esta acción.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Confirmar',
    cancelButtontext: 'Cancelar'
    }).then((result) => {
      if (result.value) {
        window.location.href='/eliminar/'+id+'/';
      }
    })
}
