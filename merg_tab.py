#_*_coding:utf-8_*_
#!/usr/bin/env python
import MySQLdb
print "Hello"
tag_db = MySQLdb.connect(host='',user='taguser',passwd='',db='tag')
tag_cur = tag_db.cursor()
table = ''
query = """select * from '%s'""" % table
command = tag_cur.execute(query)
results = command.fetchall()

new_db = MySQLdb.connect(host='',user='taguser',passwd='',db='tag')
new_cur = new_db.cursor()
insert = """insert into tag_pid(key.scope,tag,tag_payday,tag_iou,create_at,update_at) values(%s,%s,%s,%s,%s,%s,%s)"""
arguments = results
new_cur.executemany(insert,arguments)
print 'Finished'