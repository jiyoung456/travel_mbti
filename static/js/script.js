document.addEventListener("DOMContentLoaded", () => {
  const selectedValues = {};
  // Object to store the selected values, keyed by dropdown data-key

  // Find all dropdown items
  const questionBoxes = document.querySelectorAll(".question-box");

  // Add click event listeners to each dropdown item
  questionBoxes.forEach((item) => {
    item.addEventListener("click", function (event) {
      event.preventDefault(); // Prevent default link behavior

      // Retrieve the text content of the clicked item and the dropdown data-key

      const questionArea = this.closest(".question-area");
      const questionKey = questionArea.getAttribute("data-question");

      // Update the dropdown button text to show the selected item
      // dropdownButton.textContent = value;

      // Update the selected value for this dropdown in selectedValues object

      const value = this.getAttribute("data-value");
      selectedValues[questionKey] = value;

      // Remove 'active' class from all items in the current dropdown
      // const dropdownMenu = this.closest('.dropdown-menu');
      // dropdownMenu.querySelectorAll('.dropdown-item').forEach(item => {
      //     item.classList.remove('active');
      // });

      questionArea.querySelectorAll(".question-box").forEach((box) => {
        box.classList.remove("active");
      });

      // Add 'active' class to the selected item
      this.classList.add("active");
      // Log the current state of the selectedValues object

      console.log(selectedValues);
    });
  });

  // Additional code can be added here if you need to do something with the values, like sending them to a server
});
