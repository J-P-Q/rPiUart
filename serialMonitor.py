import serial

PORT = "/dev/ttyUSB0"
BAUD = 896000
ser = serial.Serial(PORT, BAUD, timeout=0.5)


try:
    while True:
        if ser.in_waiting > 0:
            data = ser.read(17)
            print(data.hex(' ').upper())
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()

