function msg(data){


}
$(document).ready(function () {
    $("form").submit(function (event) {

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