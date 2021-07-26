const request = new XMLHttpRequest();
let currentUser = "";
let savedMovies = document.getElementById("saved-movies-list");

function createUser() {
    let usernameBox = document.getElementById("userToCreate");
    let username = usernameBox.value;
    let url = "http://127.0.0.1:5000/createUser/" + username;
    request.open("POST", url);

    request.onload = function() {
        if (request.status >= 400) return;
        currentUser = username;
        document.getElementById("current-user").innerHTML = "Current User: <strong>" + currentUser + "</strong>";
        savedMovies.innerHTML = "";
    };

    request.send();
}

function deleteUser() {
    let username = currentUser;
    let url = "http://127.0.0.1:5000/deleteUser/" + username;
    request.open("DELETE", url);

    request.onload = function() {
        if (request.status >= 400) return;
        currentUser = "";
        document.getElementById("current-user").innerHTML = "Current User: <strong>" + currentUser + "</strong>";
        savedMovies.innerHTML = "";
    };

    request.send();
}

function getMovieList() {
    let usernameBox = document.getElementById("userToSwitchTo");
    let username = usernameBox.value;
    let url = "http://127.0.0.1:5000/getMovieList/" + username;
    request.open("GET", url)
    request.responseType = 'json';

    request.onload = function() {
        if (request.status >= 400) return;
        currentUser = username;
        document.getElementById("current-user").innerHTML = "Current User: <strong>" + currentUser + "</strong>";
        movieList = request.response;
        numMovies = 0;

        for (var key in movieList) {
            if (!results.hasOwnProperty(key)) {
                break;
            }
            
            let li = document.createElement("li");
            li.id = "movie" + numMovies.toString();
            li.className = "movie";
            
            let title = document.createElement("p");
            title.innerHTML = results[key];
            li.appendChild(title);
            
            let deleteButton = document.createElement("button");
            addButton.innerHTML = "Delete Movie";
            addButton.addEventListener("click", function() {deleteMovie(title.innerHTML)});
            li.appendChild(deleteButton);

            savedMovies.appendChild(li);
            numMovies++;
        }
    };

    request.send()
}

function addMovie(title) {}

function deleteMovie(title) {}

function search() {
    let searchBox = document.getElementById("search-box")
    let text = searchBox.value;

    let ol = document.getElementById("search-results");
    ol.innerHTML = ""; // Resets Search Results
    numResults = 0;

    let url = "http://127.0.0.1:5000/search/" + text;
    request.open("GET", url);
    request.responseType = 'json';

    request.onload = function() {
        if (request.status >= 400) return;
        results = request.response;

        for (var key in results) {
            if (!results.hasOwnProperty(key)) {
                break;
            }
            
            let li = document.createElement("li");
            li.id = "result" + numResults.toString();
            li.className = "search-result";
            
            let title = document.createElement("p");
            title.innerHTML = results[key];
            li.appendChild(title);

            let addButton = document.createElement("button");
            addButton.innerHTML = "Add Movie";
            addButton.addEventListener("click", function() {addMovie(title.innerHTML)});
            li.appendChild(addButton);
            
            ol.appendChild(li);
            numResults++;
        }
    };

    request.send();
}

function aq1() {}

function aq2() {}