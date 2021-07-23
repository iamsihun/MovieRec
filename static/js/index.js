const request = new XMLHttpRequest();

function search() {
    let searchBox = document.getElementById("searchBox")
    let text = searchBox.value;

    let url = "http://127.0.0.1:5000/search/" + text;
    request.open("GET", url);
    request.responseType = 'json';

    request.onload = function() {
        if (request.status >= 400) return;
        results = request.response;
    };

    request.send();
}