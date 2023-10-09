import sys
import serial
import serial.tools.list_ports

import mythread

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QFileDialog

from Ui_pyside2_Main import Ui_Form_Main


# 创建主窗口类，继承自QWidget
class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 创建ui实例，来自ui文件的主窗口类
        self.ui = Ui_Form_Main()
        # 使用窗口设置
        self.ui.setupUi(self)
        # 创建串口线程空的类
        self.ser_thread = None
        # 创建串口信息的字典
        self.ser_dist = {}
        # 信号处理
        self.ui.pushButton_ser_open.clicked.connect(self.pushbutton_ser_open_clicked)
        self.ui.comboBox_ser_select.clicked.connect(self.combobox_ser_select_clicked)
        self.ui.comboBox_ser_select.currentIndexChanged.connect(self.combobox_ser_select_changed)

    # 串口选择combobox点击槽函数
    def combobox_ser_select_clicked(self):
        # 清除已有的combobox选项
        self.ui.comboBox_ser_select.clear()
        # 获取串口信息列表
        ser_list = serial.tools.list_ports.comports()
        # 判断是否检测到串口
        if len(ser_list) <= 0:
            QMessageBox.warning(self, '警告', '未检测到串口')
            return -1
        # 构造一个字典，以端口号(如COM2)作为键值
        # 方便后续更新串口详细信息时以端口号查询
        for i in range(len(ser_list)):
            # 循环将串口信息填入字典，com，详细信息
            self.ser_dist[ser_list[i][0]] = ser_list[i][1]
        for ser_port_info in ser_list:
            # 循环将串口信息填入combobox
            ser_name_list = str(ser_port_info[0])
            self.ui.comboBox_ser_select.addItem(ser_name_list)

    # 串口选择combobox选择槽函数
    def combobox_ser_select_changed(self):
        # 获取combobox的当前选择串口号
        com_x = self.ui.comboBox_ser_select.currentText()
        # 根据当前获取的串口号将详细串口信息显示出来
        if com_x == '':
            self.ui.label_ser_info.setText(' ')
        else:
            text = self.ser_dist[com_x]
            self.ui.label_ser_info.setText(str(text))
            print(text)

    # 打开串口按钮点击槽函数
    def pushbutton_ser_open_clicked(self):
        # 点击按钮会改变按钮状态，响应前需要先判断按钮状态
        if self.ui.pushButton_ser_open.text() == '打开串口':
            # 判断串口实例是否创建，如果没创建，则创建
            if self.ser_thread is None:
                self.ser_thread = mythread.MySerThread()
            print('打开串口')
            # 尝试打开串口
            try:
                self.ser_thread.open_ser(self.ui.comboBox_ser_select.currentText(), self.ui.lineEdit_baud.text())
                # 若打开串口，锁定串口相关ui
                self.ser_open_look_ui(False)
                # 修改按钮显示字符
                self.ui.pushButton_ser_open.setText('关闭串口')
            except mythread.CustomException as e:
                # 如果打开失败，显示异常信息
                QMessageBox.warning(self, '提示', str(e))
        else:
            print('关闭串口')
            try:
                # 尝试关闭串口，解锁ui，设置event为set退出线程，将ser_thread实例取消，设置为None
                self.ser_thread.close_ser()
                self.ui.pushButton_ser_open.setText('打开串口')
                self.ser_open_look_ui(True)
                self.ser_thread.thread_event.set()
                self.ser_thread = None
            except mythread.CustomException as e:
                QMessageBox.warning(self, '提示', str(e))

    # 锁定和解锁ui
    def ser_open_look_ui(self, status):
        self.ui.comboBox_ser_select.setEnabled(status)
        self.ui.lineEdit_baud.setEnabled(status)


def main():
    # 开启高分屏支持
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # 创建app实例
    app = QApplication([])
    # 创建主窗口实例
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
