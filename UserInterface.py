import mysql.connector, time

db_handle = mysql.connector.connect
(
    host = 'localhost',
    user = 'root',
    password = '1234'
)

print(db_handle)

cursor = db_handle.cursor()

names = []

file = open ("HotelRooms.txt", "r")

for x in file.readline();
    names.append(x)

for y in names:
    cursor.execute("Create Database " + y)
    time.sleep(1)