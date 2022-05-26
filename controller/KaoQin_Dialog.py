from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidgetItem, QWidget, QPushButton, QHBoxLayout, \
    QMessageBox

from view import UI_KaoQin_Dialog
import config
from controller.Result_Dialog import Result_Dialog


class KaoQin_Dialog(UI_KaoQin_Dialog.Ui_KaoQin_Dialog, QMainWindow):
    def __init__(self):
        super(UI_KaoQin_Dialog.Ui_KaoQin_Dialog, self).__init__()
        self.setupUi(self)
        # 设置表格格式
        # self.tableWidget.setColumnCount(4)
        # 表格标题字体加粗
        # font = self.tableWidget.horizontalHeader().font()
        # font.setBold(True)
        # self.tableWidget.horizontalHeader().setFont(font)
        # titles = ['id', '考勤轮次', '时间', '操作']
        # self.tableWidget.setHorizontalHeaderLabels(titles)
        # 禁止编辑表格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 加载数据
        self.get_data()

    def clicked_cell_btn_view(self, id):
        data = config.coka_select_by_turn(id)[0]
        self.view = Result_Dialog(data[1], data[2])
        self.view.show()

    def clicked_cell_btn_delete(self, id):
        # print(id)
        reply = QMessageBox.question(self, '警告',
                                     '<font size=16 face=' + '等线 Light' + ' color=red><b>你确定要删除本条记录？</b></font>',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            config.coka_delete_by_id(id)
            # 这里应该要刷新表格
            self.tableWidget.clearContents()
            self.get_data()
        else:
            return

    # 生成表格所需要用到的按钮
    def btn_for_row(self, id):
        widget = QWidget()
        # update_btn = QPushButton('修改')
        # update_btn.setStyleSheet(''' text-align : center;background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  ''')
        view_btn = QPushButton('查看')
        view_btn.setStyleSheet(
            ''' text-align : center;background-color : DarkSeaGreen;height : 30px;border-style: outset;font : 13px  ''')
        view_btn.clicked.connect(lambda: self.clicked_cell_btn_view(id))
        delete_btn = QPushButton('删除')
        delete_btn.setStyleSheet(
            ''' text-align : center;background-color : LightCoral;height : 30px;border-style: outset;font : 13px  ''')
        delete_btn.clicked.connect(lambda: self.clicked_cell_btn_delete(id))
        h_layout = QHBoxLayout()
        # h_layout.addWidget(update_btn)
        h_layout.addWidget(view_btn)
        h_layout.addWidget(delete_btn)
        widget.setLayout(h_layout)
        return widget

    def get_data(self):
        data = config.coka_select_all()
        self.tableWidget.setRowCount(len(data))
        for row in range(len(data)):
            item1 = QTableWidgetItem(str(data[row][0]))
            self.tableWidget.setItem(row, 0, item1)
            item2 = QTableWidgetItem(str(data[row][3]))
            self.tableWidget.setItem(row, 1, item2)
            item3 = QTableWidgetItem(str(data[row][2]))
            self.tableWidget.setItem(row, 2, item3)
            # 添加按钮
            item4 = self.btn_for_row(data[row][0])
            self.tableWidget.setCellWidget(row, 3, item4)
