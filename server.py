import logging
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
sliderValue = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/keypress', methods=['POST'])
def keypress():
    data = request.get_json()
    key = data.get('key')
    print(f"Sunucuya gönderilen tuş: {key}, Slider değeri: {sliderValue}")
    return jsonify({"status": "success", "key": key})

@app.route('/slider', methods=['POST'])
def slider():
    global sliderValue
    data = request.get_json()
    sliderValue = data.get('value')
    return jsonify({"status": "success", "value": sliderValue})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
