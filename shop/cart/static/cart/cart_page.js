$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/cart/show/',
    }).done(function (data) {
        $('#subtotal').text('$' + data.grand_total)
        $("#cartTable").html('')
        let cartTable = '';
        for (const item of data.cart_items){
            cartTable += '<tr>'
            cartTable += '<td class="product-thumbnail">'
            cartTable += '    <figure>'
            cartTable += '        <a href="'+ item.product.get_absolute_url +'">'
            cartTable += '            <img src="'+ item.product.main_pic +'" width="100" height="100"'
            cartTable += '                alt="product">'
            cartTable += '        </a>'
            cartTable += '    </figure>'
            cartTable += '</td>'
            cartTable += '<td class="product-name">'
            cartTable += '    <div class="product-name-section">'
            cartTable += '        <a href="'+ item.product.get_absolute_url +'">'+ item.product.title +'</a>'
            cartTable += '    </div>'
            cartTable += '</td>'
            cartTable += '<td class="product-subtotal">'
            cartTable += '    <span class="amount">$'+ item.product.get_after_discount_price +'</span>'
            cartTable += '</td>'
            cartTable += '<td class="product-quantity">'
            cartTable += '    <span class="quantity">'+ item.quantity +'</span>'
            // cartTable += '    <div class="input-group">'
            // cartTable += '        <button class="quantity-minus d-icon-minus"></button>'
            // cartTable += '        <input class="quantity form-control" type="number" min="1"'
            // cartTable += '            max="1000000" value='+ item.quantity +'>'
            // cartTable += '        <button class="quantity-plus d-icon-plus"></button>'
            // cartTable += '    </div>'
            cartTable += '</td>'
            cartTable += '<td class="product-price">'
            cartTable += '    <span class="amount">$'+ item.sub_total +'</span>'
            cartTable += '</td>'
            cartTable += '<td class="product-close">'
            cartTable += '    <a href="#" class="product-remove" title="Remove this product">'
            cartTable += '        <i class="fas fa-times"></i>'
            cartTable += '    </a>'
            cartTable += '</td>'
            cartTable += '</tr>;'
        }

        $("#cartTable").html(cartTable);
    });


    // let delCartBtns = document.getElementsByClassName('tt');
    // console.log(delCartBtns);
    // Array.from(delCartBtns).forEach(function(element) {
    //     console.log(element)
    // });

});