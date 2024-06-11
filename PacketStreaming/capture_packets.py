import pyshark
import psutil
from utils.packet_to_dict import packet_to_dict
from PacketProcessing.format_packets import format_packets


def list_interfaces():
    interfaces = psutil.net_if_addrs()
    interface_array = [interface for interface in interfaces]
    return interface_array


def start_capture():
    list_of_interfaces = list_interfaces()
    capture = pyshark.LiveCapture(interface=list_of_interfaces[1])
    for packet in capture.sniff_continuously():
        print("**************************************")
        # print(packet)
        packet_dict = packet_to_dict(packet)
        # I want to capture my packets
        format_packets(packet_dict)

