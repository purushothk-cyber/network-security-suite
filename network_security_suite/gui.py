from flask import Flask, render_template, request, redirect, url_for
import threading
import time
import os
from sniffer import start_sniffing
from log_analyzer import analyze_logs

app = Flask(__name__)
sniffer_thread = None
sniffer_running = False

# Ensure logs exist
if not os.path.exists('logs/firewall.log'):
    open('logs/firewall.log', 'w').close()
if not os.path.exists('logs/packets.log'):
    open('logs/packets.log', 'w').close()
if not os.path.exists('logs/intrusion.log'):
    open('logs/intrusion.log', 'w').close()


def run_sniffer():
    global sniffer_running
    sniffer_running = True
    start_sniffing()


@app.route('/')
def home():
    with open('logs/firewall.log', 'r') as f:
        firewall_logs = f.readlines()
    with open('logs/packets.log', 'r') as f:
        packet_logs = f.readlines()
    with open('logs/intrusion.log', 'r') as f:
        intrusion_logs = f.readlines()

    return render_template('index.html', sniffer_running=sniffer_running,
                           firewall_logs=firewall_logs,
                           packet_logs=packet_logs,
                           intrusion_logs=intrusion_logs)


@app.route('/start')
def start():
    global sniffer_thread
    if not sniffer_running:
        sniffer_thread = threading.Thread(target=run_sniffer)
        sniffer_thread.start()
    return redirect(url_for('home'))


@app.route('/stop')
def stop():
    global sniffer_running
    sniffer_running = False
    return redirect(url_for('home'))


@app.route('/analyze')
def analyze():
    analyze_logs()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
