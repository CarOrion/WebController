from flask import Flask, request
import atexit
import spidev


stopState = True
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
    
    if(stopState):
        send_data(key, event, slider_value, stopState)
        print({key},{event},{slider_value})
    else:
        send_data("X", "X", 0, stopState)
        print(f"Car in STOP state.{stopState}")
    
    return "Data received successfully!", 200

@app.route('/stopButton', methods=['POST'])
def stopButton():
    data = request.get_json()

    stopState = data.get('state')

    return "Data received successfully!", 200

def send_data(key, event, slider_value, stopState):

    # String to byte
    key_byte = key.encode('utf-8')
    event_bytes = event.encode('utf-8') + b'\x00'
    slider_bytes = str(slider_value).encode('utf-8') + b'\x00'  # Integer to byte
    bool_byte = b'\x01' if stopState else b'\x00' # Boolean to byte

    data = key_byte + event_bytes + slider_bytes + bool_byte

    spi.xfer2(list(data))

def close_spi():
    spi.close()

if __name__ == '__main__':
    app.run(port=5201, use_reloader=False)

atexit.register(close_spi)