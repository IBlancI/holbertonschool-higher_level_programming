// Select the header element
const header = document.querySelector('header');
// Select the div with id "toggle_header"
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener to the div
toggleHeader.addEventListener('click', () => {
  // Check the current class and toggle it
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
