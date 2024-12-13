import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="adithi"
)

print(mydb)
import mysql.connector as mycon

# Establish the connection
con = mycon.connect(host='localhost', user='root', password="adithi") 
cur = con.cursor() 

# Create database and table if they don't exist
cur.execute("CREATE DATABASE IF NOT EXISTS restaurant") 
cur.execute("USE restaurant")
cur.execute("""
    CREATE TABLE IF NOT EXISTS booking (
booking_id INT AUTO_INCREMENT PRIMARY KEY,
customer_nameVARCHAR(50),
table_number INT,
booking_time DATETIME
    )
""")
con.commit() 


def add_record():
customer_name = input("Enter Customer Name: ")
table_number = int(input("Enter Table Number: "))
booking_time = input("Enter Booking Time (YYYY-MM-DD HH:MM:SS): ")
    query = "INSERT INTO booking (customer_name, table_number, booking_time) VALUES (%s, %s, %s)"


con.commit()
print("## Data Saved ##")

def display_records():
    query = "SELECT * FROM booking"
cur.execute(query)
    result = cur.fetchall()
print(f"{'Booking ID':<12} {'Customer Name':<25} {'Table Number':<15} {'Booking Time':<20}")
    for row in result:
        print(f"{row[0]:<12} {row[1]:<25} {row[2]:<15} {row[3]:<20}")

def update_record():
booking_id = int(input("Enter Booking ID to update: "))
customer_name = input("Enter New Customer Name: ")
table_number = int(input("Enter New Table Number: "))
booking_time = input("Enter New Booking Time (YYYY-MM-DD HH:MM:SS): ")
    query = """
        UPDATE booking
        SET customer_name = %s, table_number = %s, booking_time = %s
        WHERE booking_id = %s
    """
cur.execute(query, (customer_name, table_number, booking_time, booking_id))
con.commit()
    if cur.rowcount:
print("## Record Updated ##")
    else:
print("## No Record Found with Given ID ##")

def delete_record():
booking_id = int(input("Enter Booking ID to delete: "))
    query = "DELETE FROM booking WHERE booking_id = %s"
cur.execute(query, (booking_id,))
con.commit()
    if cur.rowcount:
print("## Record Deleted ##")
    else:
print("## No Record Found with Given ID ##")

choice = None 
while choice != 0: 
print("1. ADD RECORD") 
print("2. DISPLAY RECORDS") 
print("3. UPDATE RECORD") 
print("4. DELETE RECORD") 
print("0. EXIT") 
    choice = int(input("Enter Choice: ")) 

    if choice == 1: 
add_record()
elif choice == 2: 
display_records()
elif choice == 3: 
update_record()
elif choice == 4: 
delete_record()
elif choice == 0: 
con.close() 
print("## Bye!! ##") 
    else: 
print("## INVALID CHOICE ##")




