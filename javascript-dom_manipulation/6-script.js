// Fetch character data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Check if the response is okay (status code 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON from the response
  })
  .then(data => {
    // Get the character name from the data
    const characterName = data.name;
    // Display the character name in the HTML element with id 'character'
    document.getElementById('character').textContent = characterName;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
