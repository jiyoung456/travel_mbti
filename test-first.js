document.addEventListener('DOMContentLoaded', () => {
    // Object to store the selected values
    const selectedValues = {};

    // Find all dropdown items
    const dropdownItems = document.querySelectorAll('.dropdown-item');

    // Add click event listeners to each dropdown item
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Retrieve the text content of the clicked item
            const value = this.textContent.trim();

            // Find the associated dropdown button
            const dropdownButton = this.closest('.dropdown').querySelector('.btn');

            // Update the dropdown button text to show the selected item
            dropdownButton.textContent = value;

            // Get the key from the button's data-key attribute
            const key = dropdownButton.getAttribute('data-key');
            selectedValues[key] = value;  // Store the value under the correct key

            // Log the current state of the selectedValues object
            console.log(selectedValues);
        });
    });
});
