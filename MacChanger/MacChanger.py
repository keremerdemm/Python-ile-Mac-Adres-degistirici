import subprocess
import time
import sys



print("MAC CHANGER STARTED...")
time.sleep(2)
exit = "exit"
wlan0 = "wlan0"
eth0 = "eth0"
wlan1 = "wlan1"
while True:
    try:
        interface = input("enter interface wlan0,eth0,wlan1: ")

    except NameError:
        print("\nnot valid interface!\n")
        continue

    else:
        break

if (interface == exit):
    print("\nexiting")
    time.sleep(1)
    sys.exit()


time.sleep(1)
print("\nLoading...")
time.sleep(2)
while True:
    try:
        mac_address = str(raw_input("\nenter new MAC address: "))
    except TypeError:
        print("invalid mac address!")
        continue
    else:
        break
if (mac_address == exit):
    print("\nexiting")
    time.sleep(1)
    sys.exit()

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])

