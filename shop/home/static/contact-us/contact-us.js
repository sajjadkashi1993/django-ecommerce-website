
// $(document).ready(function () {
//     $("#contact_form").submit(function (event) {

//         /* get the action attribute from the <form action=""> element */
//         var $form = $(this),
//             url = $form.attr('action');

//         console.log(url);

//         var formData = {
//             name: $("#name").val(),
//             comment: $("#comment").val(),
//             email: $("#email").val(),
//         };
//         var token = $("input[name=csrfmiddlewaretoken]").val();

//         $.ajax({
//             type: "POST",
//             url: url,
//             headers: { "X-CSRFToken": token },
//             data: formData,
//             dataType: "json",
//             encode: true,
//         }).done(function (data) {
//             console.log(data.message);
//             $("#msg").html('')
//             $("#msg").html('<div class="alert  alert-'+ data.status +' alert-dark alert-round alert-inline mb-1"><h4 class="alert-title">'+data.status+' :</h4>' +
//                 data.message+
//                 '<button type="button" class="btn btn-link btn-close"><i class="d-icon-times"></i></button></div>');

//             $("#name").val('') ; 
//             $("#comment").val('');
//             $("#email").val('');
//         });
//         event.preventDefault();
//     });
// });