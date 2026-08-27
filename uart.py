import serial

comm = serial.Serial()

comm.baudrate = 38400
comm.port = '/dev/ttyUSB0'
comm.stopbits = 1
comm.bytesize = 8
comm.parity = 'N'
comm.timeout = 0	# polls for 0s before context switching to other processes

comm.close()
