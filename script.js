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
    const selectedText = element.textContent.trim();
    const questionArea = element.parentNode;
    const siblings = questionArea.children;

    // Clear previous selections in the same group
    for (let i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('selected');
    }
    element.classList.add('selected');

    // Find if there's an existing entry from the same question area
    const areaIndex = Array.from(document.querySelectorAll('.question-area')).indexOf(questionArea);
    if (selectedValues[areaIndex]) {
        // Replace the existing value if one is already recorded from the same area
        selectedValues[areaIndex] = selectedText;
    } else {
        // Extend the array size if necessary
        selectedValues[areaIndex] = selectedText;
    }
    
    console.log(selectedValues);
}

let selectedValues = []; // This array stores the selections

function moveBus() {
    const busIcon = document.querySelector('.bus-icon');
    busIcon.classList.add('move-right');

    // After 2 seconds, redirect to the result page
    setTimeout(function() {
        window.location.href = 'result.html';
    }, 2000);
}