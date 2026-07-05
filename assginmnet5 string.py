# String Basics 
# 1. Filter vowels and consonants from the string "How are you sir".

# text="how are you sir"

# vowels=""
# consonants=""
# for i in text:
#     if i.isalpha():
#         if i.lower() in "aeiouAEIOU":
#             vowels+=i
#         else:
#             consonants+=i

# print("vowels:",vowels)
# print("consonants:",consonants)

#-----------------------------------------------------------------------------------------

#2. Count vowels and consonants in the string "How are you sir". 

# text = "how are you sir"
# vowel_count=0
# consonants_count=0
# for i in text:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowel_count+=1
#         else:
#             consonants_count+=1

# print("vowels count:",vowel_count)
# print("consonants count:",consonants_count)

#--------------------------------------------------------------------------------------
#3. Reverse the string "How are you sir".

# text="how are you sir"
# reverse=""
# for i in text:
#     reverse=i + reverse
# print("reverse string:",reverse)
#-----------------------------------------------------------------------------------
#4. Convert lowercase letters to uppercase in the string "How are you sir".

# text="how are you sir"
# result=""
# for i in text:
#     if i.islower():
#         result+=i.upper()
#     else:
#         result+=i

# print(result)
#-------------------------------------------------------------------------------
#5. Remove duplicate letters from the string "this is python programming 
# place".

# text="this is python programming palce"

# result=""
# for i in text:
#     if i not in result:
#         result+=i

# print(result)
#---------------------------------------------------------------------------------------
# 6. Search for a specific character in the string "this is python  programming place".

# text="this is python programming place"
# character=input("enter specific character :")
# found=False

# for i in text:
#     if i==character:
#         found=True
# if found:
#     print("character found")
# else:
#     print('character not found')
#-----------------------------------------------------------------------------------
# 7. Find the greatest and smallest characters from the string "venugopaliyer".

# text= "venugopaliyer"

# greatest=text[0]
# smallest=text[0]
# for i in text:
#     if i>greatest:
#         greatest=i
#     if i < smallest:
#         smallest=i
# print(greatest)
# print(smallest)
#----------------------------------------------------------------------------------------------

#8.  Count the total occurrences of a specific letter in the string "this is python programming place". 

# text="this is python programming place"

# letter=input("enter character :")

# count=0

# for i in text:
#     if i==letter:
#         count+=1

# print(count)
#------------------------------------------------------------------------------------------------
# 9. Replace "python" with "javascript" in the string "python developer python engineer python holder".

# text="python developer python engineer python holder"

# new_text=text.replace("python","javascript")

# print(new_text)
#--------------------------------------------------------------------------------------------
# 10. Print alternate letters from the string "How are you sir".

# text="how are you sir"

# for i in range(0,len(text),2):
#     print(text[i],end="")
#--------------------------------------------------------------------------------------------
# 11. Convert the string "qwertyuiopasdfghjklzxcvbnm" to "abcdefghijklmnopqrstuvwxyz".

# text="qwertyuiopasdfghjklzxcvbnm"
# result="".join(sorted(text))
# print(result)
#------------------------------------------------------------------------------------
#12. Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome).
# text=input("enter string :")
# reverse=""
# for i in text:
#     reverse=i+reverse
# if text==reverse:
#     print("palindrome")
# else:
#     print("not palindrome")
#-------------------------------------------------------------------------------------------------
#13. Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!".
# text = "Python 3.9 is awesome!!"

# spaces = 0
# digits = 0
# alphabets = 0
# special = 0

# for i in text:
#     if i.isalpha():
#         alphabets += 1
#     elif i.isdigit():
#         digits += 1
#     elif i== " ":
#         spaces += 1
#     else:
#         special += 1

# print("Alphabets:", alphabets)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)
#----------------------------------------------------------------------------------------
#14. Find the longest word in the string "Python programming is interesting".


# text = "Python programming is interesting"

# words = text.split()

# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word:", longest)
# print("Length:", len(longest))
#--------------------------------------------------------------------------------------------
# 15. Capitalize the first letter of each word in "welcome to python world".

# text="welcome to python world"
# print(text.title())
#-----------------------------------------------------------------------------------------
#16. Remove all spaces from "How are you sir".
# text="how are you sir "
# result=" "
# for i in text:
#     if i!=" ":
#         result+=i

# print(result)
#---------------------------------------------------------------------------------------
#17. Check if all characters in the string are unique (e.g., "abcde" → True, "hello" → False).
# text = input("Enter a string: ")

# seen = ""

# unique = True

# for ch in text:
#     if ch in seen:
#         unique = False
#         break
#     seen += ch

# print(unique)
#---------------------------------------------------------------------------------------------
# # 18. Sort characters alphabetically in "programming" → "aggimmnoprr".
# text="programming"
# result="".join(sorted(text))
# print(result)
#--------------------------------------------------------------------------------------------
#19. Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".
# text = "Python Is Fun" 
# result=text.swapcase()
# print(result)
#----------------------------------------------------------------------------------------------
# 20. Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }.

# srt1="banana"
# result={}
# for i in srt1:
#     if i in result:
#         result[i]+=1
#     else:
#          result[i]=1
# print(result)
#-----------------------------------------------------------------------------------------------
#21. Remove vowels from "How are you sir" → "Hw r y sr".

# srt1="how are you sir"
# vowels="aeiouAEIOU"
# result=""
# for i in srt1:
#     if i not in vowels:
#         result+=i
# print(result)
#-------------------------------------------------------------------------------------------------
# 22. Check if a substring exists in "Python programming" (e.g., "thon" → Found).
# str1="python programming"
# res="thon"
# if res in str1:
#     print("found")
# else:
#     print("not found")
#-------------------------------------------------------------------------------------------------
# 23. Print words in reverse order in "How are you sir" → "sir you are How". 
# text="How are you sir"
# def reverse_words(text):
#     word = ""
#     result = ""

#     for ch in text:
#         if ch != " ":
#             word += ch
#         else:
#             result = word + " " + result
#             word = ""

#     result = word + " " + result

#     return result.strip()

# str1 = "How are you sir"
# print(reverse_words(str1))
#------------------------------------------------------------------------------------------------
# 24. Count words in the string ""This is a python assignment. 
# # srt1="This is a python assignment"
# def count_words(text):
#     words = text.split()
#     return len(words)

# str1 = "This is a python assignment"

# print(count_words(str1))
#------------------------------------------------------------------------------------------------
# #25. Find the ASCII value of each character in "ABcd".
# def ascii_value(text):
#     for ch in text:
#         print(ch, "=", ord(ch))

# str1 = "ABcd"

# ascii_value(str1)
#------------------------------------------------------------------------------------------------
# # 26. Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"]).
# str1 = "Python is fun"

# print(str1.split())
#--------------------------------------------------------------------------------------------------
#27. Join a list of words into a string using "join()" (e.g., ["Python", "is", 
# "fun"] → "Python is fun").
# words = ["Python", "is", "fun"]

# print(" ".join(words))
#----------------------------------------------------------------------------------------------
# 28. Find the first non-repeating character in "swiss" → "w".
# str1 = "swiss"

# for i in str1:
#     if str1.count(i) == 1:
#         print(i)
#         break
#------------------------------------------------------------------------------------------------------
#29. Check if two strings are anagrams (e.g., "listen" and "silent" → Anagrams).
# str1 = "listen"
# str2 = "silent"

# if sorted(str1) == sorted(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")
#---------------------------------------------------------------------------------------------
#30. Replace all spaces with hyphens (-) in "Python is easy to learn" → "Python-is-easy-to-learn".
# str1 = "Python is easy to learn"

# print(str1.replace(" ", "-"))
#-----------------------------------------------------------------------------------------------
#31. Extract a substring from "Python Programming" → from index 0 to 6 should give "Python".
# str1 = "Python Programming"

# print(str1[0:6]) 
#-------------------------------------------------------------------------------------------------
# #32. Check if one string is a substring of another (e.g., "gram" is a substring of "Programming"). 
# str1 = "Programming"

# if "gram" in str1:
#     print("Found")
# else:
#     print("Not Found")
#--------------------------------------------------------------------------------------------------
# #33. Find all occurrences of a substring in "This is Python and Python is fun" → Substring "Python".
# str1 = "This is Python and Python is fun"

# index = str1.find("Python")

# while index != -1:
#     print(index)
#     index = str1.find("Python", index + 1)
#---------------------------------------------------------------------------------------------------
# # 34. Replace a substring in "I like Python" → Replace "Python" with "Java".
# str1 = "I like Python"

# print(str1.replace("Python", "Java"))
#-----------------------------------------------------------------------------------------
#35. Remove a substring from "HelloWorld" → Remove "World" → "Hello". 
# str1 = "HelloWorld"

# print(str1.replace("World", ""))
#-------------------------------------------------------------------------------------------------
#36. Count occurrences of a substring in "banana" → Substring "ana" appears 2 times.
# str1 = "banana"

# print(str1.count("ana"))
#-----------------------------------------------------------------------------------------------
#37. Check if a string starts with a substring (e.g., "Python is easy" starts with "Python").
# str1 = "banana"
# sub = "ana"

# count = 0

# for i in range(len(str1) - len(sub) + 1):
#     if str1[i:i+len(sub)] == sub:
#         count += 1

# print(count)
#--------------------------------------------------------------------------------------------------
#38. Check if a string ends with a substring (e.g., "Learn coding" ends with "coding").
# str1 = "Python is easy"

# print(str1.startswith("Python"))
#------------------------------------------------------------------------------------------------
# 39. Split a string based on a substring (e.g., "apple,banana,grapes" → Split by "," → ["apple", "banana", "grapes"]).
# str1 = "apple,banana,grapes"

# print(str1.split(","))
#--------------------------------------------------------------------------------------------------------------
# 40. Find the index of the first occurrence of a substring in "Programming is 
# great" → Substring "is" → Index 12.
# str1 = "Programming is great"

# print(str1.find("is"))
#-------------------------------------------------------------------------------------------------------
# 41. Find the index of the last occurrence of a substring in "Programming in 
# Python Programming" → Substring "Programming". 
# str1 = "Programming in Python Programming"

# print(str1.rfind("Programming"))
#--------------------------------------------------------------------------------------------------------
# 42. Extract substring after a specific word (e.g., "Welcome to Python 
# World" → substring after "to" → "Python World"). 
# str1 = "Welcome to Python World"

# print(str1.split("to ")[1])
#----------------------------------------------------------------------------------------------------

# 43. Extract substring before a specific word (e.g., "Welcome to Python 
# World" → substring before "Python" → "Welcome to"). 
# str1 = "Welcome to Python World"

# print(str1.split("Python")[0].strip())
#------------------------------------------------------------------------------------------------

# 44. Check if two strings are rotations (cyclic substrings) of each other (e.g., 
# "abcd" and "cdab" → Rotations). 
# str1 = "abcd"
# str2 = "cdab"

# if len(str1) == len(str2) and str2 in (str1 + str1):
#     print("Rotation")
# else:
#     print("Not Rotation")
#------------------------------------------------------------------------------------------
# 45. Find the longest common substring between two strings (e.g., "abcdxyz" 
# and "xyzabcd" → Longest common substring = "abcd").

# str1 = "abcdxyz"
# str2 = "xyzabcd"

# longest = ""

# for i in range(len(str1)):
#     for j in range(i + 1, len(str1) + 1):
#         sub = str1[i:j]
#         if sub in str2 and len(sub) > len(longest):
#             longest = sub

# print(longest)