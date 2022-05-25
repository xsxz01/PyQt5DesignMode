# 软件部署教程
*pyqt暂时未找到比较合适的部署教程，因此只写运行的教程*

## 安装运行环境
```bash
pip install opencv-python --user
pip install opencv-contrib-python --user
pip install pymysql --user
pip install Pillow --user
```
## 导入数据库
建议使用Navicat Mysql

## 修改配置文件
修改config.py中的数据库配置，位置如下所示，
```python
mysql_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "database": "face"
}
```