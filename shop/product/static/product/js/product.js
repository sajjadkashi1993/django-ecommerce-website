$(document).ready(function () {
    $("#addCart").click(function (event) {
        var formData = {
            quantity: $("#quantity").val(),
            product: $("#product").val(),
        };
        console.log(formData)
        url = 'http://127.0.0.1:8000/api/v1/cart/add/'


        var token = $("input[name=csrfmiddlewaretoken]").val();
        console.log(token)
        $.ajax({
            type: "POST",
            url: url,
            headers: { "X-CSRFToken": token },
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            htmlCartModal(data)
        });
        event.preventDefault();
    });
});