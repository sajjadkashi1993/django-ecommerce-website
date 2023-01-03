function checkout_html(data){
    $('#order-subtotal').text('$' + data.cart.grand_total)
        $('#shipping').text('$' + data.shipping)
        $('#tax').text('$' + data.tax)
        $('#discount').text('$' + data.discount)
        $('#total').text('$' + data.total)

        let products = '';
        for (const item of data.cart.cart_items){
            products +='<tr class="mb-2">'
            products +='<td class="product-name">'+ item.product.title +'<span'
            products +='        class="product-quantity">×&nbsp;'+ item.quantity +'</span></td>'
            products +='<td class="product-total text-body">  $'+ item.sub_total +'</td>'
            products +='</tr>'
        }
        
        $("#order-product").html('');
        $("#order-product").html(products);
}

$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/order/checkout/',
    }).done(function (data) {
      checkout_html(data)  
    });

    $("#applyCoupon").click(function (event) {
        var coupon= $("#coupon").val();
        url = 'http://127.0.0.1:8000/api/v1/order/checkout/?coupon='+coupon
        console.log(url) 
        $.ajax({
            type: "GET",
            url: url,
        }).done(function (data) {
            console.log(1111, data)
            checkout_html(data)  
        });
        event.preventDefault();
    });

});