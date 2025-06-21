def analyze_logs():
    ip_counter = {}

    try:
        with open('logs/firewall.log', 'r') as log_file:
            for line in log_file:
                parts = line.strip().split(' ')
                if len(parts) > 1:
                    ip = parts[1].split(':')[0]
                    ip_counter[ip] = ip_counter.get(ip, 0) + 1

        for ip, count in ip_counter.items():
            if count >= 5:  # Suspicious if blocked 5 times
                print(f' Possible brute-force from {ip} ({count} attempts)')
                with open('logs/intrusion.log', 'a') as intru_file:
                    intru_file.write(f'Suspicious IP: {ip} - {count} attempts\n')

    except FileNotFoundError:
        print(' No logs found to analyze.')
