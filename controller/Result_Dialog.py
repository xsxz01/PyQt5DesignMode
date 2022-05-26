import json

from PyQt5.QtWidgets import QMainWindow

from view import UI_Result_Dialog


class Result_Dialog(UI_Result_Dialog.Ui_Result_Dialog, QMainWindow):
    # kao_qin_entity
    # data, time
    def __init__(self, *args):
        super(UI_Result_Dialog.Ui_Result_Dialog, self).__init__()
        self.setupUi(self)
        print(args)
        if len(args) == 2:
            data, time = args
            self.label.setText(self.label.text() + f"\t{time}")
            self.kao_qin_entity = json.loads(data)
            self.lcdNumber_total.display(str(self.kao_qin_entity['total']))
            self.lcdNumber_unsigned.display(str(len(self.kao_qin_entity['unsigned_students']['py/set'])))
            self.lcdNumber_might.display(str(len(self.kao_qin_entity['might_students']['py/set'])))
            self.lcdNumber_confirm.display(str(len(self.kao_qin_entity['confirm_students']['py/set'])))
            # 更新列表
            self.listWidget_confirm_signed.addItems(self.kao_qin_entity['confirm_students']['py/set'])
            self.listWidget_might_signed.addItems(self.kao_qin_entity['might_students']['py/set'])
            self.listWidget_unsigned.addItems(self.kao_qin_entity['unsigned_students']['py/set'])
            # 更新第一轮列表
            self.listWidget_turn1_signed.addItems(self.kao_qin_entity['turn1']['signed_students']['py/set'])
            self.listWidget_turn1_unsigned.addItems(self.kao_qin_entity['turn1']['unsigned_students']['py/set'])
            # 更新第二轮列表
            self.listWidget_turn2_signed.addItems(self.kao_qin_entity['turn2']['signed_students']['py/set'])
            self.listWidget_turn2_unsigned.addItems(self.kao_qin_entity['turn2']['unsigned_students']['py/set'])
            print(data,time)
        else:
            kao_qin_entity = args[0]
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