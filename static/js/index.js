const request = new XMLHttpRequest();
let currentUser = "";

function createUser() {
    let usernameBox = document.getElementById("userToCreate");
    let username = usernameBox.value;
    let url = "http://127.0.0.1:5000/createUser/" + username;
    request.open("POST", url);

    request.onload = function() {
        if (request.status >= 400) return;
        currentUser = username;
        document.getElementById("current-user").innerHTML = "Current User: <strong>" + currentUser + "</strong>";
        document.getElementById("favorite-movie").innerHTML = "Favorite Movie: ________";
        document.getElementById("saved-movies-list").innerHTML = "";
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
        document.getElementById("current-user").innerHTML = "Current User: ________";
        document.getElementById("favorite-movie").innerHTML = "Favorite Movie: ________";
        document.getElementById("saved-movies-list").innerHTML = "";
    };

    request.send();
}

function getFavoriteMovie() {
    let url = "http://127.0.0.1:5000/getFavoriteMovie/" + currentUser;
    request.open("GET", url);
    request.responseType = "json";
    request.onload = function() {
        if (request.status >= 400) return;
        let movie = request.response
        if (movie[0] != undefined) {
            document.getElementById("favorite-movie").innerHTML = "Favorite Movie: <strong>" + movie[0] + "</strong>";
        } else {
            document.getElementById("favorite-movie").innerHTML = "Favorite Movie: ________";
        }
    }
    request.send();
}

function updateFavoriteMovie(movieID, title) {
    let url = "http://127.0.0.1:5000/updateFavoriteMovie/" + currentUser + "/" + movieID;
    request.open("PUT", url)
    request.onload = function() {
        if (request.status >= 400) return;
        document.getElementById("favorite-movie").innerHTML = "Favorite Movie: <strong>" + title + "</strong>";
    }
    request.send();
}

function getMovieList(username) {
    if (username == null) {
        let usernameBox = document.getElementById("userToSwitchTo");
        username = usernameBox.value;
    }

    let ol = document.getElementById("saved-movies-list");
    ol.innerHTML = ""; // Resets Saved Movies List

    let url = "http://127.0.0.1:5000/getMovieList/" + username;
    request.open("GET", url)
    request.responseType = 'json';

    request.onload = function() {
        if (request.status >= 400) return;
        currentUser = username;
        document.getElementById("current-user").innerHTML = "Current User: <strong>" + currentUser + "</strong>";

        let movieList = request.response;
        for (var key in movieList) {
            if (!movieList.hasOwnProperty(key)) {
                break;
            }

            let movieID = movieList[key][0]
            
            let li = document.createElement("li");
            li.id = movieID;
            li.className = "movie";
            
            let title = document.createElement("p");
            title.innerHTML = movieList[key][1];
            li.appendChild(title);
            
            let deleteButton = document.createElement("button");
            deleteButton.innerHTML = "Delete Movie";
            deleteButton.addEventListener("click", function() {deleteMovie(movieID)});
            li.appendChild(deleteButton);

            ol.appendChild(li);
        }

        getFavoriteMovie();
    };

    request.send()
}

function addMovie(movieID) {
    let username = currentUser;
    let url = "http://127.0.0.1:5000/addMovie/" + username + "/" + movieID;
    request.open("PUT", url);
    request.onload = function() {
        if (request.status >= 400) return;
        getMovieList(currentUser); // Refreshes Saved Movies
    };
    request.send();
}

function deleteMovie(movieID) {
    let username = currentUser;
    let url = "http://127.0.0.1:5000/deleteMovie/" + username + "/" + movieID;
    request.open("DELETE", url);
    request.onload = function() {
        if (request.status >= 400) return;
        getMovieList(currentUser); // Refreshes Saved Movies
    };
    request.send();
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
        let results = request.response;

        for (var key in results) {
            if (!results.hasOwnProperty(key)) {
                break;
            }
            
            let li = document.createElement("li");
            li.id = "result" + numResults.toString();
            li.className = "search-result";

            let movieID = results[key][0]
            
            let title = document.createElement("p");
            title.innerHTML = results[key][1];
            li.appendChild(title);

            let addButton = document.createElement("button");
            addButton.innerHTML = "Add Movie";
            addButton.addEventListener("click", function() {addMovie(movieID)});
            li.appendChild(addButton);

            let favoriteButton = document.createElement("button");
            favoriteButton.innerHTML = "Set As Favorite";
            favoriteButton.addEventListener("click", function() {updateFavoriteMovie(movieID, title.innerHTML)});
            li.appendChild(favoriteButton);
            
            ol.appendChild(li);
            numResults++;
        }
    };

    request.send();
}

function advanced_query(queryID) {
    let ol = document.getElementById("aq" + queryID.toString() + "-results");
    ol.innerHTML = ""; // Resets Query Results

    let url = "http://127.0.0.1:5000/aq" + queryID;
    request.open("GET", url);
    request.responseType = "json";

    request.onload = function() {
        if (request.status >= 400) return;
        let results = request.response;

        for (var key in results) {
            if (!results.hasOwnProperty(key)) {
                break;
            }

            let li = document.createElement("li");
            li.className = "search-result";
            li.innerHTML = results[key];
            ol.appendChild(li)
        }
    };

    request.send();
}