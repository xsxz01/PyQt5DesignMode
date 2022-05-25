import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import UI_RunDialog
import config
import face_recognition
from KaoQinEntity import KaoQinEntity
from Result_Dialog import Result_Dialog


class RunDialog(UI_RunDialog.Ui_Run_Dialog, QMainWindow):
    def __init__(self):
        super(UI_RunDialog.Ui_Run_Dialog, self).__init__()
        self.setupUi(self)
        # 初始化摄像头参数
        self.cap_state = -1
        self.cap_property = None
        # 生成轮次参数
        self.turn = config.coka_get_max_turn()
        ttt = self.turn[0][0]
        self.label_10.setText(str(ttt))
        # 初始化考勤信息
        self.kao_qin_entity = KaoQinEntity()
        self.turn1_signed_students = set()
        self.turn2_signed_students = set()
        # 初始化考勤流程
        '''
        step 为考勤步骤
        状态码     意义
        -1         结束
        1          第一步（第一轮）
        2          第一轮结束
        3          第二轮开始
        4          第二轮结束
        '''
        self.step = -1
        self.pushButton_start.clicked.connect(self.start2)

    def start(self):
        data = config.user_select_all()
        face_recognition.recognition(data)

    def start2(self):
        _translate = QtCore.QCoreApplication.translate
        cap = self.cap_property
        if self.cap_state == 1:
            # 关闭摄像头
            cap.release()  # 关闭摄像头
            self.cap_state = -1
            self.label_cap.setHidden(True)
            # 对step进行控制
            if self.step == 1:
                self.step = 2
                self.label_2.setText("第一轮考勤完毕")
                self.pushButton_start.setText(_translate("Run_Dialog", "开始"))
                self.kao_qin_entity.set_turn1(self.turn1_signed_students)
                self.label_4.setText('~人')
                self.label_6.setText('~人')
                self.label_8.setText('~人')
            elif self.step == 3:
                self.step = 4
                self.label_2.setText("第二轮考勤完毕")
                self.kao_qin_entity.set_turn2(self.turn2_signed_students)
                QMessageBox.information(self, '提示', '考勤已结束，点击确认查看结果')
                self.result = Result_Dialog(self.kao_qin_entity)
                self.result.show()
                self.setHidden(True)
            return
        else:
            # 对step进行控制
            data = config.user_select_all()
            self.label_4.setText(str(len(data)))
            if self.step == -1:
                self.step = 1
                self.label_2.setText("正在进行考勤第一轮")
                all_students_set = set()
                for i in data:
                    all_students_set.add(i[1])
                self.kao_qin_entity.set_student(all_students_set)
            elif self.step == 2:
                self.step = 3
                self.label_2.setText("正在进行考勤第二轮")
            # 采用直接调用OpenCV的方式
            self.label_cap.setHidden(False)
            self.cap_property = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0表示默认系统摄像头
            self.cap_state = 1
            # 修改按钮标题
            self.pushButton_start.setText(_translate("Run_Dialog", "停止"))
            cap = self.cap_property
            font = cv2.FONT_HERSHEY_SIMPLEX
            all_students = data
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # 创建一个训练器
            faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  # 加载人脸训练器xml文件
            recognizer.read('people_face.yml')  # 加载训练好的文件
            # 有序列表，用来放学生进入的顺序的
            student_list = []
            # 检测到的当前学生的id
            current_id = 0
            # 获取所有已经训练了的学生
            while True:
                if self.cap_state == -1:
                    cap.release()
                    break
                ok, img = cap.read()  # 读取摄像头数据, 必须返回两个参数
                if not ok:
                    break

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像

                # faces存放所有脸信息(要用灰度图片检测)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(32, 32)
                )

                # 如果有脸，就把脸框起来画矩形
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))
                    # 开始识别人脸
                    id, con = recognizer.predict(gray[y:y + h, x:x + w])
                    current_id = id
                    # 判断这个人是谁
                    name_str = 'none'
                    for x in all_students:
                        # 识别到考勤人员
                        if x[2] == str(id):
                            if self.step == 1:      # 第一轮
                                self.turn1_signed_students.add(x[1])
                                self.label_6.setText(str(len(self.turn1_signed_students)) + '人')
                                self.label_8.setText(str(len(self.kao_qin_entity.data['turn1']['unsigned_students'])) + '人')
                            elif self.step == 3:    # 第二轮
                                self.turn2_signed_students.add(x[1])
                                self.label_6.setText(str(len(self.turn2_signed_students)) + '人')
                                self.label_8.setText(str(len(self.kao_qin_entity.data['turn2']['unsigned_students'])) + '人')
                            name_str = x[2]
                            # 先判断是否打卡 根据轮次获取本轮所有的考勤信息
                            # 没打卡   数据库存入一条打卡的信息
                            # 已打卡   直接跳过
                            break

                    student_list.append(name_str)

                # 绘制签到信息
                student_list_str = "".join(set(student_list))
                last_student = ''
                if len(set(student_list)) > 0:
                    last_student = student_list[len(student_list) - 1]

                # cv2.putText(img, 'Current People Num: ' + str(len(set(student_list))), (10, 20), font, 0.6, (0, 255, 0),
                #             1)
                # cv2.putText(img, 'Last Person: ' + last_student, (10, 40), font, 0.6, (0, 255, 0), 1)
                # cv2.putText(img, 'Current Student List: [' + student_list_str + ']', (10, 60), font, 0.6, (0, 255, 0),
                #             1)
                cv2.putText(img, 'Current Student ID: ' + str(current_id), (10, 80), font, 0.6, (0, 255, 0), 1)

                # cv2.imshow('Recognition', img)
                # 设置图片大小
                img = cv2.resize(img, (800, 600))
                image_height, image_width, image_depth = img.shape
                QIm = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
                # 绘制摄像头内容到label_cap
                self.label_cap.setPixmap(QPixmap.fromImage(QIm))
                cv2.waitKey(10)

    def closeEvent(self, event):
        cap = self.cap_property
        # 释放摄像头
        cap.release()
        # 继续执行关闭
        event.accept()
