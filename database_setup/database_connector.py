import pymysql.cursors
import pymysql 
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="rootPass",
  database="MealPlan"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myMeals")
# mycursor.execute("SHOW DATABASES")

# mycursor.execute("select * from all_diets")
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE user_diet_preferences (user_id INT NOT NULL, diet_preference VARCHAR(85))")

mycursor.execute("ALTER TABLE users ADD COLUMN currentWeight FLOAT")
mycursor.execute("ALTER TABLE users ADD COLUMN goalWeight FLOAT")
mycursor.execute("ALTER TABLE users ADD COLUMN mainGoal VARCHAR(50)")






