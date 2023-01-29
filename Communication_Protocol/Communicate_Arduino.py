import serial 
import time
arduino = serial.Serial(port='COM3', baudrate=115200,timeout=.1)
def write_read(x):
    arduino.write(bytes(x,'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
def write_data_txt(vl):
    with open("data.txt", "w") as file:
            file.write((vl) + "\n")

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value)
    print("Type is: ",type(value)) # printing the value
    write_data_txt(value.decode("utf-8") ) #convert byte to string and write into data.txt