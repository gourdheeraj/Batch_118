# 1. Task: Calculate Profit Percentage 
# ● Write a program that takes input for the cost price and selling price of an item. 
# ● Hints 
# ○ Prompt the user to input the cost price and selling price. 
# ○ Determine whether the transaction resulted in a profit or loss. 
# ○ If there is a profit calculate the profit percentage; if there is a loss 
# calculate the loss percentage. 
# ○ Display the profit or loss and the respective percentage.

# cost_price=int(input("enter cost price :"))
# selling_price=int(input("enter selling price :"))

# if selling_price > cost_price:
#     profit=selling_price-cost_price
#     print("profit :",profit)
# elif selling_price<cost_price:
#      loss=cost_price-selling_price
#      print("loss",loss)
# else:
#      print("no loss on profit")
#--------------------------------------------------------------------------------------------------------
# 2. Task: Cricket Stats Analyzer 
# ● Objective: Write a script to analyze cricket stats for a team. 
# ● Hints: 
# ○ Prompt the user to input the runs scored by each of the five players in a 
# cricket match. 
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they 
# scored. 
# ○ Calculate the total runs scored by all players and the average runs. 
# ○ Display the total runs and average runs to the user.

# player1=int(input("run scored player1:"))
# player2=int(input("run scored player2:"))
# player3=int(input("run scored player3:"))
# player4=int(input("run scored player4:"))
# player5=int(input("run scored player5:"))
# total=player1+player2+player3+player4+player5
# avg=total/5
# print("total:",total)
# print("average:",avg)
#--------------------------------------------------------------------------------------------------------
# 3. Task: Retirement Age Calculator 
# ● Objective: Write a program that prompts the user for their age and tells them how 
# many years until they reach retirement age (65). 
# ● Hints: 
# ○ Ask the user to input their age. 
# ○ Calculate how many more years they have until they reach 65 years of 
# age. 
# ○ Display the number of years left until retirement or a message if the user 
# has already reached retirement age.

# age=int(input("enter age"))
# left_year=65-age
# if age>=65:
#     print("you have already reach retriment age")
# else:
#     print("year left until retriment:",left_year)
#-------------------------------------------------------------------------------------------------------

# 4. Task: Calculate the Area of a Circle 
# ● Objective: Write a program to calculate the area of a circle. 
# ● Hints: 
# ○ Ask the user to input the radius of the circle. 
# ○ Calculate the area of the circle using the formula: Area = π * 
# radius^2. 
# ○ Display the calculated area

# radius=int(input("enter radius:"))
# area=3.14*radius**2
# print("area of circle:",area)
#-----------------------------------------------------------------------------------------------------------
# 5. Task: Salary Calculation 
# ● Objective: You have to calculate an employee's salary by computing the gross 
# salary tax and net salary based on the given parameters. 
# ● Hints: 
# ○ Base Salary = ₹50000 
# ○ Bonus = ₹5000 
# ○ Tax Rate = 10%  
# ○ Other Charges = ₹2000 
# Display the Gross Salary Tax and Net Salary

# base_salary=50000
# bonus=5000
# tax_rate=10
# other_charges=2000
# gross_salary=base_salary+bonus
# tax = gross_salary*tax_rate/100
# net_salary = gross_salary-tax_rate-other_charges
# print("gross salary",gross_salary)
# print(tax)
# print("net salary:",net_salary)
#---------------------------------------------------------------------------------------------------------
# 6. Task: Bank Loan Approval System applican
# ● Objective: You have to create a javascript script that checks whether an user is 
# eligible for a bank loan based on various criteria. 
# ● Hints: 
# ○ The applicant's age must be between 18 and 60 years. 
# ○ The applicant's monthly income must be greater than or equal to ₹25000. 
# ○ The applicant's credit score must be greater than or equal to 700. 
# ○ The applicant must not have any outstanding debts greater than ₹10000 
# 1. Output: 
# ○ Display "Loan Approved" if the applicant meets all the conditions. 
# ○ Otherwise display "Loan Rejected".

# age=int(input("enter applicant age : "))
# monthly_income=int(input("enter applicant monthly income :"))
# credit_score=int(input("applicant credit score :"))
# debts=int(input("applicant outstnding :"))
# if age>=18 and age<=65 and monthly_income>=25000 and credit_score>=700 and debts<=10000:
#     print("laon apporved")
# else:
#     print("loan rejected")
#----------------------------------------------------------------------------------------------------------
# 7. Task: Students Interview Eligibility Checker 
# ● Objective:you have to design a python script that checks whether a student is 
# eligible for an interview based on their academic score attendance percentage 
# and extracurricular participation. 
# ● Input: 
# ○ Academic Score (percentage): A floating-point number representing the 
# student's academic score. Ex .78.88 
# ○ Attendance Percentage: A floating-point number representing the 
# student's attendance percentage. Ex.85.88 
# ○ Extracurricular Participation: This indicates whether the student has 
# participated in any extracurricular activities. Ex.Yes/no 
# Conditions for Interview Eligibility: 
# 1. The student’s academic score must be 60 or above. 
# 2. The student’s attendance percentage must be 75 or above. 
# 3. The student should have participated in at least one extracurricular activity. 
# Output: 
# ● If the student meets all three conditions print "Eligible for Interview". 
# ● If the student fails to meet any of the conditions print "Not Eligible for Interview".

# academic_score=float(input("student's acadmic score :"))
# attendace_percentage=float(input("student's attendance percentage :"))
# if academic_score>=60 and attendace_percentage>=75:
#     print("eligible for interview")
# else:
#     print("Not Eligible for Interview")
#---------------------------------------------------------------------------------------------------------
# 8. Task: Validating Email Domain 
# ● Objective: You will implement a python program to validate the domain of a 
# user's email address. The program will check if the email contains a specific 
# domain (e.g. "gmail.com"). 
# Problem Statement: 
# You are building a registration system that only accepts email addresses from a certain 
# domain (e.g. "gmail.com"). Your task is to: 
# 1. Prompt the user to enter their email address. 
# 2. Check if the entered email address contains the domain "gmail.com". 
# 3. Display whether the email is eligible for registration based on the domain 
# check. 
# 4. Print a message to inform the user if their email is eligible for registration 
# or not. 

# email=input("enter email :")
# if "gmail.com" in email:
#     print("eligible for registration ")
# else:
#     print("not eligible for registration ")
#---------------------------------------------------------------------------------------------------------
# 10.Task : Student Grading System 
# Create a javascript program to calculate a student's grade based on their marks. 
# Task: 
# 1. Input: Prompt the user to enter their marks. 
# 2. Criteria: 
# ○ Grade A: 90–100 
# ○ Grade B: 80–89 
# ○ Grade C: 70–79 
# ○ Grade D: 60–69 
# ○ Grade E: 50–59 
# ○ Grade F: 0–49 
# ○ Invalid marks: Outside the range 0–100. 
# 3. Output: Display the grade or an error message for invalid marks. 
# Example Outputs: 
# ● Marks: 85 → Grade: B 
# ● Marks: 45 → Grade: F 
# ● Marks: 105 → Invalid marks.

# marks=int(input("enter marks :"))
# if marks>=90:
#     print("grade A")
# elif marks>=80:
#     print("grade B")
# elif marks>=60:
#     print("grade C")
# elif marks>=50:
#     print("grade D")
# else:
#     print("fail")
# #--------------------------------------------------------------------------------------------------------------
# 11.Task : Authentication System. 
# Write a javascript program that authenticates a user by checking their username and 
# password. The program should compare the entered credentials with predefined valid 
# credentials. 
# ● Predefined valid usernames and corresponding passwords 
# username1 = "user1"  
# username1_password1 = "pass@123"
# Instructions: 
# 1. Input: 
# ○ Prompt the user to input their username and password. 
# 2. Processing: 
# ○ Check if the username and password match  
# 3. Output: 
# ○ If both the username and password match the predefined valid credentials 
# display "Authentication successful." 
# ○ If either the username or the password does not match display 
# "Authentication failed." 
# user_name=input("enter username:")
# password1=input("enter password:")

# if user_name=="user" and password1=="pass@123":
#     print("authentication successful")
# else:
#     print("authencation failed")
#-------------------------------------------------------------------------------------------------------
# 12.Employee Salary Based on Experience. 
# You are building a system for a Human Resources (HR) department that calculates an 
# employee's salary based on their years of experience. The system assigns salary tiers 
# based on the number of years an employee has been working. It also offers bonuses for 
# employees who have more than 15 years of experience. 
# Scenario Breakdown: 
# Context 1: Senior Employee 
# ● An employee with 10 or more years of experience is classified as a Senior 
# Employee. The base salary for such an employee is 80000. 
# ● If the employee has more than 15 years of experience they receive a bonus of 
# 5000 to their salary. 
# Example: 
# An employee with 18 years of experience: 
# ● They are classified as Senior Employees. 
# ● Their base salary is 80000. 
# ● Since they have more than 15 years of experience they receive an additional 
# 5000 bonus. 
# ● The final salary is 85000. 
# Context 2: Mid-Level Employee 
# ● Employees with 5 to 9 years of experience are classified as Mid-Level 
# Employees. 
# ● Their base salary is 50000 with no bonus. 
# Example: 
# An employee with 7 years of experience: 
# ● They are classified as a Mid-Level Employee. 
# ● Their base salary is 50000. 
# ● Since they have fewer than 10 years of experience no bonus is added. 
# ● The final salary is 50000. 
# Context 3: Junior Employee 
# ● Employees with less than 5 years of experience are classified as Junior 
# Employees. 
# ● Their base salary is 30000 with no bonus. 
# Example: 
# An employee with 3 years of experience: 
# ● They are classified as Junior Employees. 
# ● Their base salary is 30000. 
# ● No bonus is added. 
# ● The final salary is 30000. 
# Output Examples: 
# Senior Employee with 18 years of experience: 
# Enter years of experience: 18 
# Senior employee 
# Experience exceeds 15 years. Bonus added. 
# Salary: 85000 
# Mid-Level Employee with 7 years of experience: 
# Enter years of experience: 7 
# Mid-level employee 
# Salary: 50000 
# Junior Employee with 3 years of experience: 
# Enter years of experience: 3 
# Junior employee 
# Salary: 30000 
 
# experience=int(input("enter year of experiance :"))
# if experience >= 10:
#     salary=85000
#     if experience >= 15:
#         salary += 5000
#         print("seinor employee")
#         print("salary=",salary)
#     elif experience >= 5:
#         salary =50000
#         print("mid level employee")
#         print("salary=",salary)
#     else:
#         salary=30000
#         print("junior employee")
#         print("salary",salary)
#--------------------------------------------------------------------------------------------------------
# 13. Library Charge Calculation 
# Problem Statement: 
# Write a javascript program that calculates the library charge based on the number of days a 
# book has been borrowed. 
# Charge Criteria
# ● Up to 5 days: Rs. 2 per day 
# ● 6 to 10 days: Rs. 3 per day 
# ● 11 to 15 days: Rs. 4 per day 
# ● More than 15 days: Rs. 5 per day 
# Instructions: 
# 1. Input: Prompt the user to enter the number of days the book has been borrowed. 
# 2. Processing: Calculate the charge based on the given criteria. 
# 3. Output: Display the calculated charge.

# days = int(input("number of days :"))
# if days<=5:
#     charge=days*3
# elif days<=10:
#     charge=days*3
# elif days<=15:
#     charge=days*4
# else:
#     charge=days*5
# print(charge)
#----------------------------------------------------------------------------------------------
# 14. Arranging Three Numbers in Descending Order 
# Task: 
# Write a javascript program to arrange three numbers in descending order. 
# Input: 
# Prompt the user to enter three numbers. 
# Processing: 
# Sort the numbers in descending order. 
# Example: 
# ● Enter first number: 3 
# ● Enter second number: 1 
# ● Enter third number: 2 
# Output: 
# ● Numbers in Descending Order: 3, 2, 1 

# n1=int(input("enter number 1 )
