# I want to format my packets into a dataframe like format

def format_packets(packet_data: dict):
    print("******************************************")
    print(packet_data.keys())
    print(packet_data['layers'].keys())
    if 'ip' in packet_data['layers'].keys():
        print("protocol:   ", packet_data['layers']['ip']['proto'])
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