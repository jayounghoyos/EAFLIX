function filterMovies(genre) {
    // Oculta todas las películas
    let movies = document.querySelectorAll('.movie');
    movies.forEach(movie => {
        movie.style.display = 'none';
    });

    // Muestra solo las películas del género seleccionado
    let selectedMovies = document.querySelectorAll('.' + genre);
    selectedMovies.forEach(movie => {
        movie.style.display = 'block';
    });
}

function showAllMovies() {
    // Muestra todas las películas
    let movies = document.querySelectorAll('.movie');
    movies.forEach(movie => {
        movie.style.display = 'block';
    });
}

function searchMovies() {
    let searchTerm = document.querySelector('#search-bar input').value.toLowerCase();
    let movies = document.querySelectorAll('.movie');

    movies.forEach(movie => {
        let title = movie.querySelector('h2').innerText.toLowerCase();
        let displayStyle = title.includes(searchTerm) ? 'block' : 'none';
        movie.style.display = displayStyle;
    });
}

