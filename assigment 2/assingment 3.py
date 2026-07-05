# # 1. Write a Python program to print all odd and even numbers from 1 to 20.
# for i in range(1,21):
#     print(i)
#---------------------------------------------------------------------------------------
# # 2. Write a Python program to generate all multiples of 12.
# for i in range(1,11):
#     print(i*12)
#---------------------------------------------------------------------------------------
#3. Write a Python program to generate a table of a number provided by the user.
# num=int(input("enter number: "))
# for i in range (1,11):
#     print(num,"x",i,"=",num*i)
#---------------------------------------------------------------------------------------
# # 4.Write a Python program to check if a number provided by the user is prime or not.

# num=int(input("enter number"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
#------------------------------------------------------------------------------------------
#5.. Write a Python program to calculate the sum of numbers between a starting and 
# ending point provided by the user.

# start=int(input("starting point :"))
# end=int(input("ending point :"))
# total =0
# for i in range(start,end+1):
#     total+=i
# print("sum :",total)
#----------------------------------------------------------------------------------------------
# 6. Write a Python program to calculate the product of numbers between a starting 
# and ending point provided by the use

# start=int(input("starting point :"))
# end=int(input("ending point :"))
# total=1
# for i in range(start,end+1):
#     total=i*total
# print("product :",total)
#------------------------------------------------------------------------------------------------
#7. Write a Python program to generate the Fibonacci sequence up to a specified 
# # number of terms.
# num =int(input("number of terms :"))
# a=0
# b=1
# for i in range(num):
#      print(a, end=" ")
#      c = a + b
#      a = b
#      b = c
#----------------------------------------------------------------------------------------------------
#8. Write a Python program to calculate the factorial of a number provided by the 
# user. 
# import math
# n=int(input("enter number :"))
# print(math.factorial(n))

# n=int(input("enter number:"))

# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
#--------------------------------------------------------------------------------------------------
# #9. Write a Python program to find the greatest character from the string "python".

# string="python"

# greatest=max(string)

# print(greatest)

# string="dheeraj"
# greatest=string[0]
# for ch in string:
#     if ch > greatest:
#         greatest=ch
# print(greatest)
#--------------------------------------------------------------------------------------------------
#10. Write a Python program to display all letters except 'm' and 'i' from the string 
# "Dreamer infotech".

# string="dreamer infotech"
# for ch in string:
#     if ch!='m' and ch!='i':
#         print(ch,end="")

# string="dheeraj gour"
# for ch in string:
#     if ch!='d' and ch!='o':
#         print(ch,end=" ")
#------------------------------------------------------------------------------------------------
# 11. Write a Python program to print alternate characters from a given string.
# string="dheeraj gour"
# print(string[: :2])

# string="dheeraj gour"

# for i in range(0,len(string),2):
#     print(string[i],end="")
#------------------------------------------------------------------------------------------------
#  12. Write a Python program to reverse a string entered by the user.

# string="this is python"
# res=""
# for i in range(len(string)-1,-1,-1,):
#     res=res+(string[i])
# print(res)
#---------------------------------------------------------------------------------------------------
#13. Write a Python program to count the total number of characters in a string 
# entered by the user.

# string=input("enter string :")
# count=0
# for i in string:
#     count=count+1
# print(count)
# #----------------------------------------------------------------------------------------------------
# start=int(input("start number :"))
# end=int(input("end number :"))
# sum=0
# for i in range(start,end+1):
#     sum=sum+i
# print(sum)

# start=int(input("start number :"))
# end=int(input("end number :"))
# product=1
# for i in range(start,end+1):
#     product=product*i
# print(product)
#----------------------------------------------------------------------------------------------------------------
# sum=0
# for i in range(0,11,2):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# sum=0
# for i in range(1,21,2):
#         sum=sum+i
# print(sum)
#-------------------------------------------------------------------------------------------------------
# multiple=0
# for i in range(1,50):
#     if i%5==0:
#         multiple=multiple+i
# print(multiple)
#--------------------------------------------------------------------------------------------------------
# for i in range(1,11):
#         print(i,"->",i*i)
    

# num=int(input("enter number"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
#---------------------------------------------------------------------------------------------------------
# count = 0

# for i in range(1, num + 1):

# if num % i == 0:

# count = count + 1
# num=int(input("enter number"))
# count=0
# for i in range(1,num+1):
#     if num%2==0:
#         count=count+1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

#-------------------------------------------------------------------------------------
# str1="dheeraj"
# for i in str1:
#     print(i)
#-------------------------------------------------------------------------------------