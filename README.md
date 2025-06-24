# 🧰 Offensive Python Toolkit

> A modular command-line toolkit for cybersecurity testing, ethical demos, and automation — built entirely in Python.

## 📌 Description

This CLI-based tool combines multiple mini-offensive security tools in one script. Each module is designed for **educational and ethical use only**, to demonstrate common offensive techniques in a controlled and legal environment.

---

## ⚙️ Features

1. **Port Scanner** – Scans common TCP ports on a target host  
2. **Subdomain Enumerator** – Discovers subdomains using a wordlist  
3. **Hash Cracker** – Cracks MD5, SHA1, or SHA256 hashes via dictionary attack  
4. **Nmap Wrapper** – Runs basic Nmap scans from within the tool  
5. **Email Spoof Simulation** – Simulates the layout of a spoofed email (no sending)  
6. **Brute-force Simulator** – Demonstrates a password brute-force loop on a fake login

---

## 🚀 Usage

```bash
python offensive_toolkit.py
```

You will be presented with a menu to choose from the available tools.

> ⚠️ Some tools require wordlists or Nmap installed on your system.

---

## 📦 Requirements

### 🔹 Python Packages
Install with pip:

```bash
pip install requests
```

### 🔹 External Tools
You must have **Nmap** installed on your system for the Nmap Wrapper to function:

- **Linux:** `sudo apt install nmap`
- **macOS:** `brew install nmap`
- **Windows:** Download from [nmap.org](https://nmap.org/download.html) and add to PATH

Test with:
```bash
nmap -v
```

---

## 🧪 Example Wordlists

You can use:

- `/usr/share/wordlists/rockyou.txt` (Linux)
- Custom `.txt` files with passwords or subdomains

---

## 🔐 Skills Learned

- Ethical red team scripting  
- Socket programming and port scanning logic  
- Dictionary attacks and hash verification  
- Subprocess control and Nmap automation  
- Simulating email spoofing and password attacks  
- Modular CLI app development in Python

---

## 📂 File Structure

```
offensive_toolkit.py       
README.md                  
             
```

---

## ⚠️ Legal Disclaimer

This toolkit is intended for **educational use only**. Do **not** use it to attack or scan systems/networks without **explicit permission**. The author is not responsible for misuse.

---

## 👨‍💻 Author

**Edward Huber**  
GitHub: [@EdwardHuber](https://github.com/EdwardHuber)  
Email: edwardhuber1234@gmail.com
