import socket

socket = socket.socket()

socket.bind(('localhost',87654))

socket.listen(5)

while True:
  ali, addd = socket.accept()
