# 基于 PyQt5 的MVC设计模式基础程序框架
本程序是一个Java转Python的程序员所对PyQt编程的理解，程序体现了在MVC思想下的PyQt的大型多窗口应用的开发过程。
# 模块定义
## view
存放视图内容，只存视图。
你使用Qt Designer设计的窗口都要放在本模块中，在本程序中如图所示
![view目录下的内容](https://images.iotlearn.cn/img/20220523152624.png)

## controller
存放界面逻辑相关的内容。
![controller存放页面逻辑](https://images.iotlearn.cn/img/20220523152743.png)
要求每个类与窗口的关系是**一一对应**

## res
存放程序用到的资源文件。qt的资源文件是*.qrc，需要使用Res_Generator.bat来将资源文件编译成二进制文件，然后在View的生成类中引用。
![](https://images.iotlearn.cn/img/20220523153448.png)

## main.py
程序的启动类。如果没有特殊的需求，建议不要改变其内容。一般来言，它只有启动窗口的作用。后期可能会写入其他内容。
```python
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
```