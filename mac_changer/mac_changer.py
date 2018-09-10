#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="mac", help="New MAC address")

parser.parse_args()


interface = input("interface > ")
mac = input("MAC > ")

print("[+] Changing MAC address for " + interface + " to " + mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw","ether", mac])
subprocess.call(["ifconfig", interface, "up"])