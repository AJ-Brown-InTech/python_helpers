#get host machine data
import platform
import os
from datetime import date


os_data = os.uname()
machine = os_data.machine
version = os_data.version
system = os_data.sysname
hostname = os_data.nodename
proccesor = platform.processor()
prompt = input(" Do you want to view your system data: [Y] or [N] ")


#print(prompt)
def console(response):
    if(response == "n" or response == "N"):
       return  print("goodbye :)")
    elif(response == "Y" or response == "y"):
        print(f"Today: {date.today()}")
        print(f"System: {system}\nMachine: {machine}\nVersion: {version}\nProccesor: {proccesor}\n")

console(prompt)