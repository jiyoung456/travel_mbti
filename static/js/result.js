// 예측 API 호출 함수

function callPredictAPI(features) {
  const url = "http://127.0.0.1:5500/predict";

  return fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ features: features }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("API 요청에 실패했습니다.");
      }
      return response.json();
    })
    .then((data) => {
      console.log("예측 결과:", data.prediction);
      return data.prediction;
    })
    .catch((error) => {
      console.error("API 호출 중 오류 발생:", error);
    });
}

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
  //api콜하는 자리
  if (choices.join("-") === "nature-long-trip-plan-photo-famous") {
    resultContent.innerHTML =
      "<h1>자연과 긴 여행, 계획이 있는 사진 여행 추천!</h1>";
  } else if (choices.join("-") === "city-day-trip-no-plan-memory-discover") {
    resultContent.innerHTML =
      "<h1>도시와 짧은 당일치기, 무계획의 기억 남는 여행 추천!</h1>";
  } else {
    resultContent.innerHTML =
      "<h1>선택한 옵션에 해당하는 추천을 찾을 수 없습니다.</h1>";
  }
  alert(choices);

  features = choices;

  callPredictAPI(features);

  // callPredictAPI(choices);

  // Continue with more combinations...
}
// 예측 API 호출 함수 (위에서 작성한 jQuery 코드 포함)
function callPredictAPI(features) {
  alert("callPredictAPI");
  const url = "http://127.0.0.1:5500/predict";

  return $.ajax({
    url: url,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ features: features }),
    success: function (data) {
      console.log("예측 결과:", data.prediction);
    },
    error: function (xhr, status, error) {
      console.error("API 호출 중 오류 발생:", error);
    },
  });
}
