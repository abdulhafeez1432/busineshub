$(document).ready(function () {
    // catch the form's submit event
    $('#sell-business').submit(function () {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "{% url 'seller:sell-business' %}",
            // on success
            success: function (response) {
                alert("Thankyou for reaching us out " + response.about);
                $('#sell-business')[0].reset();
                window.location.href = "/seller/addaboutbusiness/" + response.about;
            },
            // on error
            error: function (response) {
                // alert the error if any error occured
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})