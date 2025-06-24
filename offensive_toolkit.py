import socket
import hashlib
import subprocess
import os
import time
import requests

# ------------------------
# 1. Port Scanner
# ------------------------
def port_scanner():
    target = input("Enter target IP address: ")
    print(f"\n[+] Scanning ports on {target}...\n")
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass

# ------------------------
# 2. Subdomain Enumerator
# ------------------------
def subdomain_enum():
    domain = input("Enter target domain (e.g. example.com): ")
    wordlist = input("Enter path to subdomain wordlist: ")

    if not os.path.exists(wordlist):
        print("Wordlist not found.")
        return

    with open(wordlist) as file:
        subdomains = file.read().splitlines()

    print(f"\n[+] Enumerating subdomains for {domain}...\n")
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=1)
            if response.status_code < 400:
                print(f"[FOUND] {url}")
        except:
            pass

# ------------------------
# 3. Hash Cracker
# ------------------------
def hash_cracker():
    hash_input = input("Enter the hash to crack: ")
    hash_type = input("Hash type (md5, sha1, sha256): ")
    wordlist = input("Enter path to wordlist: ")

    if not os.path.exists(wordlist):
        print("Wordlist not found.")
        return

    with open(wordlist, 'r') as file:
        for word in file.read().splitlines():
            word = word.strip()
            if hash_type == "md5":
                result = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                result = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "sha256":
                result = hashlib.sha256(word.encode()).hexdigest()
            else:
                print("Unsupported hash type.")
                return
            if result == hash_input:
                print(f"[SUCCESS] Hash cracked: {word}")
                return
    print("[FAILED] Hash not found in wordlist.")

# ------------------------
# 4. Nmap Wrapper
# ------------------------
def nmap_wrapper():
    target = input("Enter IP or hostname to scan with Nmap: ")
    print("\n[+] Running Nmap...\n")
    try:
        subprocess.call(["nmap", "-F", target])
    except FileNotFoundError:
        print("Nmap is not installed or not in PATH.")

# ------------------------
# 5. Email Spoof Simulator
# ------------------------
def email_spoof_sim():
    sender = input("Enter fake sender email: ")
    recipient = input("Enter recipient email (simulation only): ")
    subject = input("Enter email subject: ")
    print("\n--- Simulated Email ---")
    print(f"From: {sender}")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print("Body: This is a harmless spoof simulation.")
    print("--- End ---\n")

# ------------------------
# 6. Brute-force Simulator
# ------------------------
def brute_force_sim():
    username = "admin"
    password = "password123"
    print("\n[+] Starting brute-force demo against simulated login\n")
    wordlist = input("Enter path to password wordlist: ")

    if not os.path.exists(wordlist):
        print("Wordlist not found.")
        return

    with open(wordlist, 'r') as file:
        for word in file.read().splitlines():
            print(f"Trying: {word}")
            if word == password:
                print(f"[SUCCESS] Password cracked: {word}\n")
                return
            time.sleep(0.1)
    print("[FAILED] Password not found in wordlist.")

# ------------------------
# Main Menu
# ------------------------
def main():
    while True:
        print("""
========= Offensive Python Toolkit =========
1. Port Scanner
2. Subdomain Enumerator
3. Hash Cracker
4. Nmap Wrapper
5. Email Spoof Simulation
6. Brute-force Simulator
0. Exit
""")
        choice = input("Select a tool: ")
        if choice == '1':
            port_scanner()
        elif choice == '2':
            subdomain_enum()
        elif choice == '3':
            hash_cracker()
        elif choice == '4':
            nmap_wrapper()
        elif choice == '5':
            email_spoof_sim()
        elif choice == '6':
            brute_force_sim()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.\n")

if __name__ == '__main__':
    main()
