import dns.resolver
import requests
import json
from colorama import Fore, Style,init
import argparse
import pyfiglet
import argparse
import sys

init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("GhostDomain")  # Or your chosen name
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "Subdomain Takeover Scanner")
    print(Fore.GREEN + "Version: 1.0.0 by GhostDomain 🔥\n")
    print(Style.RESET_ALL)
    

def load_subdomains(file=None):
    if file:
        with open(file, "r") as f:
            return [line.strip() for line in f if line.strip()]
    else:
        with open("common_subs.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]

        
def resolve_subdomain(sub, domain):
    full = f"{sub}.{domain}"
    try:
        answers = dns.resolver.resolve(full, "CNAME")
        return str(answers[0].target)
    except Exception:
        return None


with open("fingerprints.json", "r") as f:
    fingerprints = json.load(f)

def check_takeover(subdomain, fingerprints):
    url = f"http://{subdomain}"
    try:
        resp = requests.get(url, timeout=5)
        status_code = resp.status_code
        body = resp.text.lower()

        for service, signature in fingerprints.items():
            if service in subdomain and signature.lower() in body:
                return True, status_code, signature
        return False, status_code, ""
    except requests.exceptions.RequestException:
        return False, "No Response", ""
    
    


def main(domain, wordlist=None):
    print_banner()

    subdomains = load_subdomains(wordlist)
    with open("fingerprints.json", "r", encoding="utf-8") as f:
        fingerprints = json.load(f)

    for sub in subdomains:
        full_sub = f"{sub}.{domain}"
        cname = resolve_subdomain(sub, domain)
        if cname:
            vulnerable, status, message = check_takeover(full_sub, fingerprints)
            if vulnerable:
                print(Fore.RED + f"[VULNERABLE] {full_sub} - Status: {status} - {message}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"[OK]        {full_sub} - Status: {status}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"[NXDOMAIN]  {full_sub} - No DNS Record" + Style.RESET_ALL)
                    


if __name__ == "__main__":
    
    try:
        
        parser = argparse.ArgumentParser(
            description="🛡️ GhostDomain - Subdomain Takeover Scanner",
            epilog="Example: python main.py -d example.com -w customlist.txt"
        )
    
        parser.add_argument(
            "-d", "--domain",
            help="Target domain (e.g. example.com)",
            required=True
        )

        parser.add_argument(
            "-w", "--wordlist",
            help="Custom wordlist file (default: common_subs.txt)",
            required=False
        )

        parser.add_argument(
            "-v", "--version",
            action="store_true",
            help="Show version and exit"
        )

        args = parser.parse_args()

        if args.version:
            print("🔎 GhostDomain v1.0.0 - by You 💻")
            sys.exit()

        main(args.domain, args.wordlist) 
        
    except KeyboardInterrupt:
        
        print("\n🛑 Scan interrupted by user (Ctrl+C). Exiting...")
        exit(0)
        