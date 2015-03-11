# Licensed under the Unlicense (http://unlicense.org)
# Made by horriblecoders.com
# Chat Program
import socket
import threading

# Config
MODE = "SERVER"         # Modes can either be SERVER or CLIENT	
HOST = ""               # Symbolic name meaning all available interfaces
PORT = 1337             # Arbitrary non-privileged port (> 1024)
chatName = "Default"    # Your name
friendName = ""         # Leave this blank
connected = False       # Leave this False

def send():
	while True:
		message = input(chatName + ": ")
		data = message.encode()
		conn.sendall(data)

def recv():
	while True:
		data = conn.recv(1024)
		if not data: break
		print(friendName.decode() + ":",data.decode())

if (MODE == ''):
	MODE = "CLIENT"

if (chatName == ''):
	chatName = input("Enter Name: ")

if (MODE=="SERVER"):
	print("Starting in server mode...")
	while not connected:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind((HOST, PORT))
			s.listen(1)
			print("Server Started: Listening")
			conn, addr = s.accept()
			friendName = conn.recv(1024)
			conn.sendall(chatName.encode())
			print(friendName.decode(), 'connected by', addr)
			connected = True
			break
		except:
			nothing = input("ERROR: Failed to bind to port: " + str(PORT) + ". Press Enter to try again...")
			continue

if (MODE=="CLIENT"):
	while not connected:
		print("Starting in client mode...")
		try:
			if(HOST == ''):
				HOST = input("Host IP: ")
			if(PORT == ''):
				PORT = 1337
			conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			conn.connect((HOST, PORT))
			connected = True
			conn.sendall(chatName.encode("utf-8"))
			friendName = conn.recv(1024)
			print("Connected to " + friendName.decode())
			connected = True
			break
		except:
			nothing = input("Error occurred when attempting to connect. Press Enter to try again...")
			continue
		
thread_list = []

thread_list.append(threading.Thread(target = recv))
thread_list.append(threading.Thread(target = send))

for thread in thread_list:
	thread.start()
for thread in thread_list:
	thread.join()
