document.addEventListener('DOMContentLoaded', () => {
    // Array to store the selected values
    const selectedValues = [];

    // Find all dropdown items
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    
    // Add click event listeners to each dropdown item
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Retrieve the text content of the clicked item
            const value = this.textContent.trim();
            
            // Update the dropdown button text
            this.closest('.dropdown').querySelector('.btn').textContent = value;

            // Check if the item is already in the list to prevent duplicates
            if (!selectedValues.includes(value)) {
                selectedValues.push(value);
            }

            // For debugging: log the current state of the selectedValues array
            console.log(selectedValues);
        });
    });

    // If you need to do something with the values, like send them to a server
    // You can add more code here to handle that
});
