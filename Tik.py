import requests
from json.decoder import JSONDecodeError
import random
import string
import colorama
from colorama import Fore

colorama.init()

def generate_random_username(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def check_usernames(usernames):
    available_usernames = []
    taken_usernames = []

    for username in usernames:
        try:
            url = f"https://www.tiktok.com/@{username}"
            response = requests.get(url)

            if response.status_code == 200:
                taken_usernames.append(username)
            else:
                available_usernames.append(username)
        except Exception as e:
            print(f"An error occurred while checking {username}: {str(e)}")

    return available_usernames, taken_usernames


def main_menu() -> list:
    print("Welcome to TikTok username created by 3nTr, insta&twitter @4qd")
    flag = False
    while flag is False:
        try:
            num_usernames = int(input("How many letters in the username?  >")) # username
            username = int(input("How many random usernames do you want to check? >")) # num_usernames
            flag = True
        except ValueError:
            print("Please enter a length of the letters and how many times as a whole number\n\
                  Example: 2 for 2 letter usernames, 100 if you want to check 100 random usernames")

    available_usernames = []
    taken_usernames = []


    for _ in range(username):
        username = generate_random_username(num_usernames)
        available, taken = check_usernames([username])
        if available:
            available_usernames.extend(available)
        else:
            taken_usernames.extend(taken)

    print("Available usernames:")
    for username in available_usernames:
        print(Fore.GREEN + username + Fore.RESET)

    print("\nTaken usernames:")
    for username in taken_usernames:
        print(Fore.RED + username + Fore.RESET)

if __name__ == '__main__':
    main_menu()
