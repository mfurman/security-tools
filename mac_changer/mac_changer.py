#!/usr/bin/env python

import subprocess

interface = input("interface > ")
mac = input("mac > ")

print("[+] Changing MAC address for " + interface + " to " + mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)