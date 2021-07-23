const request = new XMLHttpRequest();

function login() {
    let usernameBox = document.getElementById("usernameBox");
    let username = usernameBox.value;
    /*
    let url = "http://127.0.0.1:5000/login/" + username;
    request.open("GET", url);
    request.responseType = 'json';

    request.onload = function() {
        if (request.status >= 400) return;
        results = request.response;
    };

    request.send();*/
}

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
        // console.log(results);

        for (var key in results) {
            if (!results.hasOwnProperty(key)) {
                break;
            }
            
            let li = document.createElement("li");
            li.id = "result" + numResults,toString();
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

function addMovie(movieName) {
    let savedMovies = document.getElementById("saved-movies");
    let movie = document.createElement("li");
    movie.className = "movie";
    movie.innerHTML = movieName;
    savedMovies.appendChild(movie);
}

function loadMovies(username) {}