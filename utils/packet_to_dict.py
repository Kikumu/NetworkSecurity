from pyshark.packet.packet import Packet


def packet_to_dict(packet: Packet) -> dict:
    packet_dict = {'number': packet.number, 'length': packet.length, 'sniff_time': packet.sniff_time,
                   'sniff_timestamp': packet.sniff_timestamp, 'layers': {}}

    for layer in packet.layers:
        layer_name = layer.layer_name
        packet_dict['layers'][layer_name] = {}
        for field_name in layer.field_names:
            packet_dict['layers'][layer_name][field_name] = getattr(layer, field_name)

    return packet_dict
