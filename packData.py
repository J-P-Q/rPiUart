import serial
import numpy as np

def parseFrame(buffer):	# packs start + 16 bytes into eight 16 bit data in array
	rawBuffer = np.frombuffer(buffer, dtype = np.uint8)

	payload = rawBuffer[1:17].reshape(8, 2)
	
	channels = (payload[:, 0].astype(np.uint16) << 8) | payload[:, 1]
	return channels

# MAIN:

PORT = "/dev/ttyUSB0"
BAUD = 896000
uartData = serial.Serial(PORT, BAUD, timeout=0.5)


try:
	while (1):
		if(uartData.inWaiting() > 0):
			buffer = uartData.read(17)

			if (buffer[0] == 0xAA):	# check start byte
				channels = parseFrame(buffer)
				print(channels)



except KeyboardInterrupt:
	print("\n Stopped")

finally:
	uartData.close()
