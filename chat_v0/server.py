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

        d = {1: "Hey", 2: "There"}
        msg = pickle.dumps(d)
        #print(msg)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

        client_socket.send(msg)

    #     while 1:
    #         time.sleep(3)
    #         msg = f"The time is:  {time.time()}"
    #         msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #         client_socket.send(bytes(msg, "utf-8"))


if __name__ == '__main__':
    main()
