# Hackxercise_6-4

# In the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured with a sniffer (namely, Wireshark), and figure out what is the source IP address of the fourth packet, and the destination IP address in the sixth packet.

# Submit your answers in the following text boxes. 

# This hackxercise cannot be implemented on your local Python environment because the pcap file is only available inside the Codeboard system.

# NOTE
# Don’t try to read the pcap file yourself - use scapy to read the pcap file and then choose which packet you need wisely.

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    for num, packet in enumerate(packets):
        if num==3: # 4th packet
            print("src ip:" + packet[IP].src)
        if num==5: # 6th packet
            print("dst ip:" + packet[IP].dst)
    pass # print the source and destination ip addresses

show_source_destination_ip_address()