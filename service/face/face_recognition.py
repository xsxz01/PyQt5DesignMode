import json


import cv2
import os
from PIL import Image
import numpy as np
# 全局学生信息数组
# all_students = [
#     {"id": 8001, "name": "PangYuYu"},
#     {"id": 8002, "name": "ZhangHan"},
# ]
# 从本地读入数据
def loadMsg():
    # 测试数据，实际应该是直接读取本地文件
    # return [
    #     {"id": 8001, "name": "PangYuYu"},
    #     {"id": 8002, "name": "ZhangHan"},
    # ]
    f = open("student.db", "r")
    json_str = f.read()
    f.close()
    return json.loads(json_str)
# 写入学生信息
def writeMsg(id, name, university):
    all_students = loadMsg()
    # all_students = []
    t = { "id": id,"name":name,"university":university}
    all_students.append(t)
    # 写入文件
    f = open("student.db", "w")
    f.write(json.dumps(all_students))
    f.close()
    return True

# 人脸检测，采集数据
def detection(NameId, number):
    cap = cv2.VideoCapture(0)  # 0表示默认系统摄像头
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  # 加载人脸训练器xml文件
    font = cv2.FONT_HERSHEY_SIMPLEX

    count = 1
    while True:
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
            cv2.putText(img, NameId, (x + w + 5, y - 5), font, 0.6, (0, 255, 0), 1)  # 1, 1分别代表字体大小和粗细
            cv2.imwrite('./FaceData/User_' + NameId + '_' + str(count) + '.jpg', gray[y:y + h, x:x + w])
            print('采集第', count, '张成功！')
            count += 1
        cv2.imshow('Detection', img)

        if count > number:
            print('人脸信息采集完毕！')
            break

        key = cv2.waitKey(10)  # 间隔10ms刷新
        if cv2.getWindowProperty('Detection', cv2.WND_PROP_AUTOSIZE) < 1:  # 鼠标关闭窗口
            break
        elif key == 8:  # 键盘按×退出
            break

    cap.release()  # 关闭摄像头
    cv2.destroyWindow('Detection')  # 删除窗口


# 训练人脸数据
def training():
    path = './FaceData'
    all_image_path = [os.path.join(path, i) for i in os.listdir(path)]

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # 创建一个训练器
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  # 加载人脸训练器xml文件

    count = 1
    # 训练需要两组数据ids、face_samples
    ids = []
    face_samples = []
    
    for each_image in all_image_path:
        id = int(os.path.split(each_image)[1].split('_')[1])
        PIL_image = Image.open(each_image).convert('L')  # 把图片转换成训练所需要的数据
        np_image = np.array(PIL_image, 'uint8')  # 把数据长度格式转换为8位
        faces = faceCascade.detectMultiScale(np_image)  # 检测转换的数据矩阵里面有没有脸
        for (x, y, w, h) in faces:
            face_samples.append(np_image)
            ids.append(id)
        print('已训练', count, '张')
        count += 1

    recognizer.train(face_samples, np.array(ids))
    recognizer.write('people_face.yml')
    print('人脸数据训练成功！')
    return '人脸数据训练成功！'


# 开始识别
def recognition(all_data):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0表示默认系统摄像头
    font = cv2.FONT_HERSHEY_SIMPLEX
    # all_students = loadMsg()
    all_students = all_data
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # 创建一个训练器
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  # 加载人脸训练器xml文件
    recognizer.read('people_face.yml')  # 加载训练好的文件
    # 有序列表，用来放学生进入的顺序的
    student_list = []
    # 检测到的当前学生的id
    current_id = 0
    # 获取所有已经训练了的学生

    while True:
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
            # if int(id) == 8001:
            #     name_str = 'Pang Yu Yu'
            # if int(id) == 8002:
            #     name_str = 'Dong Xiang Ting'
            # if int(id) == 8003:
            #     name_str = 'Zhang Han'
            # if int(id) == 1001:
            #     name_str = 'Li Ji Fei'
            for x in all_students:
                if x[0] == id:
                    name_str = x[2]
                    # 先判断是否打卡 根据轮次获取本轮所有的考勤信息
                    # 没打卡   数据库存入一条打卡的信息
                    # 已打卡   直接跳过
                    break

            student_list.append(name_str)
            # cv2.putText(img, "name_str", (x + w + 5, y - 5), font, 0.6, (0, 255, 0), 1)

        # 绘制签到信息
        student_list_str = "".join(set(student_list))
        last_student = ''
        if len(set(student_list)) > 0:
            last_student = student_list[len(student_list) - 1]

        cv2.putText(img, 'Current People Num: '+str(len(set(student_list))), (10, 20), font, 0.6, (0, 255, 0), 1)
        cv2.putText(img, 'Last Person: '+ last_student, (10, 40), font, 0.6, (0, 255, 0), 1)
        cv2.putText(img, 'Current Student List: ['+student_list_str+']', (10, 60), font, 0.6, (0, 255, 0), 1)
        cv2.putText(img, 'Current Student ID: ' + str(current_id), (10, 80), font, 0.6, (0, 255, 0), 1)

        cv2.imshow('Recognition', img)
        key = cv2.waitKey(10)  # 间隔10ms刷新

        if cv2.getWindowProperty('Recognition', cv2.WND_PROP_AUTOSIZE) < 1:  # 鼠标关闭窗口
            break
        elif key == 8:  # 键盘按×退出
            break
    cap.release()  # 关闭摄像头
    cv2.destroyWindow('Recognition')  # 删除窗口


if __name__ == '__main__':
    # recognition()
    # 编号 采集张数
    # 存入文件数据
    # id    学生姓名
    # detection(str(8003),200)
    # all_students = loadMsg()
    # writeMsg(8001,'Pang Yu Yu','YCU')
    training()
    # pass
