import pymysql
# 创建连接
connection = pymysql.connect(host='127.0.0.1',user='root',password='root',db='test')
# 创建游标
cur = connection.cursor()
# 插入一条新记录
sql = 'insert into '