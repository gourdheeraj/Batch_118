# #  file=It is typically a corrupted version of De finibus bonorum et malorum, 
# # a 1st-century BC text by the Roman statesman and philosopher Cicero, with words altered, added, and removed to make it nonsensical and improper Latin.
# # [not in body] The first two words are the truncation of dolorem ipsum ("pain itself").
# # # Lorem ipsum's purpose is to permit a page layout to be designed, independently of the copy that will subsequently populate it,
# # # or to demonstrate various fonts of a typeface without meaningful text that could be distracting.

# # with open("sample.txt", "r") as file:
# #     data = file.read()

# # data = "".join(ch for ch in data if not ch.isdigit())

# # with open("sample.txt", "w") as file:
# #     file.write(data)
# # with open("demo.txt","r") as f:
# #     r=f.read()
# #     print(r)
# # with open("demo.txt","w+") as file:
# # file.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# #         Lorem Ipsum has been the industry's standard dummy text ever since 1966, 
# #         when designers at Letraset and James Mosley, 
# #         the librarian at St Bride Printing Library in London, 
# #         took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. 
# #         It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. 
# #         It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.""")
# # file.seek(0)
# #  r=file.read()
# #     with open("newdemo.txt", "w+") as newfile:
# #         for i in r:
# #             if i in "0123456789":
# #                 newfile.write("")
# #             else:
# #            newfile.write(i)




# # import json
# # import pymysql

# # # Step 1: Connect MySQL Server
# # connection = pymysql.connect(
# #     host="localhost",
# #     user="root",
# #     password="root"
# # )

# # cursor = connection.cursor()

# # # Step 2: Create Database
# cursor.execute("CREATE DATABASE IF NOT EXISTS product_db")

# # Step 3: Use Database
# cursor.execute("USE product_db")

# # Step 4: Create Table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products(
#     id INT PRIMARY KEY,
#     title VARCHAR(255),
#     description TEXT,
#     category VARCHAR(100),
#     price DECIMAL(10,2),
#     discountPercentage DECIMAL(5,2),
#     rating DECIMAL(3,2),
#     stock INT
# )
# """)

# print("Database and Table Created Successfully")

# # Step 5: Read JSON File
# with open("product.json", "r") as file:
#     data = json.load(file)

# # Step 6: Insert Data into Table
# query = """
# INSERT INTO products
# (id,title,description,category,price,discountPercentage,rating,stock)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
# """

# for product in data["products"]:
#     values = (
#         product["id"],
#         product["title"],
#         product["description"],
#         product["category"],
#         product["price"],
#         product["discountPercentage"],
#         product["rating"],
#         product["stock"]
#     )

#     cursor.execute(query, values)

# connection.commit()

# print("All Products Inserted Successfully")

# # Close Connection
# cursor.close()
# connection.close()