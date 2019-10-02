#!/bin/python3
import socket
import time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2345))
    s.listen(5)
    while True:
        client_socket, address = s.accept()
        print(f"Connection from {address} has been established!")
        client_socket.send(bytes("Welcome!", "utf-8"))


if __name__ == '__main__':
    main()
