#!/usr/bin/python3
 
import pymysql


def InitDbConnection():
    # 打开数据库连接 后期需要写成配置
    db = pymysql.connect(host='124.222.188.78',
                        user='root',
                        password='123456',
                        database='sbhermes',
                        autocommit=True,
                        )
    return db

# 全局变量
DB = InitDbConnection()

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

def ClearGoods():
    cursor = DB.cursor()
    sql1 = 'delete from goods where id >0'
    cursor.execute(sql1)

def GoodsInsert(imageRes):
    cursor = DB.cursor()
    for image in imageRes:
        #插入
        sql2 = 'insert into goods(image) values(%s)'
        cursor.execute(sql2,(image))

def GetGoods(start,limit):
    cursor= DB.cursor()
    sql1='select count(*) from goods'
    cursor.execute(sql1)
    count = cursor.fetchone()
    cursor.execute("SELECT * from goods limit %s offset %s ",args=[limit,start])
    datas = cursor.fetchall()
    images=[]
    for v in datas:
        images.append(v[1])
    dic ={'images':images,'total':count[0]}
    return dic



