from ipmp.emu.neo import NeoPanel
from ipmp.pages.rest.api import GuiApi
import logging
import threading
import multiprocessing
import time


class Running(multiprocessing.Process):
    def __init__(self, panel):
        super().__init__()
        self.panel = panel

    def run(self):
        self.panel.connectITv2()



def main():
    n = '%X' % (1 + 0xBA0008400005)
    print(n)
    log = logging.basicConfig(level='DEBUG')

    api = GuiApi('94.125.123.42', log)
    panel = NeoPanel(n, n[2:], 'IP', log, 'HS3248')
    panel.config.host = '94.125.123.42'
    panel.add_device('Contact', 54)
    panel.set_device_alarm('tamper', 2, 54)
    panel.set_device_trouble('tamper', 1, 54)
    # panel.send_trouble_notification('tamper', 2, 54)
    proc = Running(panel)
    proc.start()



    #print(panel.logger())

    #time.sleep(20)

    #panel.sendInit()
    # panel.add_device()
    #panel.connectITv2()
    # time.sleep(15)
    # proc.terminate()
    # panel.sendInit()
    # panel.sendHeartBeat()
    pass


if __name__ == '__main__':
    main()
