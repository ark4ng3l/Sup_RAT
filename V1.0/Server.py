import pyfiglet
import colorama
import subprocess
import os
import requests


banner = pyfiglet.figlet_format('sup _ RAT')
print (colorama.Fore.CYAN + banner)


menu_item_choise_1=['1','2']

menu_items1='''
[1] Active Mode
[2] Passive Mode
'''
print (colorama.Fore.YELLOW + menu_items1)

user_input = input(colorama.Fore.GREEN + "select a number: " + colorama.Fore.RESET)
if user_input == '1':
    pass
elif user_input =='2':
    
    menu_item_choise_2=['1','2','3','4','5','6']
    menu_items_2='''
    [1] View system information
    [2] Get path to creat X folders
    [3] Get command and show output
    [4] Get program name and kill
    [5] Get site name and list virtual directory
    [6] exit
    '''
    os.system('cls')
    print (colorama.Fore.CYAN + banner)
    print (colorama.Fore.RED + 'PAssive OPTIONs: ')
    print (colorama.Fore.YELLOW + menu_items_2)

    user_input_2 = input(colorama.Fore.GREEN + "select a number: " + colorama.Fore.RESET)
    
    while user_input_2 not in menu_items_2:
        os.system('cls')
        print (colorama.Fore.CYAN + banner)
        print (colorama.Fore.RED + 'Hi, I Can Do: ')
        print (colorama.Fore.YELLOW + menu_items_2)
        user_input_2 = input(colorama.Fore.GREEN + "select a number: " + colorama.Fore.RESET)
        
    if user_input_2 == '1':
        print (subprocess.getoutput('systeminfo'))
    elif user_input_2 == '2':
        user_directory=input("Enter your directory to creat 100 folder: ")
        os.chdir(user_directory)
        for i in range(user_x):
            os.mkdir(f"new folder {i}")
    elif user_input_2 == '3':
        command = input("Enter your command: ")
        output_command = subprocess.check_output(command,shell=True).decode().split()
        print(output_command)
    elif user_input_2 == '4':
        program_name = input('Enter name of pragram to kill it: ')
        os.system(f" taskkill /f /im {program_name}*")
    elif user_input_2 == '5':
        site_name = input("enter site name: ")
        if 'www' not in site_name:
            site_name = 'www.' + site_name
        if 'http://' not in site_name:
            site_name = 'http://' + site_name
        common = ['index.html' , 'robots.txt' , 'owa' , 'wp-admin']
        found = []
        for j in common:
            r=requests.get(site_name + '/' + j)
            if r.status_code == 200:
                found.append(j)
        print(found)
    elif user_input_2 == '6':
        print( 'Nice To Meet You :)')
        exit()