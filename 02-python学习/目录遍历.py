#coding:utf8

"""
目录遍历思路
1、获取指定文件列表
2、循环(递归)判断文件并打印
"""

import os
import os.path as path2

def listFile(path):
    #获取当前文件夹下的所有文件列表
    listname=os.listdir(path) 
    # 遍历列表中文件的
    for name in listname:
        #为遍历的文件添加路径
        filename=path2.join(path,name)
        #判断是否是文件夹
        if(path2.isdir(filename)):
        #如果不是，则递归调用
            listFile(filename)
        else:
            print filename

if __name__  == "__main__":
    testpath='C:\\Users\\DELL\\Desktop\\1'
    #方法一
    # listFile(testpath)
    #方法二
    g = os.walk(testpath)
    for path,dir,filelist in g:
        for filename in filelist:
            if (filename.find('a') == -1):
                os.remove(path2.join(path,filename))
            else:
                print path2.join(path,filename)
