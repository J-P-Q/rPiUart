import serial

PORT = "/dev/ttyUSB1"
BAUD = 250000
ser = serial.Serial(PORT, BAUD, timeout=0.5)


try:
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            print(data.hex(' ').upper())
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()

