// Function to fetch the translation of "Hello"
function translateHello() {
    const languageCode = document.getElementById('language_code').value; // Get selected language code
    const helloElement = document.getElementById('hello'); // Element to display the translation

    if (languageCode) {
        const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`; // Construct the API URL

        fetch(url)
            .then(response => response.json()) // Parse the JSON response
            .then(data => {
                helloElement.textContent = data.hello; // Update the hello element with the translation
            })
            .catch(error => {
                helloElement.textContent = 'Error fetching translation'; // Handle errors
                console.error('Error:', error); // Log error to console
            });
    } else {
        helloElement.textContent = 'Please select a language'; // Prompt user to select a language
    }
}

// Add event listener to the button
document.getElementById('btn_translate').addEventListener('click', translateHello);
