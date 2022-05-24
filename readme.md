# 本项目是基于PyQt5的MVC模式开发的人脸识别项目

## 安装运行环境
```bash
pip install opencv-python --user
pip install opencv-contrib-python --user
pip install pymysql --user
pip install Pillow --user
```


## 打包程序
### 安装打包工具
```bash
pip install pyinstaller
```
### 运行打包工具
```bash
pyinstaller -F -w main.py
```