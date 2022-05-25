from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QWidget, QPushButton, QHBoxLayout, \
    QMessageBox
import UI_User_Dialog
import config


class User_Dialog(UI_User_Dialog.Ui_User_Dialog, QMainWindow):
    def __init__(self):
        super(UI_User_Dialog.Ui_User_Dialog, self).__init__()
        self.setupUi(self)
        # 禁止编辑表格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setRowCount(3)
        # 获取用户数据
        data = config.user_select_all()
        self.tableWidget.setRowCount(len(data))
        for row in range(len(data)):
            item1 = QTableWidgetItem(str(data[row][0]))
            self.tableWidget.setItem(row, 0, item1)
            item2 = QTableWidgetItem(str(data[row][1]))
            self.tableWidget.setItem(row, 1, item2)
            item3 = QTableWidgetItem(str(data[row][2]))
            self.tableWidget.setItem(row, 2, item3)
            item4 = QTableWidgetItem(str(data[row][3]))
            self.tableWidget.setItem(row, 3, item4)
            # 添加按钮
            item5 = QWidget()
            update_btn = QPushButton('修改')
            update_btn.setStyleSheet(''' text-align : center;background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  ''')
            view_btn = QPushButton('查看')
            view_btn.setStyleSheet(
                ''' text-align : center;background-color : DarkSeaGreen;height : 30px;border-style: outset;font : 13px  ''')
            view_btn.clicked.connect(lambda: self.clicked_cell_btn_view(data[row][0]))
            delete_btn = QPushButton('删除')
            delete_btn.setStyleSheet(
                ''' text-align : center;background-color : LightCoral;height : 30px;border-style: outset;font : 13px  ''')
            h_layout = QHBoxLayout()
            h_layout.addWidget(update_btn)
            h_layout.addWidget(view_btn)
            h_layout.addWidget(delete_btn)
            item5.setLayout(h_layout)
            self.tableWidget.setCellWidget(row, 4, item5)
        print(data)

    def clicked_cell_btn_view(self, id):
        # print(id)
        QMessageBox.information(self, '提示', str(id))
