#  Các thư viện dùng : OpenCV, Socket, Pickle, Struct
import socket,cv2,pickle,struct

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
HOST_IP = socket.gethostbyname(HOST_NAME)
print("Dia chi IP :",HOST_IP)
port = int(input("Nhap cong port: "))
socket_address = (HOST_IP,port)

#Socket bind:
server_socket.bind(socket_address)
#Socket Listen
server_socket.listen(5)
print("Dang lang nghe tai:",socket_address)

#Socket Accept
while True:
    client_socket,clientadrr = server_socket.accept()
    print('Da ket noi den',clientadrr)

    vc = cv2.VideoCapture(0)
    if client_socket:
      if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
      else:
        rval = False
    while rval:

        rval, frame = vc.read()
        a=pickle.dumps(frame)
        message = struct.pack("Q",len(a))+a
        client_socket.sendall(message)
        cv2.imshow("Server", frame)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            client_socket.close()
            break

    cv2.destroyWindow("Server")
    vc.release()
