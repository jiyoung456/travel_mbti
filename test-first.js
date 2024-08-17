document.addEventListener('DOMContentLoaded', () => {
    // Object to store the selected values, keyed by dropdown name
    const selectedValues = {};

    // Find all dropdown items
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    
    // Add click event listeners to each dropdown item
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Retrieve the text content of the clicked item and the dropdown name
            const value = this.textContent.trim();
            const dropdownName = this.closest('.dropdown').querySelector('.btn').textContent.trim();
            
            // Update the dropdown button text to show the selected item
            this.closest('.dropdown').querySelector('.btn').textContent = value;

            // Update the selected value for this dropdown
            selectedValues[dropdownName] = value;

            // Log the current state of the selectedValues object
            console.log(selectedValues);
        });
    });

    // Additional code can be added here if you need to do something with the values, like sending them to a server
});
