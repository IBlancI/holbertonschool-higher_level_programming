// Select the header element
const header = document.querySelector('header');
// Select the div with id "red_header"
const redHeader = document.querySelector('#red_header');

// Add a click event listener to the div
redHeader.addEventListener('click', () => {
  // Add the class "red" to the header
  header.classList.add('red');
});
