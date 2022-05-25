from PyQt5.QtWidgets import QMainWindow, QMessageBox

import UI_Insert_Dialog
import config
import face_recognition


class Insert_Dialog(UI_Insert_Dialog.Ui_Insert_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Insert_Dialog.Ui_Insert_Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.setHidden(True)

    def start(self):
        sname = self.lineEdit.text()
        sno = self.lineEdit_2.text()
        college = self.lineEdit_3.text()
        config.user_insert(sname,sno,college)
        QMessageBox.information(self,'提示','用户已存入数据库')
        # 启动用户采集数据
        # 学号，采集数量
        face_recognition.detection(sno, 200)
        # 训练数据
        QMessageBox.information(self, '提示', '正在进行前置操作')
        face_recognition.training()
        QMessageBox.information(self, '提示', '用户信息采集完成')
        self.close()