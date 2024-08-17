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

let selectedValues = [];

function selectBox(element) {
    const selectedText = element.dataset.value; // Use data-value instead of textContent
    const questionArea = element.parentNode;
    const siblings = questionArea.children;

    // Clear previous selections in the same group
    for (let i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('selected');
    }
    element.classList.add('selected');

    // Store the selected value in the array based on question area
    const areaIndex = Array.from(document.querySelectorAll('.question-area')).indexOf(questionArea);
    selectedValues[areaIndex] = selectedText;
    
    console.log(selectedValues);
}

function moveBus() {
    const busIcon = document.querySelector('.bus-icon');
    busIcon.classList.add('move-right');

    // After 2 seconds, redirect to the result page with query parameters
    setTimeout(function() {
        const queryString = selectedValues.join('-');
        window.location.href = `result.html?choices=${queryString}`;
    }, 2000);
}

document.addEventListener('DOMContentLoaded', () => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const choices = urlParams.get('choices');

    if (choices) {
        displayResult(choices.split('-'));
    }
});

function displayResult(choices) {
    const resultContent = document.getElementById('result-content');

    // Example logic to display content based on choices
    if (choices.includes('nature') && choices.includes('long-trip')) {
        resultContent.innerHTML = '<h1>자연과 긴 여행 추천!</h1>';
        // You can add more complex HTML content here based on the choices
    } else if (choices.includes('city') && choices.includes('day-trip') && choices.includes('no-plan')) {
        resultContent.innerHTML = '<h1>도시와 짧은 당일치기 여행, 계획이 필요 없는 여행 추천!</h1>';
    } else {
        resultContent.innerHTML = '<h1>선택한 옵션에 해당하는 추천을 찾을 수 없습니다.</h1>';
    }
}
