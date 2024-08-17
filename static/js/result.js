document.addEventListener("DOMContentLoaded", () => {
  // URL에서 쿼리 문자열을 가져옴
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  // 선택된 모든 데이터를 객체로 변환
  const selectedValues = {};
  for (const [key, value] of urlParams.entries()) {
    selectedValues[key] = value;
  }

  // 데이터가 있으면 콘솔에 출력
  if (Object.keys(selectedValues).length > 0) {
    console.log("Final Selection:", selectedValues);

    // 선택된 데이터로 예측 API 호출 및 결과 표시
    displayResult(selectedValues);
  } else {
    console.error("No data found in URL parameters.");
  }
});

function displayResult(choices) {
  const resultContent = document.getElementById("result-content");

  // 선택된 옵션을 features로 사용하여 API 호출
  callPredictAPI(choices).then((prediction) => {
    // 예측 결과를 UI에 반영
    resultContent.innerHTML = `<h1>추천 여행지: ${prediction}</h1>`;
  });
}

function callPredictAPI(features) {
  const url = "http://127.0.0.1:5500/predict";

  return $.ajax({
    url: url,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(features),
  })
    .then((data) => {
      if (data.error) {
        throw new Error(data.error);
      }
      return data.prediction;
    })
    .catch((error) => {
      console.error("API 호출 중 오류 발생:", error);
    });
}
