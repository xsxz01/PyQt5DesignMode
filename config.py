import pymysql
import datetime as dt

mysql_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "database": "face"
}


# 连接数据库
def get_connection():
    return pymysql.connect(**mysql_config)


# 插入学生表
def user_insert(sno, sname, college):
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"INSERT INTO `face`.`sys_user` (`sno`, `sname`, `college`) VALUES (%s, %s, %s);"
    try:
        cursor.execute(sql, [sno, sname, college])
        connection.commit()
    except Exception as e:
        print("操作失败", e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# 根据学号查询学生信息
def user_select_by_sno(sno):
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"SELECT `id`, `sno`, `sname`, `college` FROM `face`.`sys_user` WHERE  `sno`=%s;"
    cursor.execute(sql, [sno])
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result


# 根据学号查询学生信息
def user_select_all():
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"SELECT `id`, `sno`, `sname`, `college` FROM `face`.`sys_user`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


# 插入考勤记录
def coka_insert(data, time, turn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"INSERT INTO `face`.`sys_coka` (`data`, `time`, `turn`) VALUES (%s, %s, %s);"
    try:
        cursor.execute(sql, [data, time, turn])
        connection.commit()
    except Exception as e:
        print("操作失败", e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def coka_get_max_turn():
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"SELECT MAX(turn) from sys_coka"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


# 查询某一轮次考勤结果
def coka_select_by_turn(turn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = f"SELECT sys_coka.id AS id, sys_user.sname AS sname, sys_user.college AS college, sys_coka.time AS stime  FROM sys_user, sys_coka WHERE sys_coka.uid=sys_user.id AND sys_coka.turn=%s"
    cursor.execute(sql, [turn])
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


if __name__ == '__main__':
    # 测试
    print(get_connection())
    # user_insert("庞宇宇", "运城学院")
    # coka_insert(8001,dt.datetime.now().isoformat(),1)\
    # print(coka_select_by_turn(1))
