import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
print('Ports:')
for p in ports:
    print(p.device, p.description, p.hwid)
