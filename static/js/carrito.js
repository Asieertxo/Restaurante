const Clickbutton = document.querySelectorAll('.carta-btn')
let carrito = []

Clickbutton.forEach(btn => {
    btn.addEventListener('click', addItem)
})





function addItem(e){
    const button = e.target
    const item = button.closest('.carta-tarjeta')
    const itemName = item.querySelector('.carta-nombre').textContent
    const itemPrice = item.querySelector('.carta-precio').textContent
    const itemImg = item.querySelector('.carta-photo').src

    const newItem = {
        name: itemName,
        price: itemPrice,
        img: itemImg,
        cant: 1
    }

    addToCarrito(newItem)
}



function addToCarrito(newItem){
    var carrito = []
    var carritoLocal = []

    if(typeof(Storage) !== "undefined"){
        console.log(carrito)
        console.log('2')
        carritoLocal = JSON.parse(localStorage.getItem("carrito"))
        if(carritoLocal  !== null){//si hay algo almacenado lo ponemos como carrito y añadimos articulo
            console.log('3')
            carrito = carritoLocal
            for(let i=0; i<carrito.length; i++){
                console.log(carrito[i].name)
                console.log(newItem.name)
                if(carrito[i].name === newItem.name){
                    carrito[i].cant ++
                    localStorage.setItem("carrito", JSON.stringify(carrito))//hay que almacenar antes de salir
                    return null
                }
            }
            carrito.push(newItem)
        }else{//si no hay nada guardado, creamos un nuevo carrito y le añadimos el articulo
            console.log('4')
            carrito = [newItem];
        }

        console.log(carrito)
        localStorage.setItem("carrito", JSON.stringify(carrito))
    }else{
        console.log("No hay localStorage")
    }
}








function renderCarrito(){
    carrito = JSON.parse(localStorage.getItem("carrito"))
    var template = []

    carrito.map(item => {
        precio = item.price.substring(0, item.price.length - 1)
        var productPrice = precio * item.cant
        template.push(
            '<div class="carrito-tarjeta">' +
            '<img class="carrito-tarjeta_img" src=' + item.img + '>' +
            '<p class="carrito-tarjeta_nombre">' + item.name + '</p>' +
            '<input class="carrito-tarjeta_cant" type="number" value="' + item.cant + '">' +
            '<p class="carrito-tarjeta_precio">' + (productPrice).toFixed(2) + ' €</p>' +
            '<button class="btn btn-danger carrito-tarjeta_eliminar">x</button>' +
            '</div>'
        )
    })
    var htmlString = template.join('')
    document.write(htmlString)
}



function carritoTotal(){
    let total = 0;
    var carrito  = JSON.parse(localStorage.getItem("carrito"))
    carrito.forEach((item) => {
        precio = item.price.substring(0, item.price.length - 1)
        total = (precio * item.cant) + total
    })
    var template = []
    template.push(
        '<p>' + (total).toFixed(2) + ' €</p>'
    )

    document.write(template)
}