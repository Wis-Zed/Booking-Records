import sqlite3

conn = sqlite3.connect("roombookings.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS rooms
                  (room_ID TEXT,
                  roomname TEXT,
                  roomprice INTEGER,
                  primary key(room_ID))
               """)

           
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (mem_id TEXT,
                  usertype TEXT,
                  firstname TEXT,
                  surname TEXT,
                  email TEXT,
                  telephone TEXT,
                  password TEXT,
                  primary key(mem_id))
              """)


cursor.execute("""CREATE TABLE IF NOT EXISTS bookings
                  (booking_id INTEGER,
                  room_ID TEXT,
                  mem_ID TEXT, 
                  time TIME,
                  date DATE,
                  price INTEGER, 
                  paid TEXT,
                  primary key (booking_id),
                  foreign key(room_ID) references rooms(room_ID),
                  foreign key(mem_ID) references users(mem_ID))
              """)
                  



