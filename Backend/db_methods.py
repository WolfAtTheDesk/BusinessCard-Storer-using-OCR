"""
This file holds methods used to query the PostGresDB
Title:OCR
File Location: OCR/Backend/db_methods.py
"""
import psycopg2

conn = psycopg2.connect(database="business_cards",
                        host="localhost",
                        user="postgres",
                        password="DBcon2")
cursor = conn.cursor()


def insert_into_pdb(data):
    insert_query= ''' insert into cards( name, designation, company, phone, email, website, address, other, image)
                                              values(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

    values= (
            data["Name"][0],
            data["Designation"][0],
            data["Company"][0],
            data["Phone"][0],
            data["Email"][0],
            data["Website"][0],
            data["Address"][0],
            data["Other"][0],
            data["image"][0]
            )
    cursor.execute(insert_query,values)
    conn.commit()
print("done")
