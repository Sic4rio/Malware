import time
import sys
import re
import concurrent.futures
import requests
import os
from colorama import Fore

os.system('cls' if os.name == 'nt' else 'clear')
requests.urllib3.disable_warnings()

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

banner = '''
 \u001b[36m
	    _______  ______     ____  ____  ______
	   / ____/ |/ / __ \   / __ )/ __ \/_  __/
	  / /    |   / /_/ /  / __  / / / / / /
	 / /___ /   |\__, /  / /_/ / /_/ / / /
	 \____//_/|_/____/  /_____/\____/ /_/
                      Wp Scanner
  \u001b[32mDEVELOPED BY TEAM BADS and CRACKED BY SICARIO! ᕦ(ò_óˇ)ᕤ\033[0m
'''

def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)

def URLdomain(site):
    if site.startswith("www."):
        site = site.replace("www.", "")
    return site

def exploit(url):
    try:
        session = requests.Session()
        session.headers.update(headers)
        response = session.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            if 'wp-content' in response.text:
                print(Fore.GREEN + '[+] VULNERABLE: ' + url)
                with open('exploit.txt', 'a') as f:
                    f.write(url + '\n')
    except Exception as e:
        pass

def main():
    print(banner)
    print()
    animated(Fore.YELLOW + '[*] Loading Scanner...')

    url_input = input("Enter the URL or the name of the file containing URLs: ")

    if os.path.isfile(url_input):
        with open(url_input, 'r') as file:
            urls = file.read().splitlines()
    else:
        urls = [url_input]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(exploit, urls)

    print(Fore.CYAN + '\n[+] Scan Complete!')

if __name__ == "__main__":
    main()

