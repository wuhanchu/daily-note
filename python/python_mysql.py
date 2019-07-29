#coding:utf-8
import MySQLdb
import httplib
import json

#from urllib import request, parse, error

db = MySQLdb.connect("iwillgoodata1.mysql.rds.aliyuncs.com","tms_user","JhH7XYzPtPsWPA4w","tms_data" )
#db = MySQLdb.connect("localhost","root","whcxhwyz","iwillgoo" )

cursor = db.cursor()
conn = httplib.HTTPConnection("api.map.baidu.com")

cursor.execute("select KEYNO,SADDR,NLATITUDE,NLONGITUDE from gg_corp  where IFLAG = 'wx' and NLATITUDE is null")

results = cursor.fetchall()
for row in results:
			
	if not row[1] or "#" in row[1]:
		continue
	
	path = "/place/v2/search?q="+row[1]+"&region=福建&output=json&ak=TF9uZIGSSLdT4yNQQXjvi5N5"
	conn.request("GET", path)
	print path
	r1 = conn.getresponse()
	body = r1.read()  
	print body
	if not body:
		continue
	
	result = json.loads(body)
	if len(result['results']) > 0:
		try:
			sql = "UPDATE gg_corp SET NLATITUDE = "+str(result['results'][0]['location']['lat'])+",NLONGITUDE="+str(result['results'][0]['location']['lng'])+" where KEYNO='"+row[0]+"'"
			print sql
			cursor.execute(sql)
			db.commit()
		except Exception,e:
			print str(e)
			db.rollback()

db.close()