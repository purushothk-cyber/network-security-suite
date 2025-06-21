ALLOWED_IPS = ['127.0.0.1']
BLOCKED_PORTS = [23, 445, 3389]  # Example: Telnet, SMB, RDP

def filter_packet(packet):
    src_ip = packet[0][1].src
    dst_port = None
    proto = None

    if packet.haslayer('TCP'):
        dst_port = packet['TCP'].dport
        proto = 'TCP'
    elif packet.haslayer('UDP'):
        dst_port = packet['UDP'].dport
        proto = 'UDP'

    if dst_port in BLOCKED_PORTS:
        log_block_event(src_ip, dst_port, proto)
        return False

    return True


def log_block_event(ip, port, proto):
    with open('logs/firewall.log', 'a') as log_file:
        log_file.write(f'Blocked: {ip}:{port} via {proto}\n')
    print(f' Blocked {ip}:{port} via {proto}')
