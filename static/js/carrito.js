const Clickbutton = document.querySelectorAll('.carta-btn')
let carrito = []
let totalPagar = []

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
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))
    let localDescuento = 1//es por lo que multiplica, por defecto, luego se comprueba

    if(totalPagar !== null){
        if(totalPagar.descuento !== 0){
            localDescuento = totalPagar.descuento
        }else{
            localDescuento = 1//es por lo que multiplica el total
        }
    }
    
    let total = 0;
    var carrito  = JSON.parse(localStorage.getItem("carrito"))
    carrito.forEach((item) => {
        precio = item.price.substring(0, item.price.length - 1)
        total = (precio * item.cant) + total
    })

    totalPagar = {
        subtotal: parseFloat((total).toFixed(2)),
        servicio: 0,
        transporte: 0,
        descuento: localDescuento,
        total: parseFloat((total).toFixed(2))
    }
    localStorage.setItem("totalPagar", JSON.stringify(totalPagar))

    var template = []
    template.push(
        '<p>' + (totalPagar.subtotal).toFixed(2) + ' €</p>'
    )
    document.write(template)
}

function cantItem(id){
    const itemName = document.getElementById('name-'+id).textContent
    const itemCant = document.getElementById('cant-'+id).value
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

function servicio(){
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))
    totalPagar.servicio = parseFloat((totalPagar.total*10/100).toFixed(2))
    totalPagar.total = totalPagar.total + totalPagar.servicio
    localStorage.setItem("totalPagar", JSON.stringify(totalPagar))

    var template = []
    template.push(
        '<p>' + (totalPagar.servicio).toFixed(2) + ' €</p>'
    )
    document.write(template)
}

function randTrasnport(){
    pTraspot =  Math.random() * (3 - 1 + 1) + 1
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))
    totalPagar.transporte = parseFloat((pTraspot).toFixed(2))
    totalPagar.total = totalPagar.total + totalPagar.transporte
    localStorage.setItem("totalPagar", JSON.stringify(totalPagar))

    var template = []
    template.push(
        '<p>' + (totalPagar.transporte).toFixed(2) + ' €</p>'
    )
    document.write(template)
}

function pagoTotal(){
    var template = []
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))

    if(totalPagar.descuento === "T"){
        template.push(
            '<p>' + (totalPagar.total - totalPagar.transporte).toFixed(2) + ' €</p>'
        )
    }else{
        template.push(
            '<p>' + (totalPagar.total * totalPagar.descuento).toFixed(2) + ' €</p>'
        )
    }
    document.write(template)

    if(pagoTotal.descuento !== 0){
        totalPagar.descuento = 0
        localStorage.setItem("totalPagar", JSON.stringify(totalPagar))
    }
}

function verDescuento(){
    var template = []
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))

    console.log(totalPagar)
    if(totalPagar.descuento !== 1){
        if(totalPagar.descuento === "T"){
            template.push(
                '<p->' + (totalPagar.transporte).toFixed(2) + ' €</p>'
            )
        }else{
            template.push(
                '<p->' + ((totalPagar.total * totalPagar.descuento) - totalPagar.total).toFixed(2) + ' €</p>'
            )
        }
        
    }else{
        template.push(
            '<p>0 €</p>'
        )
    }
    document.write(template)
}


function descuento(){
    let descu = document.getElementById('descuento').value
    totalPagar = JSON.parse(localStorage.getItem("totalPagar"))
    switch (descu){
        case "Burger10":
            totalPagar.descuento = 0.9
            console.log('10%')
            break
        case "Burger20":
            totalPagar.descuento = 0.8
            console.log('20%')
            break
        case "Trasporte":
            totalPagar.descuento = "T"
            console.log('T')
            break
        default:
            totalPagar.descuento = 0
            console.log('None')
            break
    }
    localStorage.setItem("totalPagar", JSON.stringify(totalPagar))
    location.reload()
}

function savecarrito(){
    var savecarrito = JSON.stringify(JSON.parse(localStorage.getItem("carrito")))

    var template = []

    template.push(
        "<input type='hidden' name='carrito' value='" + savecarrito + "'></input>"
    )
    document.write(template)
}