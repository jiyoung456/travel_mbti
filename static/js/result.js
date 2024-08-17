document.addEventListener("DOMContentLoaded", () => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const choices = urlParams.get("choices");

  if (choices) {
    displayResult(choices.split("-"));
  }
});

function displayResult(choices) {
  const resultContent = document.getElementById("result-content");

  // 선택된 옵션을 features로 사용하여 API 호출
  const features = choices;
  callPredictAPI(features).then((prediction) => {
    // 예측 결과를 UI에 반영
    resultContent.innerHTML = `<h1>추천 여행지: ${prediction}</h1>`;
  });
}

// 예측 API 호출 함수 (jQuery의 $.ajax를 사용하여 POST 요청)
function callPredictAPI(features) {
  const url = "http://127.0.0.1:5500/predict";

  return $.ajax({
    url: url,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ features: features }),
  })
    .then((data) => {
      if (data.error) {
        throw new Error(data.error);
      }
      alert(data);
      return data;
    })
    .catch((error) => {
      console.error("API 호출 중 오류 발생:", error);
    });
}
