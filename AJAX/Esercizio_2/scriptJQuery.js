function getCheckboxValues(checkBox) {
    var checked = [];
    for (var option of checkBox) {
        if (option.checked) {
            checked.push(option.value);
        }
    }
    return checked;
}

function getSelectedValues(sel) {
    return sel.options[sel.selectedIndex].value;
}

$('#regForm').on('submit', function(event) {
    event.preventDefault(); // Prevent page refresh

    var username = $('#username').val();
    var password = $('#password').val();
    var email = $('#email').val();
    var gender = $('input[name="gender"]:checked').val();
    var interests = getCheckboxValues($('input[name="interests"]'));
    var country = getCheckboxValues($('input[name="country"]'));

    var params = JSON.stringify({
        username: username,
        password: password,
        email: email,
        gender: gender,
        interests: interests,
        country: country
    });

    $.ajax({
        url: 'https://httpbin.org/post',
        type: 'POST',
        contentType: 'application/json',
        data: params,
        success: function(response) {
            var data = JSON.parse(response.data);
            var responseUsername = data.username;
            $('#response').html('Utente ' + responseUsername + ' creato!');
        },
        error: function() {
            $('#response').html('Errore durante l\'invio dei dati.').css('color', 'red');
        }
    });
});
