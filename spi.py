from flask import Flask, request
#import spidev
#import struct

#spi = spidev.SpiDev()
#spi.open(0, 0)
#spi.max_speed_hz = 2000000
#spi.mode = 0b00
app = Flask(__name__)

@app.route('/postService', methods=['POST'])
def keypress():
    data = request.get_json()
    
    key = data.get('key')
    event = data.get('event')
    slider_value = data.get('slider_value')
    
    #send_data(event, slider_value)
    print({key},{event},{slider_value})
    
    return "Data received successfully!", 200

@app.route('/stopButton', methods=['POST'])
def stopButton():
    data = request.get_json()

    stopState = data.get('state')

    print(stopState)

    return "Data received successfully!", 200

'''def send_data(angle, distance):
    """ 2 adet 16 bitlik integer gönder (Toplam 4 byte) """
    data = struct.pack('hh', angle, distance)
    response = spi.xfer2(list(data))
    print(f"Sent: Angle={angle}, Distance={distance}")
    print(f"Received: {response}")'''

if __name__ == '__main__':
    app.run(port=5201, use_reloader=False)