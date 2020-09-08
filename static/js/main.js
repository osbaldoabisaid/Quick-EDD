var btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  btnDelete.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('¿Seguro que deseas boorar este registro?')){
        e.preventDefault();
       }
      });
  })
}
console.log(btnDelete);