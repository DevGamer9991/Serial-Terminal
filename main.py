import serial

ser = serial.Serial("COM7")

print(ser.name)

command = "010C\r\n"

while True:
        ser.write(str.encode(command))
        response = ser.readline()
        print("Response: " + str(response))
        command = input("Send Command") + "\r\n"