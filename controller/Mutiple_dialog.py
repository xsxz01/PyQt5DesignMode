from PyQt5.QtWidgets import QMainWindow

from view import UI_Mutiple_Dialog


class Muitiple_Dialog(UI_Mutiple_Dialog.Ui_Muitiple_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Mutiple_Dialog.Ui_Muitiple_Dialog, self).__init__()
        self.setupUi(self)
        titles = ['签到轮次', '是否签到', '日期']
        self.tableView.setHorizontalHeaderLabels(titles)