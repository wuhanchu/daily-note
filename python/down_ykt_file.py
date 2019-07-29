#coding:utf-8
import pymysql
import requests

# 打开数据库连接
db = pymysql.connect("iwillgoodata1.mysql.rds.aliyuncs.com","ykt_user","Ykt_User","iwillgoo-ykt-server" )


cursor = db.cursor()

# 查询中奖文件
cursor.execute("select id,photos  from evidence  where daily_result = \"PRISE\"")

results = cursor.fetchall()
for row in results:
			
    #  下载文件
    r = requests.get(row[1])
    with open( str(row[0]) + ".jpg", "wb") as file:
        file.write(r.content)
        
db.close()