from PySide2.QtCore import QObject, Signal
import queue
import struct


class SerialUpSignals(QObject):
    update_raw_data = Signal(str)

    update_ascii_data1 = Signal(str)
    update_ascii_data2 = Signal(str)
    update_ascii_data3 = Signal(str)
    update_ascii_data4 = Signal(str)


globle_ser_signal = SerialUpSignals()

# 定义ascii数据存储队列，最长50
rcv_ascii_queue = queue.Queue(50)
# 定义hex数据存储队列，长度固定
rcv_hex_queue = queue.Queue(50)


def ascii_process(data):
    list_data = data.split(',')
    # print(list_data)
    globle_ser_signal.update_raw_data.emit(data)
    globle_ser_signal.update_ascii_data1.emit(list_data[0])
    globle_ser_signal.update_ascii_data2.emit(list_data[1])
    globle_ser_signal.update_ascii_data3.emit(list_data[2])
    globle_ser_signal.update_ascii_data4.emit(list_data[3])


# 使用struct.unpack将bytes格式解包成常规数据, “<”为小端模式, H为2字节，I为4字节，大写为无符号，小写为带符号
# unpack解包后格式为 ‘xxx,’ 需要转字符串将前后引号以及后面逗号去除，再转整型计算，最后转字符串输出

def hex_process(data):
    data_str = ''
    data_dec = 0
    for x in data:
        # data_hex_list.append(x.hex())
        data_str = data_str + str(x.hex()) + ' '
    globle_ser_signal.update_raw_data.emit(data_str)
    data_byte = data[2] + data[3]
    # print(data_byte)
    # print(str(struct.unpack('>H', data_byte)))
    globle_ser_signal.update_ascii_data1.emit(str(struct.unpack('>H', data_byte))[1:-2])

    data_byte = data[4] + data[5]
    # print(data_byte)
    # print(str(struct.unpack('>H', data_byte)))
    globle_ser_signal.update_ascii_data2.emit(str(struct.unpack('>H', data_byte))[1:-2])

    data_byte = data[6] + data[7]
    # print(data_byte)
    # print(str(struct.unpack('<H', data_byte)))
    globle_ser_signal.update_ascii_data3.emit(str(struct.unpack('<H', data_byte))[1:-2])

    data_byte = data[8] + data[9]
    # print(data_byte)
    # print(str(struct.unpack('<H', data_byte)))
    globle_ser_signal.update_ascii_data4.emit(str(struct.unpack('<H', data_byte))[1:-2])
    # data_dec = int(str(struct.unpack('>H', data[2:3])))
    # print(data_dec)
