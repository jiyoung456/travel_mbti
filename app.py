from flask import Flask, request, jsonify, render_template
from catboost import CatBoostClassifier
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)

# 모델 로드 (pickle을 사용하여 catboost_model.pk1 파일에서 모델 로드)
with open("catboost_model2.pk1", "rb") as file:
    model = pickle.load(file)

def test_code():
    results = pd.read_csv('df_final.csv')
        
    traveler = {
        'GENDER': 0,
        'AGE_GRP': 40.0,
        'TRAVEL_STYL_1': 1,
        'TRAVEL_STYL_2': 2,
        'TRAVEL_STYL_5': 2,
        'TRAVEL_STYL_6': 4,
        'TRAVEL_STYL_7': 2,
        'TRAVEL_STYL_8': 4,
        'VISIT_ORDER': 13
    }
    
    filtered_results = results[
    (results['GENDER'] == traveler['GENDER']) &
    (results['AGE_GRP'] == traveler['AGE_GRP']) &
    (results['TRAVEL_STYL_1'] == traveler['TRAVEL_STYL_1']) &
    (results['TRAVEL_STYL_2'] == traveler['TRAVEL_STYL_2']) &
    (results['TRAVEL_STYL_5'] == traveler['TRAVEL_STYL_5']) &
    (results['TRAVEL_STYL_6'] == traveler['TRAVEL_STYL_6']) &
    (results['TRAVEL_STYL_7'] == traveler['TRAVEL_STYL_7']) &
    (results['TRAVEL_STYL_8'] == traveler['TRAVEL_STYL_8'])
    ]
    
    
    results = pd.DataFrame([], columns=['VISIT_AREA_NM', 'SCORE'])

    print(len(filtered_results['VISIT_AREA_NM']))
    
    for area in filtered_results['VISIT_AREA_NM']:
        input = list(traveler.values())
        input.append(area)

        
        score = model.predict(input)
        print([area, score])
        results = pd.concat([results, pd.DataFrame([[area, score]], columns=['VISIT_AREA_NM', 'SCORE'])])

    top_area=results.sort_values('SCORE', ascending=False)[:10]
    print(top_area)
    return top_area

    # 예측 결과 확인
    #print(f"Prediction result: {top_area}")
    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON 요청에서 데이터 가져오기
        data = request.json
        # if 'features' not in data:
        #     return jsonify({'error': 'features가 요청에 포함되지 않았습니다.'}), 400
        
        # #카테고리형 값들을 숫자 인덱스로 매핑
        # category_mapping = {
        #     'nature': 0,
        #     'city': 1,
        #     'plan': 2,
        #     'no-plan': 3,
        #     'photo': 4,
        #     'memory': 5,
        #     'famous': 6,
        #     'discover': 7,
        # }

        #features 값을 매핑된 숫자로 변환
        # features = [category_mapping[value] for value in data['features']]
        # features = np.array(features).reshape(1, -1)  # 1D array를 2D로 변환

        # print(f"Converted features: {features}")  # 디버깅용 출력
        
        df = test_code()
        
        # Converting DataFrame to JSON
        df_json = df.to_json(orient='records', force_ascii=False)

        # Returning the JSON response
        return jsonify(df_json)
    
    except Exception as e:
        # 오류가 발생한 경우 로그 출력 및 500 응답 반환
        print(f"오류 발생: {str(e)}")
        return jsonify({'error': '서버 내부 오류가 발생했습니다.'}), 500

@app.route('/test-first', methods=['GET'])
def test_first():
    # index.html 파일을 렌더링
    return render_template('test-first.html')

@app.route('/', methods=['GET'])
def first():
    # index.html 파일을 렌더링
    return render_template('first.html')

@app.route('/index', methods=['GET'])
def index():
    # index.html 파일을 렌더링
    return render_template('index.html')


@app.route('/result.html', methods=['GET'])
def result():
    # result.html 파일을 렌더링
    return render_template('result.html')

if __name__ == '__main__':
    
    app.run(debug=True, port=5500)
