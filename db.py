#!/usr/bin/python3
 
import pymysql
 
def InitDb():
    # 打开数据库连接 后期需要写成配置
    db = pymysql.connect(host='localhost',
                        user='root',
                        password='123456',
                        database='sbhermes',
                        autocommit=True,
                        )
    return db
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # sql = 'insert into goods(image) values("xieming")'
    # cursor.execute(sql)

    # # 使用 execute()  方法执行 SQL 查询 
    # cursor.execute("SELECT * from goods")
    
    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()


    # print (data)
    
    # # 关闭数据库连接
    # db.close()


    # 插入多条数据
    # sql = "insert into login(name, pwd) values(%s,%s)"
    # sql = "insert into login values(%s,%s)"
    # res = cursor.executemany(sql, [("xm", '111'), ('mx', '111')])