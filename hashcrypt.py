from colorama import Fore, init, Style
import hashlib
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def deshash_salt():
    bruteforce_file = input("Wordlist name: ")
    hash_input = input("Enter a Hash: ")
    salt = input("Enter a Salt: ")

    with open(f'{bruteforce_file}', 'r', encoding='latin-1') as wordlist:
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Wordlist loaded")

        if len(hash_input) == 32:
            type = "MD5"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.md5((word + salt).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 40:
            type = "SHA-1"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha1((word + salt).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 64:
            type = "SHA-256"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha256((word + salt).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 128:
            type = "SHA-512"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha512((word + salt).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        else:
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Type of hash unknown")



def deshash_without_salt():
    bruteforce_file = input("Wordlist name: ")
    hash_input = input("Enter a hash: ")
    with open(f'{bruteforce_file}', 'r', encoding='latin-1') as wordlist:
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Wordlist loaded")
        if len(hash_input) == 32:
            type = "MD5"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.md5((word).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 40:
            type = "SHA-1"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha1((word).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 64:
            type = "SHA-256"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha256((word).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        elif len(hash_input) == 128:
            type = "SHA-512"
            found = False
            print(f"{Fore.YELLOW}[{Fore.RESET}+{Fore.YELLOW}]{Fore.RESET} Type of hash: {type}")

            for word in wordlist:
                word = word.strip()
                hash_attempt = hashlib.sha512((word).encode()).hexdigest()

                if hash_attempt == hash_input:
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} The password has been decrypted: {word}")
                    found = True
                    
                    break
            if not found:
                print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} The password cant be decrypted, try with other wordlist")
        else:
            print(f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Type of hash unknown")

def main_menu():
    clear_screen()
    print(f"""
{Fore.BLUE}
██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
███████║███████║███████╗███████║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║   ██║   ██║        ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   
by alekszdev.
{Fore.RESET}""")
    print(f"{Fore.CYAN}[{Fore.RESET}1{Fore.CYAN}]{Fore.RESET} HASH AND SALT.")
    print(f"{Fore.CYAN}[{Fore.RESET}2{Fore.CYAN}]{Fore.RESET} ONLY HASH.")
    option_1 = int(input("> "))
    if option_1==1:
        deshash_salt()
    elif option_1==2:
        deshash_without_salt()
main_menu()
