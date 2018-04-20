### mysql操作


    #coding=utf8
    import md5
    import random
    import os


    # files=os.listdir(os.getcwd())
    # for file in files:
    #     ext=os.path.splitext(file)
    #     print ext[1]
    #     if ext[1] == ".txt":
    #         os.remove(file)

    # for i in range(100):
    #     file=open('C:/Users/DELL/Desktop/3/'+md5.new(str(i+1)).hexdigest()+'.txt','w')
    #     s=''
    #     for ii in range(26):
    #         s += chr(random.randint(65,91))
    #     file.write(s)
    #     file.close()

    # import sys
    # from colorama import init

    # init(strip=not sys.stdout.isatty())

    # from termcolor import cprint
    # from pyfiglet import figlet_format
    # cprint(figlet_format('GAME OVER',font='starwars'),'yellow','on_blue',attrs=['bold'])

    import MySQLdb

    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","","mysql" )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()

    print "Database version : %s " % data

    # 关闭数据库连接
    db.close()
