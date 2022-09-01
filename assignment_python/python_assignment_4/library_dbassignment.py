import mysql.connector

conn = mysql.connector.connect(host = "localhost", user  ="root",
                                     password ='p@ssw0rd',database = "library_management")

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE library_management")

# cursor.execute("SHOW DATABASES")

# for i in cursor:
#     print(i)


# data_1 = '''CREATE TABLE book_category(ID INT AUTO_INCREMENT PRIMARY KEY,Books VARCHAR(30),Author VARCHAR(15));'''

# cursor.execute(data_1)
# ALTER TABLE book_category ADD FOREIGN KEY (Author) REFERENCES book_Authors(Author);

# data_2 = '''CREATE TABLE book_Authors(ID INT AUTO_INCREMENT UNIQUE KEY,Book_Name VARCHAR(30),Author VARCHAR(15) PRIMARY KEY)'''

# cursor.execute(data_2)

# query = "INSERT INTO book_category(Books,Author) VALUES(%s,%s)"
# b1 = ('Life ','k_bhagat')
# b2 = ('The Call Of The Wild','P_iran')
# b3 = ('To Kill A MockingBird','G_poll')
# b4 = ('Brave Women','D_smith')
# b5 = ('The Avengers','_B_stokes')
# b6 = ('X-MEN','R_naves')
# b7 = ('The Whistler','W_kane')
# b8 = ('Game Of Thrones','I_starc')
# b9 = ('Drafters','H.ren')
# b10 = ('The Tell-Tale Heart','M_wade')
# cursor.execute(query,b1)
# cursor.execute(query,b2)
# cursor.execute(query,b3)
# cursor.execute(query,b4)
# cursor.execute(query,b5)
# cursor.execute(query,b6)
# cursor.execute(query,b7)
# cursor.execute(query,b8)
# cursor.execute(query,b9)
# cursor.execute(query,b10)
# conn.commit()
# cursor.close()

# query2 = "INSERT INTO book_Authors(Book_Name,Author) VALUES(%s,%s)"
# a1 = ('Life Of Pie','J_smith')
# a2 = ('The Call Of The Wild','Andrew_key')
# a3 = ('To Kill A MockingBird','C_warn')
# a4 = ('Little Women','J_buttler')
# a5 = ('The Avengers','_B_stokes')
# a6 = ('X-MEN','J_roy')
# a7 = ('The Whistler','W_kane')
# a8 = ('Game Of Thrones','R_taylor')
# a9 = ('Dracula','S_kumar')
# a10 =('The Tell-Tale Heart','M_wade')
# cursor.execute(query2,a1)
# cursor.execute(query2,a2)
# cursor.execute(query2,a3)
# cursor.execute(query2,a4)
# cursor.execute(query2,a5)
# cursor.execute(query2,a6)
# cursor.execute(query2,a7)
# cursor.execute(query2,a8)
# cursor.execute(query2,a9)
# cursor.execute(query2,a10)
# conn.commit()
# cursor.close()


# Where query using 'AND' 
# where_query_and = '''(SELECT * FROM book_category WHERE Books='X-MEN' AND Author='R_naves')'''

# using string formatting 
"""where_query_and = "SELECT * FROM book_category WHERE Books='{}' OR Author='{}'".format('Life','k_bhagat')
cursor.execute(where_query_and)

and_query_result = cursor.fetchall()
for i in and_query_result:
    print(i)"""



# Where query using 'OR' 
"""where_query_or = '''(SELECT * FROM book_category WHERE Books='X-MEN' OR Author='D_smith')'''

cursor.execute(where_query_or)

or_query_result = cursor.fetchall()
for i in or_query_result:
    print(i)
"""



#INNER Join using python
"""join_query= "Select book_category.Books ,book_Authors.Book_Name from book_category JOIN book_Authors ON book_category.id=book_Authors.id"
cursor.execute(join_query)
join_result= cursor.fetchall()
for i in join_result:
    print(i)"""