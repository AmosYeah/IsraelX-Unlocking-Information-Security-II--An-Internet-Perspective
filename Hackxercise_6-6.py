# Hackxercise_6-6

# In the following codeboard, use scapy to read the pcap file, which is a recording of some DNS traffic captured with a sniffer (namely, Wireshark), and figure out what is the domain that was being resolved, and what is its IP address.

# Submit your answers in the following text boxes. 

# This hackxercise cannot be implemented on your local Python environment because the pcap file is only available inside the Codeboard system.

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_domain_ip_address():
    packets = rdpcap(recording_path)
    for pkt in packets:
        if pkt.haslayer(DNSQR):
            domain = pkt[DNSQR].qname.decode("utf-8")
            print(domain)
            print(pkt.show())
    pass # print resolved domain and ip address

show_domain_ip_address()
