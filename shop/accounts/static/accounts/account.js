function msg(data){
}


function customerOrder(data){
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/order/customer-order-list/',
    }).done(function (data) {
        let row=''
        for (item of data){
            row +='<tr>'
            row +='    <td class="order-number"><a href="#">#'+item.id+'</a></td>'
            row +='    <td class="order-date"><span>'+item.updated_at+'</span></td>'
            row +='    <td class="order-status"><span>'+item.status+'</span></td>'
            row +='    <td class="order-total"><span>$'+item.grand+'</span></td>'
            row +='    <td class="order-action"><a href="#"'
            row +='            class="btn btn-primary btn-link btn-underline">View</a></td>'
            row +='</tr>'                               
        }
        $('#orderList').html('')
        $('#orderList').html(row)
    });
}

function customerAddress(data){
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/v1/accounts/customer-adderss-list/',
    }).done(function (data) {
        let row=''
        for (item of data){
        row +='<div class="col-sm-6 mb-4">'
        row +='    <div class="card card-address">'
        row +='        <div class="card-body">'
        row +='            <h5 class="card-title text-uppercase">Address#'+item.id+'</h5>'
        row +='            <p>'+item.country+'<br>'
        row +='                '+item.province+'<br>'
        row +='                '+item.city+'<br>'
        row +='                '+item.address+'<br>'
        row +='                '+item.postal_code
        row +='            </p>'
        row +='            <a href="#" class="btn btn-link btn-secondary btn-underline">Edit <i'
        row +='                    class="far fa-edit"></i></a>'
        row +='        </div>'
        row +='    </div>'
        row +='</div>           '
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

        console.log(url);

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
            $("#msg").html('<div class="alert  alert-'+ data.status +' alert-dark alert-round alert-inline mb-1"><h4 class="alert-title">'+data.status+' :</h4>' +
                data.msg+
                '<button type="button" class="btn btn-link btn-close"><i class="d-icon-times"></i></button></div>');
        });
        event.preventDefault();
    });
});