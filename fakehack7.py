#!/usr/bin/env python3
# Dynamic Fake Hacking Demo with Matrix Rain + Alerts + Beeps + Brute Force + Data Exfiltration + Access Banner — 100% safe

import os
import random
import time
import sys
import shutil
import string
from datetime import datetime

# ANSI colors
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
red = "\033[31m"
bold = "\033[1m"
reset = "\033[0m"

def rand_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def rand_password(length=6):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

def progress(n=30, speed=0.05):
    sys.stdout.write("[")
    sys.stdout.flush()
    for _ in range(n):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(random.uniform(speed/2, speed*1.5))
    sys.stdout.write("]\n")
    sys.stdout.flush()

def fake_log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{yellow}[{now}]{reset} {msg}")

def simulate_scan():
    for _ in range(random.randint(10, 25)):
        ip = rand_ip()
        print(f"{blue}[*] Probing {ip}...{reset}")
        time.sleep(random.uniform(0.03, 0.12))

def matrix_rain(duration=2):
    cols, _ = shutil.get_terminal_size((80, 20))
    chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(cols))
        print(f"{green}{line}{reset}")
        time.sleep(0.05)

def alert_screen():
    cols, _ = shutil.get_terminal_size((80, 20))
    message = random.choice([
        "!!! THREAT DETECTED !!!",
        "!!! BREACH CONFIRMED !!!",
        "!!! UNAUTHORIZED ACCESS !!!",
        "!!! SYSTEM COMPROMISED !!!"
    ])
    box = f" {message} "
    padding = (cols - len(box)) // 2
    for _ in range(6):
        print("\n" * 2)
        print(" " * padding + f"{red}{bold}{box}{reset}\a")
        print("\n" * 2)
        sys.stdout.flush()
        time.sleep(0.3)
        os.system("clear" if os.name != "nt" else "cls")

def brute_force(interactive=False):
    users = ["admin", "root", "guest", "sys", "oracle", "postgres"]
    target = random.choice(users)
    fake_log(f"Attempting brute force login on user '{target}'")
    if interactive:
        attempts = random.randint(5, 10)
        for i in range(attempts - 1):
            guess = input(f"{blue}[{i+1:03d}] Enter password for {target}: {reset}")
            print(f"{red}[-] WRONG: {target}:{guess}{reset}")
            time.sleep(random.uniform(0.2, 0.5))
        final_pw = rand_password(8)
        guess = input(f"{blue}[{attempts:03d}] Enter password for {target}: {reset}")
        print(f"{green}[+] SUCCESS: {target}:{final_pw}{reset}")
        time.sleep(1)
    else:
        attempts = random.randint(15, 30)
        for i in range(attempts):
            pw = rand_password(random.randint(6, 10))
            print(f"{blue}[{i+1:03d}] {target}:{pw}{reset}")
            time.sleep(random.uniform(0.02, 0.06))
        print(f"{green}[+] SUCCESS: {target}:{rand_password(8)}{reset}")

def data_exfiltration():
    files = [
        "payroll_2025.xlsx",
        "secrets.db",
        "customers.csv",
        "contracts.pdf",
        "emails.mbox",
        "vault.key",
        "transactions.log"
    ]
    fake_log("Starting data exfiltration...")
    for f in random.sample(files, random.randint(3, 5)):
        size = random.randint(20, 200)
        print(f"{blue}Downloading {f} ({size} MB){reset}")
        progress(n=30, speed=random.uniform(0.03, 0.08))
        time.sleep(0.2)
    print(f"{green}[+] Exfiltration complete. Files saved to /tmp/exfiltrated/{reset}")

def access_granted_banner():
    """Big green ACCESS GRANTED banner with flicker effect"""
    banner = r"""
      █████╗  ██████╗ ██████╗ ███████╗███████╗███████╗     ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗███████╗██████╗ 
     ██╔══██╗██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
     ███████║██║  ███╗██║  ██║█████╗  ███████╗█████╗      ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██████╔╝
     ██╔══██║██║   ██║██║  ██║██╔══╝  ╚════██║██╔══╝      ██║   ██║██╔═══╝ ██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
     ██║  ██║╚██████╔╝██████╔╝███████╗███████║███████╗    ╚██████╔╝██║     ██║  ██║██║ ╚████║   ██║   ███████╗██║  ██║
     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝     ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
    for _ in range(3):  # flicker effect
        os.system("clear" if os.name != "nt" else "cls")
        if random.choice([True, False]):
            print(f"{green}{banner}{reset}")
        time.sleep(0.3)
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{green}{banner}{reset}")
    time.sleep(2)

def main(endless=False, interactive=False):
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{green}=== Termux Fake Hack Screen (Full Hollywood Mode) ==={reset}")

    startup_msgs = [
        "Initializing modules...",
        "Loading wordlists",
        "Bootstrapping exploit packs",
        "Syncing with control server",
        "Gathering threat intel feeds"
    ]
    fake_log(random.choice(startup_msgs))
    time.sleep(random.uniform(0.2, 0.6))

    fake_log("Loading wordlists")
    progress(random.randint(15, 30))

    fake_log("Starting sweep across subnets")
    simulate_scan()
    matrix_rain(duration=2)

    brute_force(interactive=interactive)
    matrix_rain(duration=2)

    data_exfiltration()
    matrix_rain(duration=2)

    ports = [21, 22, 25, 53, 80, 110, 135, 139, 443, 445, 8080, 3306, 5432, 6379]
    for _ in range(random.randint(3, 6)):
        port = random.choice(ports)
        fake_log(f"Checking port {port} on {rand_ip()}")
        time.sleep(random.uniform(0.05, 0.15))
    matrix_rain(duration=3)

    fake_log("Running cipher checks (mock)")
    alert_triggered = False
    for _ in range(random.randint(20, 40)):
        event_id = random.randint(1000, 9999)
        session = f"{random.randint(0, 65535):04X}"
        status = random.choice(["OK", "WARN", "TIMEOUT", "DENIED"])
        fake_log(f"EventID={event_id} Session={session} Status={status}")
        time.sleep(random.uniform(0.02, 0.08))
        if not alert_triggered and random.random() < 0.15:
            alert_screen()
            alert_triggered = True
        elif random.random() < 0.05:
            matrix_rain(duration=random.uniform(1, 2))
    if not alert_triggered:
        alert_screen()

    print()
    access_granted_banner()
    print(f"{green}[+] Demo complete. Just for fun.{reset}")

    if endless:
        time.sleep(1)
        main(endless=True, interactive=interactive)

if __name__ == "__main__":
    endless = "--loop" in sys.argv
    interactive = "--interactive" in sys.argv
    try:
        main(endless=endless, interactive=interactive)
    except KeyboardInterrupt:
        print(f"\n{green}[+] Exiting fake hack demo. Bye!{reset}")
