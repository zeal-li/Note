from email import charset
import pymysql
conn = pymysql.connect(host='localhost', user='root',
                       passwd='', db='mydb', port=3306, charset='utf8')

cursor = conn.cursor()
cursor.execute(
    "insert into students (name,sex,grade) values(%s,%s,%s)", ('张三', '女', 87))
conn.commit()
