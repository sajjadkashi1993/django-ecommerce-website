function checkoutHtml(data){
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


function couponMsg(msg){
        let HtmlMsg = '';
            HtmlMsg += '<div class="alert alert-primary alert-dark alert-round alert-inline">'
			// HtmlMsg += '	<h4 class="alert-title">News :</h4>'
			HtmlMsg += msg
			HtmlMsg += '	<button type="button" class="btn btn-link btn-close">'
			HtmlMsg += '		<i class="d-icon-times"></i>'
			HtmlMsg += '	</button>'
			HtmlMsg += '</div>'
        
        $("#coupon-msg").html('');
        $("#coupon-msg").html(HtmlMsg);
}

$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/order/checkout/',
    }).done(function (data) {
        checkoutHtml(data)  
    });


    $("#applyCoupon").click(function (event) {
        var coupon= $("#coupon").val();
        url = 'http://127.0.0.1:8000/api/v1/order/checkout/?coupon='+coupon
        $.ajax({
            type: "GET",
            url: url,
        }).done(function (data) {
            checkoutHtml(data)
            couponMsg(data.msg)  
        });
        event.preventDefault();
    });

    $("#order-form").submit(function (event) {
        var formData = {
            coupon: $("#coupon").val(),
            receiver_name: $('#firstname').val() + ' ' + $('#lastname').val(),
            country: $('#country').val(),
            city: $('#town').val(),
            province: $('#state').val(),
            address: $('#address').val(),
            postal_code: $('#zip').val(),
            receiver_mobile: $('#phone').val(),
            content: $('#order_notes').val(),
        };
        

        var token = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:8000/api/v1/order/checkout/',
            headers: { "X-CSRFToken": token },
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            console.log(data)
            if (data.order_id){
                $.ajax({
                    type: "GET",
                    url: "http://127.0.0.1:8000/api/v1/order/order-pay/"+data.order_id,
                }).done(function (data) {

                    console.log(111111111, data)
                });
            }
            // window.location.replace("http://127.0.0.1:8000/api/v1/order/order-pay/"+data.order_id);
        }).fail(function() {
            alert( "error" );
          });
        event.preventDefault();
    });

});