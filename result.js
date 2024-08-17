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

    if (choices.join('-') === 'nature-long-trip-plan-photo-famous') {
        resultContent.innerHTML = '<h1>자연과 긴 여행, 계획이 있는 사진 여행 추천!</h1>';
    } else if (choices.join('-') === 'city-day-trip-no-plan-memory-discover') {
        resultContent.innerHTML = '<h1>도시와 짧은 당일치기, 무계획의 기억 남는 여행 추천!</h1>';
    } else {
        resultContent.innerHTML = '<h1>선택한 옵션에 해당하는 추천을 찾을 수 없습니다.</h1>';
    }

    // Continue with more combinations...
}
