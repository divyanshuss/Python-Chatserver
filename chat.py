import socket
import threading
import sys
import os
import pyfiglet

os.system("tput setaf 3")
p=pyfiglet.figlet_format("H E Y ",font="doh")
print(p)


def receiver(ip1, port1):
    sd = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, sd)
    s.bind((ip1, p1))
    while True:
        x = s.recvfrom(1024)
        print('Received Message : ',x[0].decode())
        

def sender(ip2, port2):
    sd = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, sd)
    while True:
        msg = input()
        s.sendto(msg.encode(), (ip2, p2))
        print('Your Message : ', msg)
        


ip1= input("Enter receiver's ip address")
p1 = int(input("Reciever's port number : ")
ip2= input("Enter senders's ip address")
p2 = int(input(" Sender's port number : "))

t1 = Thread(target=sender, args=(ip2, p2))
t2 = Thread(target=receiver, args=(ip1, p1))

t1.start()
t2.start()
