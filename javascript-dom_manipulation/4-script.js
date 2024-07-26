// Select the element with id "add_item"
const addItem = document.querySelector('#add_item');
// Select the ul element with class "my_list"
const myList = document.querySelector('.my_list');

// Add a click event listener to the "add_item" element
addItem.addEventListener('click', () => {
  // Create a new li element
  const newItem = document.createElement('li');
  // Set its text content
  newItem.textContent = 'Item';
  // Append the new li to the ul
  myList.appendChild(newItem);
});
