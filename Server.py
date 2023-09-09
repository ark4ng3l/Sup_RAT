import pyfiglet
import os 
import requests
import colorama
import subprocess
import platform
from cryptography.fernet import Fernet
import sys
import socket
import winreg as wrg
from tkinter import *
from scapy.all import *
import whois
from tkinter import messagebox

banner = pyfiglet.figlet_format('netcat')
print (colorama.Fore.CYAN + banner)
print (colorama.Fore.RED + 'Hi, I Can Do: ')

menu_item_choise=['1','2','3','4','5','6']

menu_items='''
[1] View system information
[2] Get path to creat 100 folders
[3] Get command and show output
[4] Get program name and kill
[5] Get site name and list virtual directory
[6] exit
'''
print (colorama.Fore.YELLOW + menu_items)

user_input = input(colorama.Fore.GREEN + "select a number: " + colorama.Fore.RESET)

while user_input not in menu_item_choise:
    print (colorama.Fore.CYAN + banner)
    print (colorama.Fore.RED + 'Hi, I Can Do: ')
    print (colorama.Fore.YELLOW + menu_items)
    user_input = input(colorama.Fore.GREEN + "select a number: " + colorama.Fore.RESET)
if user_input == '1':
    print (os.uname_result)
elif user_input == '2':
    user_directory=input("Enter your directory to creat 100 folder: ")
    os.chdir(user_directory)
    for i in range(100):
        os.mkdir(f"new folder {i}")
elif user_input == '3':
    command = input("Enter your command: ")
    output_command = subprocess.check_output(command,shell=True).decode().split()
    print(output_command)
elif user_input == '4':
    program_name = input('Enter name of pragram to kill it: ')
    os.system(f" taskkill /f /im {program_name}*")
elif user_input == '5':
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
elif user_input == '6':
    print( 'Nice To Meet You :)')
    exit()
