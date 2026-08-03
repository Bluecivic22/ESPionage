import serial
import time
ports = ['COM5','COM4','COM3','COM1']
for p in ports:
    try:
        s = serial.Serial(p, 115200, timeout=2)
        time.sleep(0.5)
        s.write(b'\n')
        time.sleep(0.5)
        data = s.read(400)
        print(p, repr(data.decode('utf-8', 'ignore')))
        s.close()
    except Exception as e:
        print(p, 'ERR', e)
