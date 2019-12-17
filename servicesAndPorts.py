#!/usr/bin/env python 3.8

import random

#randomly generated service name and enter its port to test yourself

#dictionary of service and ports
servicesAndPorts = {
    'ftp': 21,
    'ssh': 22,
    'telnet': 23,
    'dns': 53,
    'dhcp':67,
    'tftp':69,
    'http': 80,
    'https': 443,
    'rpcbind': 111,
    'ntp': 123,
    'ldap': 389,
    'samba': 445,
    'iscsi': 860,
    'nfs': 2049
}

#type 1 to play and 2 to exit the test
playOrExit = int(input("Play ---- 1\nExit   ---- 2\n"))

if playOrExit == 1:

    while True:
        #pick a random value
        rnd = random.choice(list(servicesAndPorts.keys()))
        print(rnd)

        port = int(input("Enter the port number: "))

        if port == int(servicesAndPorts[rnd]):
            print("correct!")
            continue

        else:
            print("wrong   :`(")
            
            replayOrExit = int(input("Replay ---- 1\nExit   ---- 2\n"))
            if replayOrExit == 1:
                continue
            else:
                break

elif playOrExit == 2:
    print ("That's all folks")