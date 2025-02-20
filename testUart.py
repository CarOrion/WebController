import serial
import time

# UART portunu aç (Raspberry Pi'nin varsayılan UART portu /dev/serial0)
serial_port = "/dev/ttyAMA0"  # UART portu 
ser = serial.Serial(serial_port, baudrate=9600)

while True:
    ser.write('W'.encode())  # "W" karakterini byte olarak gönder
    print("Sent: W")
    time.sleep(1)  # 1 saniye bekle
