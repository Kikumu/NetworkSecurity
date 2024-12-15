import numpy as np


def ip_to_encode_format(ip_proto: int, total_protocols=255) -> np.array:
    ip_encode = np.zeros(total_protocols)
    ip_encode[ip_proto] = 1
    return ip_encode
