### 安装指引顺序 

1. python-2.7.5.msi
2. setuptools-2.0.1
3. pip-1.4.1
4. wxPython2.8-win32-unicode-2.8.12.1-py27.exe
5. robotframework-2.8.1.win32.exe
6. robotframework-ride-1.2.3.win32.exe
7. robotframework-selenium2library-1.4.0
8. decorator-3.4.0
9. docutils-0.11
10. selenium-2.35.0
11. pywin32-218.win32-py2.7.exe
12. AutoItLibrary-1.1
13. franz-see-Robotframework-Database-Library-0.6-3-g216432f
14. requests-2.18.4
15. robotframework-requests-0.4.7

> 安装注意：

> a、如果是exe的直接安装就好了。

> b、对于只有源代码的测试库（只有py文件）的安装，请在进入cmd命令行后，进入测试库的目录（有setup.py的目录），输入python setup.py install进行安装。
如果提示python不是命令，请把python的安装目录加到环境变量的path中。

> c、对于只有egg文件的测试库的安装，需要先安装setuptools（写这篇文章时最新版本为setuptools-0.6c11.win32-py2.7.exe），安装之后，在命令行使用easy_install加egg文件名或目录名，例如easy_install docutils-0.9-py2.7.egg

> 以上两个在命令行进行安装的方式，必须先要在环境变量PATH中加入Python的路径，如果安装在D:\Python27，那么一般建议在PATH中增加D:\Python27和D:\Python27\Scripts 两个路径。



> 按照以上的要求安装完一系列程序后，务必检查如下：

- 如果是首次使用RF在IE浏览器上测试的同学，务必检查以下几个设置：

- 1、IE选项设置的安全页中，4个区域的启用保护模式的勾选都去掉（或都勾上）

- 2、IE选项设置的连接页中，局域网设置里的代理服务器设置，不能勾选。如果需要配置代理，请使用上面的pac自动配置脚本来使用代理。

- 3、IE页面的显示比例要为100%

- 4、将安装包中的IEDriverServer.exe文件，chromedriver.exe，放到环境变量path路径的目录里或把他所在的目录加到path环境变量中。

- 完成以上所有后，请执行“内核文件更新”文件夹中的说明。

#### 运行RIDE，是否正常打开，完毕。