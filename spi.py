from flask import Flask, request
import atexit
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 2000000

app = Flask(__name__)

@app.route('/postService', methods=['POST'])
def keypress():
    data = request.get_json()
    
    key = data.get('key')
    event = data.get('event')
    slider_value = data.get('slider_value')
    
    send_data(key, event, slider_value)
    print({key},{event},{slider_value})
    
    return "Data received successfully!", 200

@app.route('/stopButton', methods=['POST'])
def stopButton():
    data = request.get_json()

    stopState = data.get('state')

    send_data("S", stopState, 0)
    print(stopState)

    return "Data received successfully!", 200

def send_data(key, event, slider_value):

    # String to byte
    key_byte = key.encode('utf-8')
    event_bytes = event.encode('utf-8') + b'\x00'
    slider_bytes = str(slider_value).encode('utf-8') + b'\x00'  # Integer to byte

    data = key_byte + event_bytes + slider_bytes

    spi.xfer2(list(data))

def close_spi():
    spi.close()

if __name__ == '__main__':
    app.run(port=5201, use_reloader=False)

atexit.register(close_spi)