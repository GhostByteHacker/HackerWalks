import os
import subprocess
from colorama import init, Fore, Style

init()

def display_ascii_art():
    art = f"""
{Fore.BLUE}
 /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$  /$$      /$$  /$$$$$$  /$$       /$$   /$$  /$$$$$$ 
| $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/| $$_____/| $$__  $$| $$  /$ | $$ /$$__  $$| $$      | $$  /$$/ /$$__  $$
| $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$      | $$  \ $$| $$ /$$$| $$| $$  \ $$| $$      | $$ /$$/ | $$  \__/
| $$$$$$$$| $$$$$$$$| $$      | $$$$$/  | $$$$$   | $$$$$$$/| $$/$$ $$ $$| $$$$$$$$| $$      | $$$$$/  |  $$$$$$ 
| $$__  $$| $$__  $$| $$      | $$  $$  | $$__/   | $$__  $$| $$$$_  $$$$| $$__  $$| $$      | $$  $$   \____  $$
| $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  \ $$| $$$/ \  $$$| $$  | $$| $$      | $$\  $$  /$$  \ $$
| $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$  | $$| $$/   \  $$| $$  | $$| $$$$$$$$| $$ \  $$|  $$$$$$/
|__/  |__/|__/  |__/ \______/ |__/  \__/|________/|__/  |__/|__/     \__/|__/  |__/|________/|__/  \__/ \______/

 [HackerWalks v2.2]
 [Author: GhostByteHacker]
{Style.RESET_ALL}
    """
    print(art)

def run_nmap_command(intensity_level, target):
    if intensity_level == "1":
        command = ["nmap", "-sn", target]
    elif intensity_level == "2":
        command = ["nmap", "-sV", target]
    elif intensity_level == "3":
        command = ["nmap", "-A", target]
    else:
        print(Fore.RED + "Invalid intensity level. Please select a number between 1 and 3." + Style.RESET_ALL)
        return

    print(Fore.CYAN + f"Running command: {' '.join(command)}" + Style.RESET_ALL)
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    
def choose_information_gathering_tools():
    while True:
        print(Fore.YELLOW + "\nChoose an information gathering tool:" + Style.RESET_ALL)
        print("1. Nmap")
        print("2. theHavester")
        print("3. Back to main menu")

        option = input(Fore.GREEN + "Enter the tool you would like to use (1-3): " + Style.RESET_ALL)

        if option == "1":
            choose_nmap_intensity()
        elif option == "2":
            config_theHarvester()
        elif option == "3":
            return
        else:
            print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)

def choose_nmap_intensity():
    while True:
        print(Fore.YELLOW + "\nChoose the intensity level for the Nmap scan:" + Style.RESET_ALL)
        print("1. Basic ping scan")
        print("2. Regular scan (service and version detection)")
        print("3. Aggressive scan")
        print("4. Back")
        
        intensity_level = input(Fore.GREEN + "Enter the scan intensity level (1-4): " + Style.RESET_ALL)
        
        if intensity_level == "4":
            return

        target = input(Fore.GREEN + "Enter the target IP address or domain to scan: " + Style.RESET_ALL)
        run_nmap_command(intensity_level, target)

def config_theHarvester():
    print(Fore.YELLOW + "Configure and fillout the options for theHavester scan:" + Style.RESET_ALL)
    
    domain = input("Please enter the company name or domain to search (e.g., example, example.com): ")
    
    limit = input("Please enter the result limit (number of results to retrieve): ")
    
    print("Choose a search engine or service (e.g., bing, yahoo): ")
    search_engine = input("Enter your preference: ")

    print("\nYou have chosen the following options:")
    print(f"Domain: {domain}")
    print(f"Limit: {limit}")
    print(f"Place To Search: {search_engine}")

    confirmation = input("Do you want to proceed with this command? (y/n): ")
    
    if confirmation.lower() == 'y':
        command = f"theHarvester -d {domain} -l {limit} -b {search_engine}"
        print(f"\nRunning the command: {command}")
        os.system(command)  
    else:
        print(Fore.RED + "Operation canceled by the user." + Style.RESET_ALL)

def main_menu():
    while True:
        print(Fore.BLUE + "\nMain Menu:" + Style.RESET_ALL)
        print("1. Information Gathering")
        print("2. Exit")
        
        choice = input(Fore.GREEN + "Select an option (1-2): " + Style.RESET_ALL)
        
        if choice == "1":
            choose_information_gathering_tools()
        elif choice == "2":
            print(Fore.YELLOW + "Exiting HackerWalks. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    display_ascii_art()
    main_menu()
