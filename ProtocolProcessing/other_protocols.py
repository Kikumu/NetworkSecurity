import numpy as np


def port_to_encode_format(port_number: int, total_number_of_ports=65536) -> np.array:
    port_encode = np.zeros(total_number_of_ports)
    port_encode[port_number] = 1
    return port_encode


def ip_to_encode_format(ip_proto: int, total_protocols=255) -> np.array:
    ip_encode = np.zeros(total_protocols)
    ip_encode[ip_proto] = 1
    return ip_encode
