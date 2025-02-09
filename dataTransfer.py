from flask import Flask, request
import atexit
#import spidev
import serial


stopState = True

#UART Start
ser = serial.Serial("/dev/serial0", baudrate=115200)
#baudrate may be 250000

'''#SPI Start
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 2000000'''

app = Flask(__name__)

@app.route('/postService', methods=['POST'])
def keypress():
    data = request.get_json()
    
    key = data.get('key')
    event = data.get('event')
    slider_value = data.get('slider_value')
    
    if(stopState):
        send_data(key, event, slider_value, stopState)
        #print({key},{event},{slider_value})
    else:
        send_data(None, None, None, stopState)
        #print(f"Car in STOP state.{stopState}")
    
    return "Data received successfully!", 200

@app.route('/stopButton', methods=['POST'])
def stopButton():
    global stopState
    
    data = request.get_json()

    stopState = data.get('state')

    return "Data received successfully!", 200

def send_data(key, event, slider_value, stopState):
    #UART CODES
    if key not in ['W', 'A', 'S', 'D', 'X', None]:
        raise ValueError(f"Invaild data in KEY: {key}")
    if event not in ['C', 'R', None]:
        raise ValueError(f"Invaild data in EVENT: {event}")
    if slider_value is not None and not (0 <= slider_value <= 100):
        raise ValueError(f"Invaild data in SLIDERVALUE: {slider_value}")
    if stopState not in [True, False]:
        raise ValueError(f"Invaild data in STOPSTATE: {stopState}")


    key_byte = 0x00 if key is None else ord(key)
    event_byte = 0x00 if event is None else ord(event)
    slider_value_byte = 0xFF if slider_value is None else slider_value
    #255 used in None state because in hexadecimal 0x00 mean 0 and when slider_value in 0, its 0x00 too.
    stopStateByte = 1 if stopState else 0

    data = key_byte, event_byte, slider_value_byte, stopStateByte

    ser.write(bytes(data))
    #Values should be like: key_byte=W,A,S,D,None / event_byte=R,C,None / slider_value_byte = 0-100,255(You can check why we used 255 in upper comment.) / stopStateByte=True,False
    print(f"Data Sent: {bytes(data)}")

    '''#SPI CODES
    # String to byte
    key_byte = key.encode('utf-8')
    event_bytes = event.encode('utf-8') + b'\x00'
    slider_bytes = str(slider_value).encode('utf-8') + b'\x00'  # Integer to byte
    bool_byte = b'\x01' if stopState else b'\x00' # Boolean to byte

    data = key_byte + event_bytes + slider_bytes + bool_byte

    spi.xfer2(list(data))'''

'''def close_spi():
    spi.close()'''

if __name__ == '__main__':
    app.run(port=5201, use_reloader=False)

#atexit.register(close_spi)
atexit.register(ser.close)