#!/usr/bin/python
import time, os
class bcolors:
    NAME = '\033[92m'
    VSOFT = '\033[96m'
    SUB = '\033[93m'
    GREY = '\033[90m'
    BLUE = '\033[94m'
    FAIL = '\033[91m'
    
from os import system
os.system("clear")
print bcolors.NAME + "Welcome to Raspberry Pi Backup!"
print bcolors.VSOFT + "Powered by VSoft"
print bcolors.GREY + "==============================="
time.sleep(2)
print bcolors.SUB + "Which directory do you want the Backup to be saved in?"
print"(This can be saved on an External drive, or a NAS)"
q1 = (raw_input("> "))
print"The OS will now be backed up. DO NOT TURN OFF UNLESS FINISHED!"
time.sleep(3)
os.system("clear")
print"Backing Up..."
os.chdir(q1)
os.system("clear")
time.sleep(2)
print"Backing Up... DO NOT TURN OFF!"
system('dd if=/ of=Backup.img')
os.system("clear")
print("FINISHED!")
time.sleep(2)
print("Will now exit.")
time.sleep(3)
os.system("clear")
print bcolors.NAME + "Thanks for using Raspberry Pi Backup."
print bcolors.VSOFT + "Powered by VSoft."
print bcolors.BLUE + "Developed by Mark M. Jorgensen."
print bcolors.GREY + "=-----------------------------------="
print"."
