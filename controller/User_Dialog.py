from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QWidget, QPushButton, QHBoxLayout, \
    QMessageBox
from view import UI_User_Dialog
import config
from controller.User_Alter_Dialog import User_Alter_Dialog


class User_Dialog(UI_User_Dialog.Ui_User_Dialog, QMainWindow):
    def __init__(self):
        super(UI_User_Dialog.Ui_User_Dialog, self).__init__()
        self.setupUi(self)
        # 禁止编辑表格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setRowCount(3)
        # 获取用户数据
        self.get_data()

    # def clicked_cell_btn_view(self, id):
    #     # print(id)
    #     QMessageBox.information(self, '提示', str(id))

    def clicked_cell_btn_delete(self, id):
        # print(id)
        # QMessageBox.information(self, '提示', str(id))
        reply = QMessageBox.question(self, '警告',
                                     '<font size=16 face=' + '等线 Light' + ' color=red><b>你确定要删除本用户？</b></font>',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            config.user_delete_by_id(id)
            # 这里应该要刷新表格
            self.tableWidget.clearContents()
            self.get_data()
        else:
            return

    def clicked_cell_btn_update(self, id):
        # print(id)
        # QMessageBox.information(self, '提示', str(id))
        self.update = User_Alter_Dialog(id)
        self.update.show()
        self.update._signal.connect(self.refresh)

    def refresh(self, signal):
        if signal == 'refresh':
            self.tableWidget.clearContents()
            self.get_data()

    # 生成表格所需要用到的按钮
    def btn_for_row(self, id):
        widget = QWidget()
        update_btn = QPushButton('修改')
        update_btn.setStyleSheet(
            ''' text-align : center;background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  ''')
        update_btn.clicked.connect(lambda: self.clicked_cell_btn_update(id))
        # view_btn = QPushButton('查看')
        # view_btn.setStyleSheet(
        #     ''' text-align : center;background-color : DarkSeaGreen;height : 30px;border-style: outset;font : 13px  ''')
        # view_btn.clicked.connect(lambda: self.clicked_cell_btn_view(id))
        delete_btn = QPushButton('删除')
        delete_btn.setStyleSheet(
            ''' text-align : center;background-color : LightCoral;height : 30px;border-style: outset;font : 13px  ''')
        delete_btn.clicked.connect(lambda: self.clicked_cell_btn_delete(id))
        h_layout = QHBoxLayout()
        h_layout.addWidget(update_btn)
        # h_layout.addWidget(view_btn)
        h_layout.addWidget(delete_btn)
        widget.setLayout(h_layout)
        return widget

    def get_data(self):
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
            item5 = self.btn_for_row(data[row][0])
            self.tableWidget.setCellWidget(row, 4, item5)
