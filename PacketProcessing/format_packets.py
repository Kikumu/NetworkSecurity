from ProtocolProcessing.transport_protocol import ip_to_encode_format


def format_packets(packet_data: dict):
    print("******************************************")
    print(packet_data.keys())
    print(packet_data['layers'].keys())
    if 'ip' in packet_data['layers'].keys():
        print("protocol: ", packet_data['layers']['ip']['proto'])
        print(ip_to_encode_format(int(packet_data['layers']['ip']['proto'])))
        print("source ip:   ", packet_data['layers']['ip']['src'])
        print("source ip:   ", packet_data['layers']['ip']['addr'])
        print("source ip:   ", packet_data['layers']['ip']['src_host'])
        # print("destination ip:   ", packet_data['layers']['ip']['dst'])
    print("eth keys: ", packet_data['layers']['eth'].keys())
    if 'ip' in packet_data['layers'].keys():
        print("ip data: ", packet_data['layers']['ip'].keys())
    if 'tcp' in packet_data['layers'].keys():
        print("tcp data: ", packet_data['layers']['tcp'].keys())
        print("source port: ", packet_data['layers']['tcp']['srcport'])
        print("destination port: ", packet_data['layers']['tcp']['dstport'])
        print("port: ", packet_data['layers']['tcp']['port'])
    # print(type(packet))
    print("--------------------------------------")
