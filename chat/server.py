#!/bin/python3
import socket
import time
import pickle
def main():

    HEADERSIZE = 10

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1235))
    s.listen()
    while 1:
        client_socket, address = s.accept()
        print(f"Connection from {address} has been established!")

        msg = "Welcome to the server!"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg

        client_socket.send(bytes(msg, "utf-8"))

    #     while 1:
    #         time.sleep(3)
    #         msg = f"The time is:  {time.time()}"
    #         msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #         client_socket.send(bytes(msg, "utf-8"))


if __name__ == '__main__':
    main()
