#!/bin/python3
import socket


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 2345))




if __name__ == '__main__':
    main()