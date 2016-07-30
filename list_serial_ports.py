import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

laserAddress = ""
for port in ports:
    print port
    typ = port[0]
    dev = port[2]
