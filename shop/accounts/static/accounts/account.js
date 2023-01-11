function msg(data) {
}


function customerOrder(data) {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/order/customer-order-list/',
    }).done(function (data) {
        console.log(data)
        let row = ''
        for (item of data) {
            row += '<tr>'
            row += '    <td class="order-number"><a href="#">#' + item.id + '</a></td>'
            row += '    <td class="order-date"><span>' + item.created_at + '</span></td>'
            row += '    <td class="order-status"><span>' + item.status + '</span></td>'
            row += '    <td class="order-total"><span>$' + item.grand + '</span></td>'
            row += '    <td class="order-action"><a href="#"'
            row += '            class="btn btn-primary btn-link btn-underline">View</a></td>'
            row += '</tr>'
        }
        $('#orderList').html('')
        $('#orderList').html(row)
    });
}


function editAddressForm(e) {
    $("#form_address").show();

    let addressID = e.dataset.address
    url = 'http://127.0.0.1:8000/api/v1/accounts/customer-adderss/' + addressID + '/'

    $.ajax({
        type: "GET",
        url: url,
    }).done(function (data) {
        console.log(data.id)
        $("#id").val(data.id);
        $("#country").val(data.country);
        $("#town").val(data.city);
        $("#state").val(data.province);
        $("#address1").val(data.address);
        $("#zip").val(data.postal_code);
    });
};


function deleteAddress(e) {

    let addressID = e.dataset.address;
    let msg = 'Are you sure about deleting Address#' + addressID + '?'
    if (confirm(msg) == true) {
        var token = $("input[name=csrfmiddlewaretoken]").val();

        url = 'http://127.0.0.1:8000/api/v1/accounts/customer-adderss/' + addressID + '/'
        $.ajax({
            type: "DELETE",
            headers: { "X-CSRFToken": token },
            url: url,
        }).done(function (data) {
            console.log(data)
            customerAddress()
        });
    }
};

$("#address_form").submit(function (event) {
    let id = $('#id').val();
    var formData = {
        country: $('#country').val(),
        city: $('#town').val(),
        province: $('#state').val(),
        address: $('#address1').val(),
        postal_code: $('#zip').val(),
    };


    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "PATCH",
        url: 'http://127.0.0.1:8000/api/v1/accounts/customer-adderss/' + id + '/',
        headers: { "X-CSRFToken": token },
        data: formData,
        dataType: "json",
        encode: true,
    }).done(function (data) {
        customerAddress()
        $("#form_address").hide();
    }).fail(function (data) {
        console.log(11111111111, data);
    });

    event.preventDefault();
});


function customerAddress() {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/accounts/customer-adderss-list/',
    }).done(function (data) {
        console.log(data)
        let row = ''
        for (item of data) {
            row += '<div class="col-sm-6 mb-4">'
            row += '    <div class="card card-address">'
            row += '        <div class="card-body">'
            row += '            <h5 class="card-title text-uppercase">Address#' + item.id + '</h5>'
            row += '            <p>' + item.country + '<br>'
            row += '                ' + item.province + '<br>'
            row += '                ' + item.city + '<br>'
            row += '                ' + item.address + '<br>'
            row += '                ' + item.postal_code
            row += '            </p>'
            row += '          <a href="#form_address" data-address="' + item.id + '" class="btn btn-link btn-secondary btn-underline" onclick="editAddressForm(this);">Edit <i'
            row += '                    class="far fa-"></i></a>'
            row += '          <P href="" data-address="' + item.id + '" class="btn btn-link btn-secondary btn-underline" onclick="deleteAddress(this);">DELETE <i'
            row += '                    class="far fa-delete"></i></P>'
            row += '        </div>'
            row += '    </div>'
            row += '</div>           '
        }
        $('#addresses').html('')
        $('#addresses').html(row)
    });
}

$(document).ready(function () {
    $("#profile_form").submit(function (event) {

        /* get the action attribute from the <form action=""> element */
        var $form = $(this),
            url = $form.attr('action');


        var formData = {
            first_name: $("#id_first_name").val(),
            last_name: $("#id_last_name").val(),
            email: $("#id_email").val(),
            gender: $("#id_gender").val(),
            birthday: $("#id_birthday").val(),
            bio: $("#id_bio").val(),
            image: $("#id_image").val(),
        };
        var token = $("input[name=csrfmiddlewaretoken]").val();

        $.ajax({
            type: "POST",
            url: url,
            headers: { "X-CSRFToken": token },
            data: formData,
            dataType: "json",
            encode: true,
        }).done(function (data) {
            console.log(data);
            // console.log(status);
            msg(data)
            $("#msg").html('')
            $("#msg").html('<div class="alert  alert-' + data.status + ' alert-dark alert-round alert-inline mb-1"><h4 class="alert-title">' + data.status + ' :</h4>' +
                data.msg +
                '<button type="button" class="btn btn-link btn-close"><i class="d-icon-times"></i></button></div>');
        });
        event.preventDefault();
    });
});