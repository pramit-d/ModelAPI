import requests

def predict():
    endpoint = 'http://127.0.0.1:8000/predict'
    files = {'file': open('./initial-model_attack-0a63a9b9-sample-33.png', 'rb')}
    response = requests.post(endpoint, files=files)
    print(response.json())

predict()