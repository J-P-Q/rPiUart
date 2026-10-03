import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 921600
uartData = serial.Serial(PORT, BAUD, timeout=0.5)


logFile = open("log.csv", "w")
logFile.write("ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8\n")


READY = 0
STATE = ""

nowTime =0
prevTime = 0

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


		nowTime = time.monotonic()

		if (savedValue > 0x0700 and READY and (nowTime - prevTime) > 0.5): # debounce 0.5s
			if STATE == "CLOSE":
				STATE = "OPEN"
			else:
				STATE = "CLOSE"

			READY = 0 
			prevTime = nowTime

		elif savedValue < 0x00F0:
			READY = 1

		line = line + "," + STATE
		
		
		print(line)
		logFile.write(line + "\n")
		



except KeyboardInterrupt:
	print("\n Stopped")

finally:
	uartData.close()
