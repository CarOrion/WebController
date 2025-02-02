from flask import Flask, request

app = Flask(__name__)

@app.route('/keypress', methods=['POST'])
def keypress():
    data = request.get_json()
    
    key = data.get('key')
    event = data.get('event')
    slider_value = data.get('slider_value')
    
    print({key},{event},{slider_value})
    
    return "Data received successfully!", 200

if __name__ == '__main__':
    app.run(port=5201)