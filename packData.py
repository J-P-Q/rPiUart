import serial

PORT = "/dev/ttyUSB0"
BAUD = 921600
uartData = serial.Serial(PORT, BAUD, timeout=0.5)


logFile = open("log.csv", "w")
logFile.write("ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8\n")


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
		for i in range(8):
			highByte = payload[i*2]
			lowByte = payload[i*2 + 1]
			value = (highByte << 8) + lowByte

			savedValue = value

			line = line + format(value, "012b")

			if i < 7:
				line = line + ","

		if savedValue > 0x0300:
			line = line + "," + "detected"
		else:
			line = line + "," + "N/A"
		
		print(line)
		logFile.write(line + "\n")
		



except KeyboardInterrupt:
	print("\n Stopped")

finally:
	uartData.close()
