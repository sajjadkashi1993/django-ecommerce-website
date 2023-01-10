function htmlCartModal(data) {
    $('#subtotal').text('$' + data.grand_total)
    $('#cart-price').text('$' + data.grand_total)
    $('#cart-count').text(data.cart_items.length)
    $("#products_cart").html('')
    let cart = '';
    for (const item of data.cart_items) {
        cart += '<div class="product product-cart">';
        cart += '    <figure class="product-media">';
        cart += '        <a href="' + item.product.get_absolute_url + '">';
        cart += '            <img src="' + item.product.main_pic + '" alt="product" width="80"';
        cart += '                height="88" />';
        cart += '        </a>';
        cart += '        <button data-product="' + item.product.id + '" class="btn btn-link btn-close" onclick="delCart(this);">';
        cart += '            <i class="fas fa-times"></i><span class="sr-only">Close</span>';
        cart += '        </button>';
        cart += '    </figure>';
        cart += '    <div class="product-detail">';
        cart += '        <a href="' + item.product.get_absolute_url + '" class="product-name">' + item.product.title + '</a>';
        cart += '        <div class="price-box">';
        cart += '            <span class="product-quantity">' + item.quantity + '</span>';
        cart += '            <span class="product-price">$' + item.product.get_after_discount_price + '</span>';
        cart += '        </div>';
        cart += '    </div>';
        cart += '</div>';
        cart += '<!-- End of Cart Product -->';
    }

    $("#products_cart").html(cart);
}

function delCart(e) {
    var token = $("input[name=csrfmiddlewaretoken]").val();
    url = 'http://127.0.0.1:8000/api/v1/cart/del/'
    let productID = e.dataset.product
    $.ajax({
        type: "DELETE",
        headers: { "X-CSRFToken": token },
        url: url,
        data: { 'product': productID },
    }).done(function (data) {
        htmlCartModal(data)
    });
};

$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/cart/show/',
    }).done(function (data) {
        console.log(data);
        htmlCartModal(data)
    });
});