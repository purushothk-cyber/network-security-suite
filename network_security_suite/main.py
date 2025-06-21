from sniffer import start_sniffing
from log_analyzer import analyze_logs

def menu():
    while True:
        print("\n1. Start Sniffer + Firewall")
        print("2. Analyze Logs")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == '1':
            start_sniffing()
        elif choice == '2':
            analyze_logs()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
