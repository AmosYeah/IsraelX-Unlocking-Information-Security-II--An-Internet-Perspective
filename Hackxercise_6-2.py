# Hackxercise_6-2

# Within the following codeboard we prepared a pcap file for you - that is, a traffic capture file collected by wireshark. Your task is to process this file, and extract the source MAC address of the 3rd captured packet.

# To do this, you should use the scapy python package, which can process pcap files (among many other things it can do).

# You can read the scapy documentation here.

# Submit your answers in the following text boxes. 

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)

    for num,pkt in enumerate(packets):
        if num==2:
            #print(pkt)
            e = pkt[Ether]
            print(e.src)

show_mac_address()