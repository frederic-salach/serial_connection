import serial
import serial.tools.list_ports

print('SERIAL CONNECTION TEST')

check_connection = False

list_ports = list(serial.tools.list_ports.comports())

for port in list_ports:

    if 'USB' in port.description :
        serial_connection = serial.Serial(port.device,9600)

        if serial_connection.is_open == True :
            print('READY ON PORT', serial_connection.name)
            check_connection = True

if check_connection == False :
    print('NOT READY')
