import PyPDF2
import mysql.connector
from fpdf import FPDF
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', 'B', 16)

# Create Table Data 
data = (
("9232","Ganesh","9864573211"),
("9250","Mohit","9988776655"),
("9260","Adarsh","9122334455"),
("9244","Dipak","9988112283"),
("9238","Ankit","9911882238"),
("9231","Aniket","9911812338"),
)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4
for row in data:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)


db = mysql.connector.connect(host="localhost", user='root', password='p@ssw0rd', database='pdfData')

c  = db.cursor()
for i in data:
    c.execute ("INSERT INTO student (Emp_id,Name,phone) VALUES ({},'{}','{}')".format(i[0],i[1],i[2]))

db.commit()

db.close()
print('Done')