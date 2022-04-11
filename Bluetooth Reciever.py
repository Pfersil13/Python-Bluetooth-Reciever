import socket

# serverMACAddress1 = '24:6F:28:7B:ED:CA' ESP32
serverMACAddress1 = '00:13:EF:00:B0:2B'     #Put bluetooth MAC address
port = 1  # Needs to match value used on the device you are connecting to
size = 1024 #size of buffer to read
s1 = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)  # Bluetooth config

s1.connect((serverMACAddress1, port))   # Connect to selected port
print("con")
while True:
    data = s1.recv(size)     # Read de incoming data
    if data:
        print(data)
        with open('PruebaBLE_R_Consumo.RAW', 'ab') as f:    # Open new file in binary and write a new line
            f.write(data)   # Write buffer in n

s1.close()

