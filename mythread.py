import serial
import threading
import time
import dataprocess


class CustomException(Exception):
    # 自定义异常类，继承自Exception
    pass


data_list = []


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
        # while self.is_alive() is True:
        #     pass
        try:
            self.ser.close()
        except serial.SerialException as e:
            print('关闭失败', str(e))
            raise CustomException(e)

    # ascii字符串接收解析
    # def run(self):
    #     while self.thread_event.is_set() is False:
    #         rcv_data = self.ser.readline().decode().strip()
    #         # 设定长度大于4个字符段处理数据
    #         if len(rcv_data.split(',')) >= 4:
    #             dataprocess.ascii_process(rcv_data)
    #         # print('线程正在运行')
    #         # time.sleep(0.5)
    #         print('thread_event状态：' + str(self.thread_event.is_set()))

    # HEX数据接收解析
    def run(self):
        while self.thread_event.is_set() is False:
            # dataprocess.rcv_hex_queue.put(self.ser.read())

            # data_list.append(dataprocess.rcv_hex_queue.get_nowait())
            data_list.append(self.ser.read(1))
            if data_list[0] == b'\xAB' and len(data_list) <= 11:
                if len(data_list) == 11 and data_list[1] == b'\xCD' and data_list[-1] == b'\xDF':
                    dataprocess.hex_process(data_list)
                    data_list.clear()
            else:
                data_list.clear()
                print(data_list)


