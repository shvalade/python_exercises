
import multiprocessing
import time
import sys


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)


class Testing(multiprocessing.Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        #x = int(input('Enter Number: '))
        while True:
            pass
            print('Hello')
            time.sleep(self.interval)


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    n = Testing(2)
    n.start()
    x = input('type :')
    print(x*3)
    #print('Hello')


#
#
# import time
# from multiprocessing import Process
#
# class TestClass():
#     def test_f(self):
#         ctr = 0
#         while True:
#             ctr += 1
#             print("     ", ctr)
#             time.sleep(1.0)
#
# if __name__ == '__main__':
#      ## run function in the background
#      CT=TestClass()
#      p = Process(target=CT.test_f)
#      p.start()
#
#      ## will not exit if function finishes, only when
#      ## "q" is entered, but this is just a simple example
#      stop_char=""
#      while stop_char.lower() != "q":
#          stop_char = input("Enter 'q' to quit ")
#          if stop_char.lower() == "u":
#              print('>')
#              ## do something else
#      print("terminate process")
#      if p.is_alive():
#          p.terminate()
#
#