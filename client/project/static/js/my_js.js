document.querySelector('#generateEncrypt').onclick = function () {
    var button = document.createElement("button");
    var span = document.createElement("span");
    var value = document.createTextNode("Get Token");
    span.appendChild(value);
    button.className = "contact100-form-btn";
    button.appendChild(span);
    document.querySelector("#getToken").appendChild(button);
};