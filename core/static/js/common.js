function sumar(url) {
    var id = `${url.slice(url.length-2, url.length-1)}`;
    var stock = $(`#${id}-stock`).val();
    var id_cantidad = `#${id}-cant`;
    var id_subtotal = `#${id}-subtotal`;
    var id_preciou = `#${id}-preciou`;
    var preciou = $(id_preciou).val();
    var total = `#total`;
    var nueva_cant = 1 + parseInt($(id_cantidad)[0].innerHTML);
    if (nueva_cant <= stock) {
        $(id_cantidad).html(nueva_cant);
        var precioU = parseInt(preciou);
        var subTotal = parseInt($(id_subtotal)[0].innerHTML);
        $(id_subtotal).html(precioU + subTotal);
        $(total).html(parseInt($(total)[0].innerHTML) + precioU);
        $.ajax({
            type: "GET",
            url: url
        });
    }
}

function restar(url) {
    var id = `${url.slice(url.length-2, url.length-1)}`;
    var id_cantidad = `#${id}-cant`;
    var id_subtotal = `#${id}-subtotal`;
    var id_preciou = `#${id}-preciou`;
    var preciou = $(id_preciou).val();
    var total = `#total`;
    var nueva_cant = -1 + parseInt($(id_cantidad)[0].innerHTML);
    if (nueva_cant >= 0) {
        $(id_cantidad).html(nueva_cant);
        var precioU = parseInt(preciou);
        var subTotal = parseInt($(id_subtotal)[0].innerHTML);
        $(id_subtotal).html(-precioU + subTotal);
        $(total).html(parseInt($(total)[0].innerHTML) - precioU);
        $.ajax({
            type: "GET",
            url: url
        });
        if(nueva_cant == 0) {
            setTimeout(function() {window.location.reload();}, 500)
        }
    }
}

function limpiar_carrito() {
    $.ajax({
        url: '/carro/limpiar/',
        type: "GET"
    });
    setTimeout(function() {window.location.reload();}, 500)
}
var first = false;
function apply_discount() {
    $.ajax({
        url: '/get/descuento/' + $('#code').val(),
        type: "GET",
        success: function(data) {
            descuentototal = data.porcentaje;
            $('#descount').html('Se aplicara un descuento del ' + data.porcentaje + '% en el total de la compra.');
            $('#total').html(parseInt($('#total')[0].innerHTML) - parseInt($('#total')[0].innerHTML)*(parseInt(data.porcentaje)/100))
            $('#descountbtn').addClass('disabled');
            $('.cantbtn').addClass('disabled');
        },
        error: function() {
            $('#descount').html('<center><p class="bg-danger rounded-pill p-3">No se ha encontrado descuento.</p></center>');
        }
    });
}

window.addEventListener('load', function() {
    var cerrar_sesion = document.getElementById('deslogearse');
    cerrar_sesion.addEventListener('click', function() {
        var cookies_array = document.cookie.split(';');
        var cookies_dict = [];
        var csrftoken;
        cookies_array.forEach(elem => {
            var temp = elem.split('=');
            cookies_dict.push({
                key: temp[0],
                value: temp[1]
            });
        })
        cookies_dict.forEach(elem => {
            if(elem.key == 'csrftoken') {
                csrftoken = elem.value;
            }
        })
        $.ajax({
            type: 'POST',
            url: '/post/logout/',
            data: {csrfmiddlewaretoken: csrftoken},
            success: function() {
                setTimeout(function() {
                    location.reload();
                }, 500);
            },
            error: function() {
                alert('error');
            }
        })
    }, false);
    if ($('#vacio').length) {
        $('#comprar-btn').addClass('disabled');
    }
    $.ajax({
        url: '/get/descuento/null/',
        type: "GET",
    })
}, false);