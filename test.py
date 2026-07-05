# marks = [94.3,89.9,90.0,66.5,45.2]
# print(marks)
# print(type(marks))
# print(len(marks))

# list=[1,2,3,4]
# list.append(5)
# print(list)

# list=[2,6,4,5,8,6,7,]
# print(list.sort(reverse=True))
# print(list)

# mov=[]

# mov1 = input("enter 1st moive:")
# mov2 = input("enter 2nd moive:")
# mov3 = input("enter 3rd moive:") 
# mov1.append()
# mov2.append()
# mov3.append()
# mov.append

# lists =[10,20,30,40,50]
# lists.remove(30)
# print(lists)
# print(len(lists))


# data = [12, 45, 67, 89, 10]

# for i in data:
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# data = [12, 45, 67, 89, 10]

# for i in data:
#     if i % 2 == 0:
#         print(i)

# marks = [78, 90, 67, 88, 56]
# total=0
# for i in marks:
#     total = total + i
# print(total)

# data = [45, 78, 12, 99, 34, 67]
# print(max(data))
# print(min(data))

# data = [45, 78, 12, 99, 34, 67]

# data.sort()
# print(data[-1])

 
# l = [1, 2, 3]
# res = l * 3
# print(res)

# def duplicate_list(lst):
#     return lst * 3

# l = [1, 2, 3]

# result = duplicate_list(l)
# print(result)

# def second_function(lst):
#     lst.sort()
#     return lst[-2]
# data = [89, 23, 24, 2, 55, 54, 64]

# lst = [89, 23, 24, 2, 55, 54, 64]
# lst.sort()
# res = lst[-2]
# print(res)

# lst =[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# lst.reverse()
# print(lst)

# lst = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] 
# lst.sort()
# print(lst)

# lst = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] 
# lst.sort(reverse=True)
# print(lst)

# string = ["Dreamer", "infotech"]
# new_str=""
# for i in string:
#     for j in i:
#         if j.lower() in "aeiou":
#             new_str += j
        
# print(new_str)

# data = []
# for i in range(5):
#     element = int(input("enter element"))
#     data.append(element)

# print(data)  

# numbers=[i for i in range(10,0,-1)]
# print(numbers) 

# numbers=[i**2 for i in range(10,0,-1)]
# print(numbers) 

# numbers=[i for i in range(1,11) if i%2==0]
# print(numbers) 

# language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']

# letter = input("Enter a letter: ")

# result = [i for i in language if letter in i]

# print(result)

# lst =[[1,2], [3,4], [5,6]] 
# lst2=[]
# for i in lst:
#     for j in i:
#         lst2.append(j)
# print(lst2)

# lst=[1, 2, 2, 3, 4, 1, 5, 2]
# l =[]

# for i in lst:
#     lst.count(l)
# print(i,":times")

# emp_name=["dheeraj","rahul"]
# for i in emp_name:
#     print(i.upper()) 

# str1="this is python"
# v = "aeiou"
# res =""
# for i in range(len(str1)):
        
#         res+=i
# print(res)

# lst = [12,3,4,34,56,76,766,]
# large = [0]
# for i in lst:
#     if large < i:
#         large = i
# print(large)

# numbers=[i for i in range(10,0,-1)]
# # print(numbers) 
# str1=["python programming"]
# str1.reverse=True()

# s = "python programming"

# for ch in s:
#     if ch == 'h' or ch == 'm':
#         continue
#     print(ch, end="")

n1=3
n2=5
n3=7
if n1%2!=0:
    print("odd",n1)
if n2%2!=0:
    print("odd",n2)
if n3%2!=0:
     print("odd",n3)


lis=["rahul"]
str1=str(lis)
res=str1.reverse()
print(res)