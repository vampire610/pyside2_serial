from PySide2.QtWidgets import QComboBox
from PySide2.QtCore import Signal


class MyComboBox(QComboBox):
    clicked = Signal()  # 创建一个信号

    def showPopup(self):  # 重写showPopup函数,"弹出下拉列表"
        self.clicked.emit()  # 弹出前发送信号
        super(MyComboBox, self).showPopup()  # 调用父类的showPopup()
