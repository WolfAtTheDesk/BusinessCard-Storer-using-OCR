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
    insert_query= ''' insert into cards( name, designation, company, phone, email, website, address, other, image, timestamp)
                                              values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

    values= (
            data["Name"][0],
            data["Designation"][0],
            data["Company"][0],
            data["Phone"][0],
            data["Email"][0],
            data["Website"][0],
            data["Address"][0],
            data["Other"][0],
            data["image"][0],
            data["time"][0]
            )
    cursor.execute(insert_query,values)
    conn.commit()

def insert_into_pdb(data):
    insert_query= '''
            INSERT INTO cards(
                            name, designation, company, phone, email, website, address, other, image, timestamp
                            )
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

    values= (
            data["Name"][0],
            data["Designation"][0],
            data["Company"][0],
            data["Phone"][0],
            data["Email"][0],
            data["Website"][0],
            data["Address"][0],
            data["Other"][0],
            data["image"][0],
            data["time"][0]
            )
    cursor.execute(insert_query,values)
    conn.commit()

def getlist():
    cursor.execute("SELECT id, name, company, timestamp FROM cards")
    # Fetch all rows as a list of tuples
    rows = cursor.fetchall()
    conn.commit()
    list=[]
    data = [dict(zip([col.name for col in cursor.description], row)) for row in rows]

    for row in data:
        if row['timestamp'] is not None:  # Check if timestamp is not null
            row['timestamp'] = row['timestamp'].strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp
        item = f"{row['id']} | {row['name']} | {row['company']} | {row['timestamp']}"
        list.append(item)

    return list

def fetch_card(card):
    req = card.split()
    print(card)
    cursor.execute("""
      SELECT *
      FROM cards
      WHERE id = %s
    """, (int(req[0]),))
    row = cursor.fetchone()
    conn.commit()
    data = dict(zip([col.name for col in cursor.description], row)) if row else None
    print(data)
    try:
        data['timestamp'] = data['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(e)
    return data

def delete_card(card):
    id = int(card['id'])
    cursor.execute("""DELETE FROM cards WHERE id = %s;""",(id,))
    conn.commit()
    rows_deleted = cursor.rowcount
    return True
