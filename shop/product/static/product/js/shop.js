function changeOrderbyBox(value){
    $.ajax({
        url:'http://127.0.0.1:8000/product/shop/',
        success: function(result) {
            console.log("POST Result:");
            console.log(result);
        }
    })
}