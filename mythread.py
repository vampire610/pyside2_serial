import serial
import threading
import time


class CustomException(Exception):
    # 自定义异常类，继承自Exception
    pass


class MySerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = None
        self.thread_event = threading.Event()

    def open_ser(self, comx, baud):
        try:
            self.ser = serial.Serial(port=comx, baudrate=baud)
            print('打开')
            self.thread_event.clear()
            self.start()

            # return 0
        except serial.SerialException as e:
            print('打开失败', e)
            raise CustomException(e)
            # return -1

    def close_ser(self):
        self.thread_event.set()
        while self.is_alive() is True:
            pass
        try:
            self.ser.close()
        except serial.SerialException as e:
            print('关闭失败', str(e))
            raise CustomException(e)

    def run(self):
        while self.thread_event.is_set() is False:
            print('线程正在运行')
            time.sleep(0.5)
            print('thread_event状态：' + str(self.thread_event.is_set()))
