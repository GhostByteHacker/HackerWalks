import os
import subprocess
import sys
from colorama import init, Fore, Style
import logging

init(autoreset=True)

# Configure logging
logging.basicConfig(filename='hackerwalks.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def display_ascii_art():
    art = f"""{Fore.BLUE}
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

def print_info(message):
    print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")

def run_command(command):
    """Run a system command safely."""
    try:
        print_info(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
        logging.info(f"Command succeeded: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        print_error(f"An error occurred: {e}")
        logging.error(f"Command failed: {' '.join(command)} - {e}")

def run_nmap_command():
    intensity_options = {
        "1": "-sn",
        "2": "-sV",
        "3": "-A"
    }

    while True:
        print(f"{Fore.YELLOW}\nChoose the intensity level for the Nmap scan:{Style.RESET_ALL}")
        print("1. Basic ping scan")
        print("2. Regular scan (service and version detection)")
        print("3. Aggressive scan")
        print("4. Back")

        intensity_level = input(f"{Fore.GREEN}Enter the scan intensity level (1-4): {Style.RESET_ALL}")

        if intensity_level == "4":
            return

        if intensity_level not in intensity_options:
            print_error("Invalid intensity level. Please select a number between 1 and 4.")
            continue

        target = input(f"{Fore.GREEN}Enter the target IP address or domain to scan: {Style.RESET_ALL}")
        if not target:
            print_error("Target cannot be empty.")
            continue

        command = ["nmap", intensity_options[intensity_level], target]
        run_command(command)

def run_theharvester():
    print(f"{Fore.YELLOW}Configure the options for theHarvester scan:{Style.RESET_ALL}")

    domain = input("Please enter the domain to search (e.g., example.com): ")
    if not domain:
        print_error("Domain cannot be empty.")
        return

    limit = input("Please enter the result limit (number of results to retrieve): ")
    if not limit.isdigit():
        print_error("Limit must be a number.")
        return

    search_engine = input("Enter the search engine to use (e.g., bing, yahoo): ")
    if not search_engine:
        print_error("Search engine cannot be empty.")
        return

    print("\nYou have chosen the following options:")
    print(f"Domain: {domain}")
    print(f"Limit: {limit}")
    print(f"Search Engine: {search_engine}")

    confirmation = input("Do you want to proceed with this command? (y/n): ")

    if confirmation.lower() == 'y':
        command = ["theHarvester", "-d", domain, "-l", limit, "-b", search_engine]
        run_command(command)
    else:
        print_warning("Operation canceled by the user.")

def run_whois():
    target = input(f"{Fore.GREEN}Enter the domain or IP address for WHOIS lookup: {Style.RESET_ALL}")
    if not target:
        print_error("Target cannot be empty.")
        return

    command = ["whois", target]
    run_command(command)

def run_dig():
    target = input(f"{Fore.GREEN}Enter the domain for DNS lookup: {Style.RESET_ALL}")
    if not target:
        print_error("Target cannot be empty.")
        return

    command = ["dig", target]
    run_command(command)

def choose_information_gathering_tools():
    tools = {
        "1": ("Nmap", run_nmap_command),
        "2": ("theHarvester", run_theharvester),
        "3": ("WHOIS Lookup", run_whois),
        "4": ("DNS Lookup (dig)", run_dig),
        "5": ("Back to main menu", None)
    }

    while True:
        print(f"{Fore.YELLOW}\nChoose an information gathering tool:{Style.RESET_ALL}")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")

        option = input(f"{Fore.GREEN}Enter the tool you would like to use (1-5): {Style.RESET_ALL}")

        if option == "5":
            return
        elif option in tools:
            tools[option][1]()
        else:
            print_error("Invalid option. Please try again.")

def main_menu():
    while True:
        print(f"{Fore.BLUE}\nMain Menu:{Style.RESET_ALL}")
        print("1. Information Gathering")
        print("2. Exit")

        choice = input(f"{Fore.GREEN}Select an option (1-2): {Style.RESET_ALL}")

        if choice == "1":
            choose_information_gathering_tools()
        elif choice == "2":
            print_warning("Exiting HackerWalks. Goodbye!")
            sys.exit()
        else:
            print_error("Invalid option. Please try again.")

if __name__ == "__main__":
    display_ascii_art()
    main_menu()
