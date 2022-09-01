from operator import index
import pandas as pd
import mysql.connector

db = mysql.connector.connect(
                host = "localhost",
                user  ="root",
                password ='p@ssw0rd',
                database = "all_db")


cursor = db.cursor()

query = "select Emp_id,Name,phone from employe"

cursor.execute(query)

query_result = cursor.fetchall()
all_Emp_id = []
all_Name = []
all_phone = []

for Emp_id,Name,phone in query_result:
    all_Emp_id.append(Emp_id)
    all_Name.append(Name)
    all_phone.append(phone)

# To store data in csv file

dic = ({'Emp_id': all_Emp_id,'Name':all_Name,'phone':all_phone})
df = pd.DataFrame(dic)
df_csv = df.to_csv("/home/neosoft/Desktop/python_assignment/python_assignment_5/fetch_data.csv")


