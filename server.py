from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)
sliderValue = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/button_down', methods=['POST'])
def button_down():
    data = request.get_json()
    key = data.get('key')
    slider_value = sliderValue
    response = requests.post('http://127.0.0.1:5201/postService', json={'key': key, 'event': 'clicked', 'slider_value': slider_value})
    print(f"{key} clicked.")
    return jsonify({"status": "success", 'event': 'clicked', "key": key})

@app.route('/button_up', methods=['POST'])
def button_up():
    data = request.get_json()
    key = data.get('key')
    slider_value = sliderValue
    response = requests.post('http://127.0.0.1:5201/postService', json={'key': key, 'event': 'released', 'slider_value': slider_value})
    print(f"{key} released.")
    return jsonify({"status": "success", 'event': 'released', "key": key})

@app.route('/slider', methods=['POST'])
def slider():
    global sliderValue
    data = request.get_json()
    sliderValue = data.get('value')
    return jsonify({"status": "success", "value": sliderValue})

@app.route('/stopButton', methods=['POST'])
def stop_button():
    data = request.get_json()
    stopState = data.get('state')
    response = requests.post('http://127.0.0.1:5201/stopButton', json={'state': stopState})
    print(stopState)
    return jsonify({"status": "success", "state": stopState})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
