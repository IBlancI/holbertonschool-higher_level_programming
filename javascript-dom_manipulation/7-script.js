// Fetch movie data from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Check if the response is okay (status code 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON from the response
  })
  .then(data => {
    // Get the list of movies
    const movies = data.results;
    const listMovies = document.getElementById('list_movies'); // Get the ul element

    // Iterate through the movies and create list items for each title
    movies.forEach(movie => {
      const li = document.createElement('li'); // Create a new li element
      li.textContent = movie.title; // Set the text content to the movie title
      listMovies.appendChild(li); // Append the li to the ul
    });
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
