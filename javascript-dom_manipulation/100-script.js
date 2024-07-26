// Function to add an item to the list
function addItem() {
    const list = document.querySelector('.my_list'); // Select the list
    const newItem = document.createElement('li'); // Create a new list item
    newItem.textContent = 'Item'; // Set the text content
    list.appendChild(newItem); // Add the new item to the list
}

// Function to remove the last item from the list
function removeItem() {
    const list = document.querySelector('.my_list'); // Select the list
    const lastItem = list.lastElementChild; // Get the last item
    if (lastItem) {
        list.removeChild(lastItem); // Remove the last item if it exists
    }
}

// Function to clear all items from the list
function clearList() {
    const list = document.querySelector('.my_list'); // Select the list
    list.innerHTML = ''; // Clear all items
}

// Add event listeners for the buttons
document.getElementById('add_item').addEventListener('click', addItem);
document.getElementById('remove_item').addEventListener('click', removeItem);
document.getElementById('clear_list').addEventListener('click', clearList);
