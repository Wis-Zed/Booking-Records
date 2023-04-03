import sqlite3

def query(sql, data):
    conn = sqlite3.connect("roombookings.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON") 

    cursor.execute(sql, data)
    conn.commit()

def insert_into_rooms(records):
    sql = "insert into rooms(room_id, roomname, roomprice) values (?, ?, ?)"
    for record in records:
        query(sql, record)

def insert_into_users(records):
    sql = "insert into users(mem_id, usertype, firstname, surname, email, telephone, password) VALUES (?,?,?,?,?,?,?)"
    for record in records:
        query(sql, record) 


def insert_into_bookings(records):
    sql = "insert into bookings(room_ID, mem_ID, time, date, paid) VALUES (?,?,?,?,?)"
    for record in records:
        query(sql, record)


if __name__ == "__main__":

    conn = sqlite3.connect("roombookings.db")
    cursor = conn.cursor()

##    rooms = [("1A","Community room","36" ), ("2A", "Sports hall","39"), ("3A", "Astro Turf (Full Pitch)","59"), ("4A", "Astro Turf (Half Pitch)","39"), ("5A", "Main Hall","39"), ("6A", "Dining Room","39"), ("7A", "Small Meeting Room","20")]
##    insert_into_rooms(rooms)


    users = [("1A34","Staff", "Tom","Smith", "t.rye@stalbans.org", "0734575677", "12345678")]


    insert_into_users(users)

####    bookings = [("2A", "1A34", "11:00", "12/12/2017", "No")]
##    
##
##    insert_into_bookings(bookings)
##
####
## 
    
    
