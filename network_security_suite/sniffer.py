from scapy.all import sniff
from firewall import filter_packet

def process_packet(packet):
    if filter_packet(packet):
        with open('logs/packets.log', 'a') as log_file:
            log_file.write(f'{packet.summary()}\n')

def start_sniffing():
    print('Sniffing started... (Press CTRL+C to stop)')
    sniff(prn=process_packet, store=False)
