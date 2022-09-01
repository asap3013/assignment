import mysql.connector
import csv

conn = mysql.connector.connect(host="localhost", user="root",
                                     password='p@ssw0rd',database='all_db')

cursor = conn.cursor()
csv_data = csv.reader(open('/home/neosoft/Desktop/python_assignment/python_assignment_1/data.csv  '))


# for row in csv_data:
#     print(row)
#     cursor.execute(
#         "INSERT INTO employe (Emp_id,Name,phone) VALUES ({},'{}','{}')".format(row[0],row[1],row[2]))
        
# conn.commit()
# cursor.close()
# print('Done')