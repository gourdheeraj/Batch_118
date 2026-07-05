#Basic Variable Swapping 
# 1. Switch values of two integers 
# Input:  
# n1 = 20, 
# n2 = 30 
# Output:  
# n1 = 30 
# n2 = 20
# n1 = 20
# n2 = 30
# print("after swapping",n1,n2)
# z=n1
# n1=n2
# n2=z
# print("before swappind",n1,n2)

# 2. Switch values of two strings (characters) 
# Input: 
# char1 = "hello" 
# char2 = "java" 
# Output:  
# char1 = "java" 
# char2 = "hello"

# char1 = "hello" 
# char2 = "java" 
# print("after swapping",char1,char2)
# char=char1
# char1=char2
# char2=char
# print("before swapping",char1,char2)

# . Update balance after deposit 
# Initial balance: current_balance = 10000 
# Deposit amount: deposit_balance = 5000 
# Output: 
# ○ Before deposit: current_balance = 10000 
# ○ After deposit: current_balance = 15000

# current_balance=10000
# deposite_balance=5000
# print("before deposite",current_balance)
# current_balance = current_balance + deposite_balance
# print("after deposite",current_balance)

#  Update balance after withdrawal 
# Before: balance = 12000 
# Withdrawal: 3000 
# After: ?
# balance=12000
# withdrawal=3000
# print("before withdrawal",balance)
# balance=balance-withdrawal
# print("after withdrawal",balance)

#  Increase shopping cart items by 3 
# Before: cart_items = 5 
# After: ?
# cart_item=5
# print("brfore cart item",cart_item)
# cart_item=cart_item+3
# print("after cart item",cart_item)

#   Apply a 20% discount to a price 
# Before: price = 1000 
# After: ?

# price=1000
# print("before price",price)
# discount =price*20/100
# print("after discount",discount)

# Calculate student percentage 
# Input: obtain_marks = 430, out_of = 500 
# Output: Percentage =?

# obtain_marks = 430
# out_of = 500

# percentage = (obtain_marks / out_of) * 100

# print("Percentage =", percentage, "%")

# 10. Calculate total and average of 4 subjects 
# Input Example: 
# subject_1 =int(input("enter subject 1 :")) 
# subject_2=int(input("enter subject 2 :")) 
# subject_3=int(input("enter subject 3 :")) 
# subject_4=int(input("enter subject 4 :")) 

# total = subject_1+subject_2+subject_3+subject_4
# avg = total/4
# print(total)
# print(avg)

# 11. Calculate average of 3 numbers 
# Input: num1 = 25, num2 = 35, num3 = 45 
# Output: Average = ? 

# num1=int(input("enter number 1 :"))
# num2=int(input("enter number 2 :"))
# num3=int(input("enter number 3 :"))

# total=num1+num2+num3
# avg = total/3
# print(total)
# print(avg)

# 12. Calculate profit or loss percentage 
# Input: cost_price = 500, selling_price = 600 
# Output: Profit or Loss = ?

# cost_price=int(input("enter cost price :"))
# selling_price=int(input("enter selleing price :"))

# profit=selling_price-cost_price
# loss=cost_price-selling_price
# print(profit)
# # print(loss)
# 13. Calculate simple interest 
# Input: principal = 10000, rate = 5, time = 2 
# Output: Simple Interest = ?

# principle =10000
# rate=5
# time=2
# simple_interest=principle*rate*time/100
# print(simple_interest)

# 14. Calculate compound interest 
# Input: principal = 10000, rate = 5, time = 2 
# Output: Compound Interest = ?

# principle=1000
# rate=5
# time=2

# amount = principle * (1 + rate / 100) ** time
# compound_interest = amount - principal

# print("Compound Interest =", compound_interest)
# 15. Calculate tax on income 
# Input: income = 500000, tax_rate = 10 
# Output: Tax = ? 

# income=500000
# tax_rate=10
# tax = income*tax_rate/100
# print(tax)

# 16. Calculate percentage increase or decrease 
# Input: initial_value = 200, final_value = 250 
# Output: Percentage Change = ? 

# intial_value=200
# final_value=250

# percentage_change=final_value-intial_value/intial_value*100
# print(percentage_change)
# 17. Convert boolean to integer 
# Input: True 
# Output: ?
# boolean=True
# output=int(boolean)
# print(output)
# print(type(output))
# 18. Convert float to string 
# Input: 45.67 
# Output: ?
# input=45.67
# print(str(input))
# print(type(str(input)))

# 19. Convert 20°C to Fahrenheit 
# Input: 20°C 
# Output: ?
# celsius=20
# fahrenheit = (9/5 * celsius) + 32
# print(fahrenheit)

# 0. Convert 50°F to Celsius 
# Input: 50°F 
# # Output: ? 
# fahrenheit=50
# celsius=(5/9)*(fahrenheit-32)
# print(celsius)



# 32.If user input is: 
# Name: Dev 
# Age: 25 
# City: Jaipur 
# Hobby: Cooking 
# Then Output is : 
# Meet Dev, a 25-year-old enthusiast from Jaipur. 
# When not busy with daily tasks, Dev loves spending time cooking. 
# Life in Jaipur keeps Dev energetic and curious every single day. 
# With coding as a passion, the future looks creative and inspiring for 
# Dev in the Jaipur City.

# name=input("enter name :")
# age=input("enter age:")
# city=input("enter city:")
# hobbies=input("enter hobbies")

# print(f"""meet {name},a {age}year old enthusiast from {city}.
#       when in {city} keeps {name} """)



# 33.Create a Python program that asks the user for the following: 
# ● Full Name 
# ● Profession 
# ● Favorite Quote 
# ● Years of Experience 
# Output format: ------------------------------------------------ 
# Name        
# : <Full Name> 
# Profession  : <Profession> 
# Experience  : <Years of Experience> 

# full_name = input("Enter Full Name: ")
# profession = input("Enter Profession: ")
# quote = input("Enter Favorite Quote: ")
# experience = input("Enter Years of Experience: ")

# print("-" * 50)
# print("Name        :", full_name)
# print("Profession  :", profession)
# print("Experience  :", experience)
# print("Quote       :", quote)