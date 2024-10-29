function Validate(){
    var nickname = document.forms["mailinglistform"]["nickname"].value;
    var email = document.forms["mailinglistform"]["email"].value;
    
    if (nickname.length < 1) {
        alert("Nickname non può essere vuoto!");
        return false;
    } else if (email.length < 1) {
        alert("Email non può essere vuoto!");
        return false
    } else if (!email.includes("@")) {
        alert("Email non valida!");
        return false;
    }
    return true;
}

document.forms["mailinglistform"].onsubmit = function(event) {
    if (!Validate()) {
        event.preventDefault(); // Blocca solo se Validate() ritorna false
    }
};

