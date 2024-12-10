import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

#Get the interface name from the environment variable
interface = os.getenv("your_Wifi_interface")
wifi_network = os.getenv("your_wifi_network")

# Set the wlx040c735a5834 interface to down then set it to monitor mode
os.system(f"sudo ifconfig {interface} down")
os.system(f"sudo iwconfig {interface} mode monitor")


# Print the targets connected to our wifi network ESSID only and note our target station BSSID
os.system(f"sudo airodump-ng --band b {interface}")

#print their ip addresses
os.system(f"sudo arp-scan --interface={interface} --localnet")