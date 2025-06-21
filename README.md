#  Network Security Suite

A simple, GUI-based Network Security Suite that provides essential tools for network security such as packet sniffing, basic firewall, log analysis, and intrusion alerts.

---

## Features
-  File Sniffer
- Basic Firewall Rules
-  Real-time Alerts
- Log File Management
- GUI for Easy Navigation
- Simple Log Analysis Tool

---

##  Technologies Used
- Python
- Tkinter (for GUI)
- Scapy / OS Libraries (for packet sniffing)
- HTML (for log templates)

---

## Project Structure
```text
network_security_suite/
│
├── alerts.py                # Real-time alert system
├── basic firewall.py        # Basic firewall rules
├── firewall.py              # Firewall engine
├── gui.py                   # GUI application
├── log_analyzer.py          # Log file analyzer
├── main.py                  # Project entry point
├── requirements.txt         # Python dependencies
├── sniffer.py               # Packet sniffer
├── .gitignore               # Ignore cache and log files
│
├── logs/                    # Log files
│   ├── firewall.log
│   ├── intrusion.log
│   └── packets.log
│
└── templates/               # HTML files
    ├── index.html
    └── logs.html
