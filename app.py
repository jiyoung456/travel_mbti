from flask import Flask, request, jsonify, render_template
from catboost import CatBoostClassifier
import numpy as np
import pickle

app = Flask(__name__)

# 모델 로드 (pickle을 사용하여 catboost_model.pk1 파일에서 모델 로드)
with open("catboost_model.pk1", "rb") as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    print("gogo")
    # JSON 요청에서 데이터 가져오기
    data = request.json
    print(data)
    #features = np.array(data['features']).reshape(1, -1)  # 1D array를 2D로 변환
    
    # 예측 수행
    prediction = model.predict(features)
    
    # 결과 반환
    return jsonify({'prediction': int(prediction[0])})


@app.route('/', methods=['GET'])
def index():
    # index.html 파일을 렌더링
    return render_template('index.html')

@app.route('/result.html', methods=['GET'])
def result():
    # index.html 파일을 렌더링
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
