# Hackxercise_6-3

# In the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured with a sniffer (namely, Wireshark), and figure out what is the username and the password.

# Submit your answers in the following text boxes. 

# This hackxercise cannot be implemented on your local Python environment because the pcap file is only available inside the Codeboard system.

# NOTE
# The traffic happens over port 8000, which scapy doesn't interpret as HTTP by default (because HTTP's default port is 80). To have it associate HTTP with port 8000, run:
# bind_layers(TCP, HTTP, dport=8000)
# bind_layers(TCP, HTTP, sport=8000)

# HINT
# There are actually two login attempts — the first one fails with "invalid credentials", and only the second one is successful.

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from re import *
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_username_password():
    packets = rdpcap(recording_path)
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    for packet in packets:
        # username = dict(re.findall("username=[a-zA-Z]+", packet, re.UNICODE))
        print(packet)
    pass # print Username and Password

show_username_password()
