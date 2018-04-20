## Robot Framework – python开发的功能强大的自动化测试套件

#### Robot Framework安装配置

[文章出处，需要注意第二个文件的安装](https://www.ibm.com/developerworks/cn/opensource/os-cn-robot-framework/index.html)

#### 需要安装的软件和库

1. 安装python 2.7.x

    - 不支持python 3

2. 安装wxPython

    - 不要使用pip install -U wxPython
    - [获取文件](https://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/)
    - 选择与 Python 版本对应的版本，并且选择 unicode 版本

3. 安装 PyCrypto

    - [获取文件](http://www.voidspace.org.uk/python/modules.shtml)

4. 安装robot framework

    ```pip install robotframework```

5. 安装robot framework ride（robotFramework的IDE）

    ```pip install robotframework-ride```

6. 安装robot framework selenium library

    ```pip install robotframework-selenium2library```
    ```pip install robotframework-archivelibrary```
    ```pip install robotframework-SSHLibrary```
    ```pip install robotframework-ftplibrary```

7. 检查安装结果

    ```pip list```

8. 启动RIDE 编辑器

    - [PythonDir]\Scripts\ride.py

9. 补充软件包requests&robotframework-requests

    ```pip install requests```
    ```pip install robotframework-requests```

#### 入门篇

[阅读](http://blog.csdn.net/tulituqi/article/details/6834037)

#### 附录

[浏览器和浏览器的Driver 1.](http://blog.csdn.net/huilan_same/article/details/51896672)
[浏览器和浏览器的Driver 2.](http://npm.taobao.org/mirrors/chromedriver/)
[浏览器和浏览器的Driver 3.](http://blog.csdn.net/huilan_same/article/details/52615123)