// Fetch the translation of "hello" in French
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    // Check if the response is okay (status code 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON from the response
  })
  .then(data => {
    // Get the hello value from the response data
    const helloTranslation = data.hello;

    // Update the HTML element with id hello
    document.getElementById('hello').textContent = helloTranslation;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
