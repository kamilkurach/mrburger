import socket
import keyboard

host = '192.168.5.107'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, 8080))

while True:
  if keyboard.read_key() == 'w':
    s = 'w'
    s_encode = s.encode()
    socket.send(s_encode)
    print('\n')
  elif keyboard.read_key() == 's':
    s = 's'
    s_encode = s.encode()
    socket.send(s_encode)
    print('\n')
  elif keyboard.read_key() == 'a':
    s = 'a'
    s_encode = s.encode()
    socket.send(s_encode)
    print('\n')
  elif keyboard.read_key() == 'd':
    s = 'd'
    s_encode = s.encode()
    socket.send(s_encode)
    print('\n')
  elif keyboard.read_key() == 'q':
    s = 'q'
    s_encode = s.encode()
    socket.send(s_encode)
    print('\n')
  elif keyboard.read_key() == 'c':
    print('\n')
    socket.close()
    break
