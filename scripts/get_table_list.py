import cx_Oracle
import os
import sys

envname=sys.argv[1]
postingdate=sys.argv[2]
batchid=sys.argv[3]

print 'Argument List:', str(sys.argv)

if os.path.exists("table_output"):
        os.system("echo > table_output")

dbname="<schema>"+envname
dbpass="<pass>"
dbsid="<dbsid>"


dbcon = cx_Oracle.connect(dbname + '/' + dbpass + '@' +dbsid)
dbcursor = dbcon.cursor()

table_list = 'list'
table_output = 'table_output'
with open(table_list) as tables:
    for table in tables:
                sql="select count(*) from " + table
                table_count = dbcursor.execute(sql)
                for row in table_count:
                        if row[0] > 0:
                                print(table.rstrip() + " has data, here's the SQL ... select * from " + table.rstrip()  + " where postingdate = '"+postingdate+"' and batchid in ("+batchid+") \n")
                                with open(table_output, 'a') as output:
                                        output.write(table.rstrip() + " has data, here's the SQL ... select * from " + table.rstrip() + " where postingdate = '"+postingdate+"' and batchid in ("+batchid+") \n")
                        else:
                                print(table.rstrip() + " no data found \n")
                                with open(table_output, 'a') as output:
                                        output.write(table.rstrip() + " no data found \n")

if dbcursor:
    dbcursor.close()
if dbcon:
    dbcon.close()

