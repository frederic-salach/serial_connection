import serial
import serial.tools.list_ports

list_ports = list(serial.tools.list_ports.comports())
for port in list_ports:
    print(port.description)
