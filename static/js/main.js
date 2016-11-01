function login() {
    var username = document.getElementById('username')
    var password = document.getElementById('password')
    console.log(username, password)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', "/login?username=" + username + "&password=" + password, true);
    xhr.send();
}

function signup() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var email = document.getElementById('email').value
    var name = document.getElementById('name').value

    console.log(username,password,email);
    /*
    var http = new XMLHttpRequest();
    var url = "/signup";
    var params = "name="+name+"&email="+email+"&username="+username+"&password="+password
    http.open("POST", url, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlcoded");

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(params); */
}
