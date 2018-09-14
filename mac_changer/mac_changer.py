#!/usr/bin/env python

# EX: python mac_changer.py -i eth0 -m 00:11:22:33:44:55

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specifiy an interface, use --help for more info")
    elif not options.mac:
        parser.error("[-] Please specifiy MAC, use --help for more info")
    return options



def change_mac(interface, mac):
    print("[+] Changing MAC address for " + interface + " to " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.mac)