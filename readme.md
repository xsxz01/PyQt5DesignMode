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
pip install auto-py-to-exe
```
### 运行打包工具
```bash
auto-py-to-exe
```
![打包工具](https://images.iotlearn.cn/img/20220526212516.png)

选择好脚本位置后，选择对应的选项，点击打包即可

![打包完成](https://images.iotlearn.cn/img/20220526212629.png)

点击**打开输出目录**即可找到你所打包好的可执行文件