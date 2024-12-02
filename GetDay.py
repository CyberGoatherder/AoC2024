### Script to automate the creation of a new day's folder and pull the necessary files from the AoC website.

import os
import requests
from bs4 import BeautifulSoup
import sys

def create_daily_folder(day):
    folder_name = f"Day{day}"
    if os.path.exists(folder_name):
        print("\n\033[91m[!] Folder already exists, did you enter the correct day?\033[0m\n")
        sys.exit(1)
    else:
        os.makedirs(folder_name)
        print("\n[+] Subfolder Created: " + str(folder_name))
    return folder_name

def get_session_cookie():
    try:
        with open('session.txt', 'r') as f:
            print("[+] Session Cookie Retrieved")
            return f.read().strip()
    except FileNotFoundError:
        print("Please create a session.txt file with your session cookie")
        sys.exit(1)

def save_problem_description(day, folder):
    url = f"https://adventofcode.com/2024/day/{day}"
    session = get_session_cookie()
    
    response = requests.get(url, cookies={'session': session})
    if response.status_code != 200:
        print(f"Failed to get problem description. Status code: {response.status_code}")
        return
    else:
        print("[+] Problem Description Retrieved")

    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find('main')
    
    if main_content:
        with open(f"{folder}/info.txt", 'w', encoding='utf-8') as f:
            f.write(main_content.get_text())

def save_input_data(day, folder):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    session = get_session_cookie()
    
    response = requests.get(url, cookies={'session': session})
    if response.status_code != 200:
        print(f"Failed to get input data. Status code: {response.status_code}")
        return
    else:
        print("[+] Input Data Retrieved")

    with open(f"{folder}/input.txt", 'w') as f:
        f.write(response.text)

def create_solution_template(folder):
    template = '''
# Setup the input lists
with open("input.txt") as file:
    lines = file.readlines()

# Do stuff here

print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")
'''
    with open(f"{folder}/part1.py", 'w') as f:
        f.write(template)
    print("[+] Part1.py Template File Created")

def main():
    day = input("\nWhich Day? ")
    folder = create_daily_folder(day)
    save_problem_description(day, folder)
    save_input_data(day, folder)
    create_solution_template(folder)
    print(f"\n\033[92m[+] Successfully created Day{day} subfolder with all necessary files\033[0m\n")

if __name__ == "__main__":
    main() 