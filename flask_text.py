from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    text = request.form['text']

    # Huawei Cloud ModelArts API Request
    api_url = 'https://e77bab36de434d4bbb37a4b0588b64b9.apigw.ap-southeast-1.huaweicloud.com/v1/infers/5f81aef0-de37-4998-bfe6-bccdf31d06e1'
    headers = {'Content-Type': 'application/json',
               'x-auth-token': 'XXXXXXXXX'}

    data = {'text': text}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    result = response.json()
    print(result)

    # Extract the predicted label and scores
    predicted_label = result['predicted_label']
    scores = result['scores']

    return render_template('result.html', predicted_label=predicted_label, scores=scores)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
