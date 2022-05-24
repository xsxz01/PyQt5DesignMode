from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidget

import UI_Simple_Dialog


class Simple_Dialog(UI_Simple_Dialog.Ui_Simple_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Simple_Dialog.Ui_Simple_Dialog, self).__init__()
        self.setupUi(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        titles = ['签到轮次','是否签到','日期']
        self.tableWidget.setHorizontalHeaderLabels(titles)