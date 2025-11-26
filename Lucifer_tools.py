#!/usr/bin/env python3
import os, sys, time, hashlib, requests, socket
from urllib.parse import urlparse

GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(f"""
{RED}██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ 
██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝
██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝{RESET}
        {GREEN}Lucifer Termux Tools Pack{RESET}
            Developed by Foysal...
""")

# ----------------------------- #
# 1. Network Scanner (ARP)
# ----------------------------- #
def arp_scan():
    os.system("pkg install net-tools -y >/dev/null")
    print(GREEN + "\nScanning local devices...\n" + RESET)
    os.system("arp -a")

# ----------------------------- #
# 2. IP Info Lookup
# ----------------------------- #
def ip_lookup():
    ip = input("\nEnter IP or Domain: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print("\n")
        for k, v in r.items():
            print(f"{k} : {v}")
    except:
        print(RED + "Error fetching info!" + RESET)

# ----------------------------- #
# 3. Port Scanner
# ----------------------------- #
def port_scan():
    target = input("\nTarget IP: ")
    ports = [21, 22, 23, 53, 80, 443, 8080]
    print("\nScanning common ports...\n")
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(GREEN + f"[OPEN] Port {port}" + RESET)
        except:
            print(RED + f"[CLOSED] Port {port}" + RESET)

# ----------------------------- #
# 4. System Information
# ----------------------------- #
def system_info():
    print("\n")
    os.system("uname -a")
    os.system("termux-info")

# ----------------------------- #
# 5. File Search
# ----------------------------- #
def file_search():
    name = input("\nEnter filename: ")
    print("\nSearching...\n")
    os.system(f"find $HOME -iname '*{name}*' 2>/dev/null")

# ----------------------------- #
# 6. Wordlist Generator
# ----------------------------- #
def wordlist():
    word = input("\nBase word: ")
    count = int(input("How many? "))
    file = open("wordlist.txt", "w")
    for i in range(count):
        file.write(f"{word}{i}\n")
    file.close()
    print(GREEN + "\nWordlist saved as wordlist.txt" + RESET)

# ----------------------------- #
# 7. Password Strength Checker
# ----------------------------- #
def pass_strength():
    ps = input("\nEnter Password: ")
    strength = 0
    if len(ps) >= 8: strength += 1
    if any(c.isdigit() for c in ps): strength += 1
    if any(c.isalpha() for c in ps): strength += 1
    if any(c in "!@#$%^&*()_+" for c in ps): strength += 1

    levels = ["VERY WEAK", "WEAK", "MEDIUM", "STRONG"]
    print(GREEN + f"\nPassword Strength: {levels[strength]}\n" + RESET)

# ----------------------------- #
# 8. Website Status Checker
# ----------------------------- #
def web_status():
    url = input("\nEnter website URL: ")
    try:
        r = requests.get(url)
        print(GREEN + f"\nStatus: {r.status_code} (OK)\n" + RESET)
    except:
        print(RED + "\nWebsite unreachable!\n" + RESET)

# ----------------------------- #
# 9. Storage Usage
# ----------------------------- #
def storage():
    os.system("du -h ~ | tail")

# ----------------------------- #
# 10. Internet Speed Test
# ----------------------------- #
def speed_test():
    os.system("pip install speedtest-cli -q")
    os.system("speedtest-cli")

# ----------------------------- #
# 11. Hash Generator
# ----------------------------- #
def hash_generate():
    text = input("\nEnter text: ")
    print("\nMD5:", hashlib.md5(text.encode()).hexdigest())
    print("SHA256:", hashlib.sha256(text.encode()).hexdigest())

# ----------------------------- #
# 12. YouTube Info Grabber
# ----------------------------- #
def yt_info():
    os.system("pip install yt-dlp -q")
    url = input("\nEnter YouTube URL: ")
    os.system(f"yt-dlp --get-title --get-duration --get-description {url}")

# ----------------------------- #
# 13. Strong Password Generator
# ----------------------------- #
def strong_pass():
    import random, string
    length = int(input("\nPassword Length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+="
    password = "".join(random.choice(chars) for _ in range(length))
    print(GREEN + f"\nGenerated Password: {password}\n" + RESET)

# ----------------------------- #
# 14. URL Shortener
# ----------------------------- #
def url_shortener():
    long_url = input("\nEnter Long URL: ")
    try:
        api = f"http://tinyurl.com/api-create.php?url={long_url}"
        short = requests.get(api).text
        print(GREEN + f"\nShort URL: {short}\n" + RESET)
    except:
        print(RED + "\nFailed to shorten URL\n" + RESET)

# ----------------------------- #
# 15. Battery Status (Termux API)
# ----------------------------- #
def battery_status():
    os.system("termux-battery-status")

# ----------------------------- #
# 16. Send SMS (Your Phone)
# ----------------------------- #
def sms_sender():
    os.system("pkg install termux-api -y")
    number = input("\nEnter number: ")
    msg = input("Message: ")
    os.system(f"termux-sms-send -n {number} '{msg}'")
    print(GREEN + "\nSMS Sent!\n" + RESET)

# ----------------------------- #
# 17. Camera Snap
# ----------------------------- #
def camera_snap():
    os.system("termux-camera-photo ~/photo.jpg")
    print(GREEN + "\nSaved: ~/photo.jpg\n" + RESET)

# ----------------------------- #
# 18. Text to PDF
# ----------------------------- #
def text_to_pdf():
    os.system("pip install fpdf -q")
    from fpdf import FPDF
    text = input("\nWrite text for PDF: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output("output.pdf")
    print(GREEN + "\nPDF saved as output.pdf\n" + RESET)

# ----------------------------- #
# 19. Temp Mail
# ----------------------------- #
def temp_mail():
    try:
        domains = requests.get("https://api.mail.tm/domains").json()
        dom = domains["hydra:member"][0]["domain"]
        print(GREEN + f"\nTemp Mail Domain: @{dom}\n" + RESET)
    except:
        print(RED + "\nCould not fetch temporary email.\n" + RESET)

# ----------------------------- #
# 20. PDF to Text
# ----------------------------- #
def pdf_to_text():
    os.system("pip install PyPDF2 -q")
    from PyPDF2 import PdfReader
    file = input("\nPDF File Path: ")
    try:
        pdf = PdfReader(file)
        print("\nExtracted Text:\n")
        for page in pdf.pages:
            print(page.extract_text())
    except:
        print(RED + "\nError reading PDF!\n" + RESET)

# ----------------------------- #
# 21. Clipboard Tools
# ----------------------------- #
def clipboard_tools():
    os.system("pkg install termux-api -y")
    print("\n1. Copy to clipboard")
    print("2. Read clipboard")
    choice = input("\nChoose: ")
    if choice == "1":
        txt = input("Enter text: ")
        os.system(f"termux-clipboard-set '{txt}'")
    elif choice == "2":
        os.system("termux-clipboard-get")

# ----------------------------- #
# 22. Random MAC Generator
# ----------------------------- #
def mac_gen():
    import random
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    mac_addr = ':'.join(f"{x:02x}" for x in mac)
    print(GREEN + f"\nRandom MAC: {mac_addr}\n" + RESET)

# ----------------------------- #
# Main Menu
# ----------------------------- #
def menu():
    while True:
        clear()
        banner()
        print(f"""
{CYAN}==============================
      Lucifer Tools Menu
=============================={RESET}
1. Network Scanner
2. IP Info Lookup
3. Port Scanner
4. System Info
5. File Search
6. Wordlist Generator
7. Password Strength Check
8. Website Status Check
9. Storage Usage
10. Internet Speed Test
11. Hash Generator
12. YouTube Video Info
13. Strong Password Generator
14. URL Shortener
15. Battery Status
16. Send SMS
17. Camera Capture
18. Text → PDF
19. Temp Mail Generator
20. PDF → Text
21. Clipboard Tools
22. Random MAC Generator
0. Exit
""")

        choice = input("Choose Option: ")

        if choice == "1": arp_scan()
        elif choice == "2": ip_lookup()
        elif choice == "3": port_scan()
        elif choice == "4": system_info()
        elif choice == "5": file_search()
        elif choice == "6": wordlist()
        elif choice == "7": pass_strength()
        elif choice == "8": web_status()
        elif choice == "9": storage()
        elif choice == "10": speed_test()
        elif choice == "11": hash_generate()
        elif choice == "12": yt_info()
        elif choice == "13": strong_pass()
        elif choice == "14": url_shortener()
        elif choice == "15": battery_status()
        elif choice == "16": sms_sender()
        elif choice == "17": camera_snap()
        elif choice == "18": text_to_pdf()
        elif choice == "19": temp_mail()
        elif choice == "20": pdf_to_text()
        elif choice == "21": clipboard_tools()
        elif choice == "22": mac_gen()
        elif choice == "0":
            clear()
            print("Goodbye Lucifer!")
            sys.exit()
        else:
            print(RED + "Invalid Option!" + RESET)

        input("\nPress Enter to return menu...")

menu()
