import cv2,socket,pickle,struct

#creat socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_IP = input("nhap dia chi IP: ")
port = int(input("Nhap cong port: "))
client_socket.connect((HOST_IP,port))
data =b""
payload_size = struct.calcsize("Q")
while True:
    while   len(data) < payload_size:
            packet = client_socket.recv(4*1024)
            if not packet:break
            data+=packet
    packet_msg_size = data[:payload_size]
    data = data[payload_size:]
    mgs_size = struct.unpack("Q",packet_msg_size)[0]

    while len(data)<mgs_size:
        data+=client_socket.recv(4*1024)
    frame_data = data [:mgs_size]
    data=data[mgs_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Received",frame)
    key = cv2.waitKey(1)& 0xFF
    if key == ord('q'):
        break
client_socket.close()
