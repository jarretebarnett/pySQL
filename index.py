import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PW = os.environ.get("PW")
DB = os.environ.get("DB")

db = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PW,
    database = DB
)

mycursor = db.cursor()

# SELECTION SYNTAX

# SELECT FROM actor TABLE JOINING film actor TABLE ON actor_id, RIGHT JOINING title WITH film TABLE ON film_id.
mycursor.execute("SELECT a.actor_id, a.first_name, a.last_name, fa.film_id, f.title FROM actor AS a INNER JOIN film_actor AS fa ON a.actor_id = fa.actor_id RIGHT JOIN film AS f ON fa.film_id = f.film_id")

# SELECT FROM actor ORDER BY actor_id
mycursor.execute("SELECT actor_id, first_name, last_name FROM actor ORDER BY actor_id")

# SELECT FROM CREATED VIEW
mycursor.execute("SELECT * FROM staff_public")

# SELECT TABLE AND ORDER BY
mycursor.execute("SELECT actor_id, first_name, last_name FROM actor ORDER BY first_name")

# SELECT row(s) FROM TABLE by WHERE
mycursor.execute("SELECT * FROM customer WHERE first_name = 'GREG'")

# Loop through database rows when printed
for x in mycursor:
    print(x)





# INSERTION SYNTAX

# INSERT VALUES INTO TABLE
mycursor.execute("INSERT INTO actor VALUES (203,'MICHAEL','STEVENSON','2006-02-15 04:34:33')")

# INSERT MANY VALUES INTO TABLE
sql = "INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES (%s, %s, %s, %s)"
val = [
    (201,'FORREST','MYERS','2006-02-15 04:34:33'),
    (202,'ROLAND','HESS','2006-02-15 04:34:33'),
    (203,'COURTNEY','DOUGLAS','2006-02-15 04:34:33'),
    (204,'TARA','ELAM','2006-02-15 04:34:33')
]

mycursor.executemany(sql, val)

# COMMIT INSERTS, DELETES, and UPDATES
db.commit()

# Console print for successful INSERT
print(mycursor.rowcount, "record insertion(s) successful")





# CREATION SYNTAX

# CREATE TABLE of choice
mycursor.execute("CREATE TABLE producer (prod_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, first_name VARCHAR(45), last_name VARCHAR(45), film_id SMALLINT UNSIGNED NOT NULL, PRIMARY KEY (prod_id, film_id))")

# COMMIT INSERTS, DELETES, and UPDATES
db.commit()





# UPDATE / ALTER SYNTAX

# UPDATE TABLE
mycursor.execute("UPDATE staff SET first_name = 'Jonathan' WHERE first_name = 'Jon'")

# ALTER TABLE of choice
mycursor.execute("ALTER TABLE producer ADD COLUMN prod_company VARCHAR(50)")

# COMMIT INSERTS, DELETES, and UPDATES
db.commit()

# Console print for successful UPDATE
print(mycursor.rowcount, "record update(s) successful")





# DELETION SYNTAX

# DELETE record
mycursor.execute("DELETE FROM language WHERE name = 'Mandarin'")

# COMMIT INSERTS, DELETES, and UPDATES
db.commit()

# Console print for successful DELETE
print(mycursor.rowcount, "record deletion(s) successful")