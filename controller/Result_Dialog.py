from PyQt5.QtWidgets import QMainWindow
import UI_Result_Dialog


class Result_Dialog(UI_Result_Dialog.Ui_Result_Dialog, QMainWindow):
    def __init__(self, kao_qin_entity):
        super(UI_Result_Dialog.Ui_Result_Dialog, self).__init__()
        self.setupUi(self)
        self.kao_qin_entity = kao_qin_entity
        self.lcdNumber_total.display(str(self.kao_qin_entity.data['total']))
        self.lcdNumber_unsigned.display(str(len(self.kao_qin_entity.data['unsigned_students'])))
        self.lcdNumber_might.display(str(len(self.kao_qin_entity.data['might_students'])))
        self.lcdNumber_confirm.display(str(len(self.kao_qin_entity.data['confirm_students'])))
        # 更新列表
        self.listWidget_confirm_signed.addItems(self.kao_qin_entity.data['confirm_students'])
        self.listWidget_might_signed.addItems(self.kao_qin_entity.data['might_students'])
        self.listWidget_unsigned.addItems(self.kao_qin_entity.data['unsigned_students'])
        # 更新第一轮列表
        self.listWidget_turn1_signed.addItems(self.kao_qin_entity.data['turn1']['signed_students'])
        self.listWidget_turn1_unsigned.addItems(self.kao_qin_entity.data['turn1']['unsigned_students'])
        # 更新第二轮列表
        self.listWidget_turn2_signed.addItems(self.kao_qin_entity.data['turn2']['signed_students'])
        self.listWidget_turn2_unsigned.addItems(self.kao_qin_entity.data['turn2']['unsigned_students'])