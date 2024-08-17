from flask import Flask, request, jsonify, render_template
from catboost import CatBoostClassifier
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)

# 모델 로드 (pickle을 사용하여 catboost_model.pk1 파일에서 모델 로드)
with open("catboost_model2.pk1", "rb") as file:
    model = pickle.load(file)
def map_travel_style(choice,style):
    mapping={
        'nature_city': {
            'nature': range(1, 5), 
            'city': range(5, 11)    
        },
        'plan_no_plan': {
            'plan': range(1, 5),
            'no-plan': range(5, 11)
        },
        'play_no_play' : {
            'no-play': range(1,5),
            'play': range(5,11)
        },
        'photo_memory': {
            'photo': range(5, 11),
            'memory': range(1,5)
        },
        'famous_discover': {
            'famous': range(5,11),
            'discover': range(1, 5)
        }
    }
    return sum(mapping[style][choice]) // len(mapping[style][choice])

def test_code(user_choices):
    results = pd.read_csv('df_final.csv')    
    
    # traveler = {
    #     'GENDER': 0,
    #     'AGE_GRP': 40.0,
    #     'TRAVEL_STYL_1': 1,
    #     'TRAVEL_STYL_2': 2,
    #     'TRAVEL_STYL_5': 2,
    #     'TRAVEL_STYL_6': 4,
    #     'TRAVEL_STYL_7': 2,
    #     'TRAVEL_STYL_8': 4,
    #     'VISIT_ORDER': 13
    # }
    traveler = {
        'GENDER': user_info.get('gender'),
        'AGE_GRP':user_info.get('age'),
        'TRAVEL_STYL_1': map_travel_style(user_choices['nature_city'], 'nature_city'),
        'TRAVEL_STYL_5': map_travel_style(user_choices['play_no_play'], 'play_no_play'),
        'TRAVEL_STYL_6': map_travel_style(user_choices['famous_discover'], 'famous_discover'),
        'TRAVEL_STYL_7': map_travel_style(user_choices['plan_no_plan'], 'plan_no_plan'),
        'TRAVEL_STYL_8': map_travel_style(user_choices['photo_memory'], 'photo_memory'),
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
    
from flask import Flask, request, jsonify, render_template
from catboost import CatBoostClassifier
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)

# 모델 로드 (pickle을 사용하여 catboost_model.pk1 파일에서 모델 로드)
with open("catboost_model2.pk1", "rb") as file:
    model = pickle.load(file)
def map_travel_style(choice,style):
    mapping={
        'nature_city': {
            'nature': range(1, 5), 
            'city': range(5, 11)    
        },
        'plan_no_plan': {
            'plan': range(1, 5),
            'no-plan': range(5, 11)
        },
        'play_no_play' : {
            'no-play': range(1,5),
            'play': range(5,11)
        },
        'photo_memory': {
            'photo': range(5, 11),
            'memory': range(1,5)
        },
        'famous_discover': {
            'famous': range(5,11),
            'discover': range(1, 5)
        }
    }
    return sum(mapping[style][choice]) // len(mapping[style][choice])

def test_code(user_choices, user_info):
    results = pd.read_csv('df_final.csv')

    # traveler 객체 생성
    traveler = {
        'GENDER': user_info['gender'],  # gender 정보를 그대로 사용
        'AGE_GRP': user_info['age'],  # age 정보를 그대로 사용
        'TRAVEL_STYL_1': map_travel_style(user_choices['nature_city'], 'nature_city'),
        'TRAVEL_STYL_5': map_travel_style(user_choices['play_no_play'], 'play_no_play'),
        'TRAVEL_STYL_6': map_travel_style(user_choices['famous_discover'], 'famous_discover'),
        'TRAVEL_STYL_7': map_travel_style(user_choices['plan_no_plan'], 'plan_no_plan'),
        'TRAVEL_STYL_8': map_travel_style(user_choices['photo_memory'], 'photo_memory'),
        'VISIT_ORDER': 13  # VISIT_ORDER는 고정 값으로 설정
    }
    
    print("Traveler 객체 구성:", traveler)

    # traveler 객체를 이용해 결과 필터링
    filtered_results = results[
        (results['GENDER'] == traveler['GENDER']) &
        (results['AGE_GRP'] == traveler['AGE_GRP']) &
        (results['TRAVEL_STYL_1'] == traveler['TRAVEL_STYL_1']) &
        (results['TRAVEL_STYL_5'] == traveler['TRAVEL_STYL_5']) &
        (results['TRAVEL_STYL_6'] == traveler['TRAVEL_STYL_6']) &
        (results['TRAVEL_STYL_7'] == traveler['TRAVEL_STYL_7']) &
        (results['TRAVEL_STYL_8'] == traveler['TRAVEL_STYL_8'])
    ]
    
    results = pd.DataFrame([], columns=['VISIT_AREA_NM', 'SCORE'])
    
    # traveler 객체를 사용해 점수 예측
    for area in filtered_results['VISIT_AREA_NM']:
        input_data = list(traveler.values())
        input_data.append(area)
        
        score = model.predict([input_data])  # 입력값을 리스트로 감싸서 전달
        print([area, score])
        results = pd.concat([results, pd.DataFrame([[area, score]], columns=['VISIT_AREA_NM', 'SCORE'])])
    
    # 상위 10개 결과 정렬
    top_area = results.sort_values('SCORE', ascending=False).head(10)
    print(top_area)
    return top_area

    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON 요청에서 데이터 가져오기
        data = request.json

        # user_info와 user_choices 추출
        user_info = {
            'age': data.get('age'),
            'gender': data.get('gender')
        }
        
        user_choices = {
            'nature_city': data.get('nature_city'),
            'plan_no_plan': data.get('plan_no_plan'),
            'play_no_play': data.get('play_no_play'),
            'photo_memory': data.get('photo_memory'),
            'famous_discover': data.get('famous_discover')
        }
        
        # test_code 함수에 전달
        df = test_code(user_choices, user_info)  # user_choices와 user_info 전달
        
        # DataFrame을 JSON으로 변환하여 반환
        df_json = df.to_json(orient='records', force_ascii=False)
        
        # traveler 객체를 API 응답에 포함
        traveler = {
            'GENDER': user_info['gender'],
            'AGE_GRP': user_info['age'],
            'TRAVEL_STYL_1': map_travel_style(user_choices['nature_city'], 'nature_city'),
            'TRAVEL_STYL_5': map_travel_style(user_choices['play_no_play'], 'play_no_play'),
            'TRAVEL_STYL_6': map_travel_style(user_choices['famous_discover'], 'famous_discover'),
            'TRAVEL_STYL_7': map_travel_style(user_choices['plan_no_plan'], 'plan_no_plan'),
            'TRAVEL_STYL_8': map_travel_style(user_choices['photo_memory'], 'photo_memory'),
            'VISIT_ORDER': 13
        }

        # traveler 객체와 예측 결과를 함께 반환
        return jsonify({'traveler': traveler, 'prediction': df_json})
    
    except Exception as e:
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
