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
        carritoLocal = JSON.parse(localStorage.getItem("carrito"))
        if(carritoLocal  !== null){//si hay algo almacenado lo ponemos como carrito y añadimos articulo
            carrito = carritoLocal
            for(let i=0; i<carrito.length; i++){
                if(carrito[i].name === newItem.name){
                    carrito[i].cant ++
                    localStorage.setItem("carrito", JSON.stringify(carrito))//hay que almacenar antes de salir
                    return null
                }
            }
            carrito.push(newItem)
        }else{//si no hay nada guardado, creamos un nuevo carrito y le añadimos el articulo
            carrito = [newItem];
        }
        localStorage.setItem("carrito", JSON.stringify(carrito))
    }else{
        console.log("No hay localStorage")
    }
}



function renderCarrito(){
    carrito = JSON.parse(localStorage.getItem("carrito"))
    var template = []
    let id = 0;

    carrito.map(item => {
        precio = item.price.substring(0, item.price.length - 1)
        var productPrice = precio * item.cant
        template.push(
            '<div class="carrito-tarjeta">' +
            '<img class="carrito-tarjeta_img" src=' + item.img + '>' +
            '<p class="carrito-tarjeta_nombre" id = name-' + id + '>' + item.name + '</p>' +
            '<input class="carrito-tarjeta_cant" id = cant-' + id + ' type="number" min="1" onchange="cantItem(' + id +')" value="' + item.cant + '">' +
            '<p class="carrito-tarjeta_precio">' + (productPrice).toFixed(2) + ' €</p>' +
            '<button class="btn btn-danger carrito-tarjeta_eliminar" onclick="deleteItem(' + id +')">x</button>' +
            '</div>'
        )
        id++
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



function cantItem(id){
    const itemName = document.getElementById('name-'+id).textContent
    const itemCant = document.getElementById('cant-'+id).value
    console.log(itemName)
    console.log(itemCant)
    carrito = JSON.parse(localStorage.getItem("carrito"))
    carrito.map(item => {
        if(item.name === itemName){
            item.cant = itemCant
        }
    })
    localStorage.setItem("carrito", JSON.stringify(carrito))
    location.reload()
}



function deleteItem(id){
    const itemName = document.getElementById('name-'+id).textContent
    carrito = JSON.parse(localStorage.getItem("carrito"))
    const newCarrito = carrito.filter(item => item.name != itemName)
    localStorage.setItem("carrito", JSON.stringify(newCarrito))
    location.reload()
}
