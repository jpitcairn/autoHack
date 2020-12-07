#! /usr/bin/env python3

###################################
# Author: Jordan Pitcairn
# Date: 06/12/2020
# Version: 0.01
###################################

# import modules
import os 
from datetime import datetime
import netifaces as ni

# Setup Variables
project = "Test"
scope = ['192.168.1.1','192.168.1.2']

# Script Logic Variables - DO NOT EDIT
ni.ifaddresses('eth0')
attack_IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']




def Setup(): # Setup Project folder structure
	if not os.path.exists(project):
		os.mkdir(project)

	for host in scope:
		host = project + "/" + host
		if not os.path.exists(host):
			os.mkdir(host)
	os.chdir(project)


def Scan(): # Initialise Scan of scope
	
	# Begin Logging
	f = open("log.txt", "a", 1)
	
	# Quick nmap Scan
	for host in scope:
		print("*" * 50) 
		print("Quick Nmap Scan in progress on host:", host)
		f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Quick Nmap Scan on " + host + " from " + attack_IP + "\n")
		os.system('nmap -oG ' + host + '/nmap_Quick ' + host + ' > /dev/null 2>&1')



	# Full nmap Scan
	for host in scope:
		print("*" * 50) 
		print("Full TCP Nmap Scan in progress on host:", host)
		f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " Full TCP Nmap Scan on " + host + " from " + attack_IP + "\n")
		os.system('nmap -sC -sV -p- -oG ' + host + '/nmap_Full ' + host + ' > /dev/null 2>&1')

	#TestSSL Scan
	for host in scope:
		print("*" * 50) 
		print("TestSSL in progress on host:", host)
		f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " TestSSL Scan on " + host + " from " + attack_IP + "\n")
		os.system('/opt/testssl.sh/testssl.sh --file ' + host + '/nmap_Full -oH ' + host + '/testssl > /dev/null 2>&1')



def main():
	print("/" * 50)
	print("Setting up Project", project)
	print("/" * 50)
	Setup()
	print("Starting Scan phase")
	print("/" * 50)
	Scan()

if __name__ == "__main__":
    # execute only if run as a script
    main()
