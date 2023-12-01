function sendMail(contactForm) {
    emailjs.send("service_i2tzp5e","rubysbooks",{
        "from_name": contactForm.fullname.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        window.location = "{% url 'thank-you.html' %}";
    }, function(error) {
        console.log('FAILED...', error);
    });
return false;  // To block from loading a new page
}


$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})