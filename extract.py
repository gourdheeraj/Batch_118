import json
with open("product.json","r") as file:
    python_data=json.load(file)
    print(python_data["id"])
    print(python_data["title"])
    print(python_data["description"])
    print(python_data["tags"])
    
import pymysql
import json
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="product_db"
)

cursor = conn.cursor()

with open("product.json", "r") as file:
    data = json.load(file)
