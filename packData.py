import serial

PORT = "/dev/ttyUSB0"
BAUD = 896000
uartData = serial.Serial(PORT, BAUD, timeout=0.5)


try:
	while (1):
		data = uartData.read(1)

		if len(data) == 0:
			continue
		firstByte = data[0]

		if firstByte != 0xAA:
			continue

		payload = uartData.read(16)

		if len(payload) < 16:
			continue

		channels = []

		
		line = ""
		for byte in payload:
			line = line + format(byte, "02X") + " "
		
		print(line)



except KeyboardInterrupt:
	print("\n Stopped")

finally:
	uartData.close()
