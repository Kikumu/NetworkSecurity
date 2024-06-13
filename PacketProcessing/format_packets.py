from ProtocolProcessing.transport_protocol import ip_to_encode_format
from ProtocolProcessing.other_protocols import port_to_encode_format


def format_packets(packet_data: dict):
    print("******************************************")
    print(packet_data.keys())
    print(packet_data['layers'].keys())
    # protocols within the ip layer
    if 'ip' in packet_data['layers'].keys():
        print("protocol: ", packet_data['layers']['ip']['proto'])
        print(ip_to_encode_format(int(packet_data['layers']['ip']['proto'])))
    if 'tcp' in packet_data['layers'].keys():
        print("tcp data: ", packet_data['layers']['tcp'].keys())
        print("source port: ", packet_data['layers']['tcp']['srcport'])
        print(port_to_encode_format(int(packet_data['layers']['tcp']['srcport'])))
        print("destination port: ", packet_data['layers']['tcp']['dstport'])
        print(port_to_encode_format(int(packet_data['layers']['tcp']['dstport'])))
        print("port: ", packet_data['layers']['tcp']['port'])
    print("--------------------------------------")
