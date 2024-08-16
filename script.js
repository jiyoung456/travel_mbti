document.addEventListener('DOMContentLoaded', () => {
    const questionBoxes = document.querySelectorAll('.question-box');
    questionBoxes.forEach(box => {
        box.addEventListener('click', function() {
            selectBox(this);
        });
    });

    document.querySelector('.result-bt').addEventListener('click', function() {
        window.location.href = 'result.html'; // Ensure 'result.html' exists and is correct
    });
});

function selectBox(element) {
    // Ensure we are not adding the same question twice
    const selectedText = element.textContent.trim();
    if (!selectedValues.includes(selectedText)) {
        // Clear previous selection in the same group
        const siblings = element.parentNode.children;
        for (let i = 0; i < siblings.length; i++) {
            siblings[i].classList.remove('selected');
        }
        element.classList.add('selected');
        // Add new selection
        selectedValues.push(selectedText);
    }
    console.log(selectedValues);
}

let selectedValues = []; // This array stores the selections
