class KaoQinEntity:
    def __init__(self):
        self.data = {
            # 考勤第一次
            "total": 0,  # 总人数
            "all_students": set(),  # 所有学生
            "unsigned_students": set(),
            "might_students": set(),
            "confirm_students": set(),
            "turn1": {
                "signed_students": set(),
                "unsigned_students": set(),
                "signed": 0,  # 签到人数
                "unsigned": 0,  # 未到人数
            },
            # 考勤第二次
            "turn2": {
                "signed_students": set(),
                "unsigned_students": set(),
                "signed": 0,  # 签到人数
                "unsigned": 0,  # 未到人数
            },
        }

    def set_student(self, student):
        self.data['all_students'] = student
        self.update()

    def get_student(self):
        return self.data['all_students']

    def set_turn1(self, signed_students):
        self.data['turn1']['signed_students'] = signed_students
        self.update(signed_students, 1)

    def set_turn2(self, signed_students):
        self.data['turn2']['signed_students'] = signed_students
        self.update(signed_students, 2)

    def update(self, *args):
        if len(args) == 2:
            # 获取参数
            signed_students, turn = args
            if turn == 1:
                self.data['turn1']['signed'] = len(signed_students)
                self.data['turn1']['unsigned'] = self.data['total'] - len(signed_students)
                # 计算未签到学生
                self.data['turn1']['unsigned_students'] = self.get_unsigned_students(signed_students)
            elif turn == 2:
                self.data['turn2']['signed'] = len(signed_students)
                self.data['turn2']['unsigned'] = self.data['total'] - len(signed_students)
                # 计算未签到学生
                self.data['turn2']['unsigned_students'] = self.get_unsigned_students(signed_students)
                # 对数据进行分析
                self.analysis()
        else:
            # 更新学生总数
            self.data['total'] = len(self.data['all_students'])

    def get_unsigned_students(self, signed_students):
        return self.data['all_students'] - signed_students

    def get_result(self):
        t1 = self.data['turn1']['signed_students'] & self.data['turn2']['signed_students']
        t2 = self.data['turn1']['unsigned_students'] & self.data['turn2']['unsigned_students']
        t3 = (self.data['turn1']['signed_students'] | self.data['turn2']['signed_students']) - t1
        print("第一轮签到人员", self.data['turn1']['signed_students'])
        print("\t未签到人员", self.data['turn1']['unsigned_students'])
        print("第二轮签到人员", self.data['turn2']['signed_students'])
        print("\t未签到人员", self.data['turn2']['unsigned_students'])
        print("第一轮和第二轮都签到人员", t1)
        print("第一轮和第二轮都未签到人员", t2)
        print("可能签到人员", t3)

    def analysis(self):
        self.data['confirm_students'] = self.data['turn1']['signed_students'] & self.data['turn2']['signed_students']
        self.data['unsigned_students'] = self.data['turn1']['unsigned_students'] & self.data['turn2']['unsigned_students']
        self.data['might_students'] = (self.data['turn1']['signed_students'] | self.data['turn2']['signed_students']) - self.data['confirm_students']


# 测试签到功能
if __name__ == '__main__':
    a = set()
    a.add('庞宇宇')  # 验证重复
    a.add('庞宇宇')
    a.add('李冀飞')
    a.add('张罕')
    a.add('马金建')
    print(a)
    # 开启签到
    sign = KaoQinEntity()
    # 获取所有学生
    sign.set_student(a)
    # 第一次签到
    sign.set_turn1({'庞宇宇', '李冀飞'})
    # 第二次签到
    sign.set_turn2({'庞宇宇', '马金建'})
    sign.get_result()
    # a = KaoQinEntity()
    # a.set_student({'庞宇宇','李冀飞','张罕','马金建'})
    # a.get_unsigned_students({'庞宇宇'})
    # print(a)
