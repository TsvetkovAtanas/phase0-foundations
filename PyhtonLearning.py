# #--------------------------------------------
# # Basic Data Types
# #--------------------------------------------

# string = "text" # same with ''
# number_int = 10
# number_string = '10'
# number_flaot = 3.14
# boolean = True # or False
# none_type = None

# print(type(number_int))
# print(type(number_string))
# print(f"The number is {type(number_int)}")



# #--------------------------------------------
# # Input & Data Conversion
# #--------------------------------------------

# number_1 = int(input('Enter the first number: '))
# number_2 = int(input('Enter the second number: '))

# print(number_1 + number_2)



# #--------------------------------------------
# # Data Types Functions
# #--------------------------------------------

# str()
# float()
# int()
# bool()

# list()
# tuple()
# set()
# dict()



# #--------------------------------------------
# # Colections Data Types
# #--------------------------------------------

# # LIST ---

# empty_list = [] # or list()

# my_list = ['wall', 'floor', 'roof', 'ceiling']

# print(my_list)
# print(my_list[1])
# print(my_list[-1])

# # Get slice of a list:

# print("get slice of a list:\n")

# print(my_list[:2])
# print(my_list[2:])
# print(my_list[1:2])
# print(my_list[::2])
# print(my_list[::-1]) #print the reversed list


# # Membership operators ---

# my_list = ['wall', 'floor', 'roof', 'ceiling']

# print("wall" in my_list)
# print("floor" not in my_list)

# # Popular Functions with List ---

# # my_list = ['wall', 'floor', 'roof', 'ceiling']
# # num_list = [2, 4, 6, 8, 0, 50]

# # print(len(my_list))
# # print(sorted(my_list))
# # print(sum(num_list))
# # print(min(num_list))
# # print(max(num_list))

# # List methods ---

# my_list = ['wall', 'floor', 'roof', 'ceiling']

# my_list += ['door', 'window'] # can be done with .extend()

# print(my_list)


# #Tuples

# empty_tuple = () # or tuple()

# data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)



# # SET


# set()

# set_items = {10, 20, 20, 30, '5', '5'}

# print(set_items)


# # methods: clear(), remove(), discard(), copy(), pop(), add()

# #copare sets ---

# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))



#dictionaries

# #exersice 1

# def most_frequent_letter(word):
#     word = word.lower()
#     dict_count = dict()
#     for letter in word:
#         if (letter not in dict_count):
#             letter_count = word.count(letter)
#             dict_count[letter] = letter_count
            

#     for k,v in dict_count.items():
#         print(f"{k} used {v} times. \n")

#     max_letter = []
#     for k,v in dict_count.items():
#         if (v == max(dict_count.values())):
#             max_letter.append(k)

#     print(f"The Most Frequent Letter is {max_letter}. Used {max(dict_count.values())} times.")



# words = ["Tomato", "Banana", "Orange", "Running", "Business", "Notebook"]

# for word in words:
#     print(f"--- The word: {word} --- \n")
#     most_frequent_letter(word)




# # #exersice 2


# def password_checker(password):
#     symbols = "~!@#$%^&*()_+|}{:></?.,><`"

#     if len(password) < 8:
#         print(f"Password should have at least 8 charachters! | Yours is {len(password)}.")
#         return True
#     elif not any(char.isdigit() for char in password):
#         print(f"Password should have at least 1 digit!")
#         return True
#     elif not any(char.islower() for char in password):
#         print(f"Password should have at least 1 lower case charachter!")
#         return True
#     elif not any(char.isupper() for char in password):
#         print(f"Password should have at least 1 upper case charachter!")
#         return True
#     elif not any(symbol in password for symbol in symbols):
#         print(f"Password should have at least 1 symbol!")
#         return True

#     return False




# username = input("Enter username:")
# password = input("Enter password:")

# if not password_checker(password):
#     print("Wellcome!")
# else:
#     while password_checker(password):
#        password = input("Try again! Enter password: ")
#     print("Wellcome!")



# #excersice factorial

# def factorial(number, total=1):
#     if number <= 0:
#         return total

#     total *= number
#     return factorial(number - 1, total)


# print(factorial(5))


#
##
###
# filename = 'exampleFile.txt'
# with open(filename, 'r') as file:
#     content = file.read()
#     #print(content)

#     for n, line in enumerate(content.splitlines()):
#         print(n, line)

# filename = 'exampleFile.txt'
# with open(filename, 'a') as file:
#      file.write('Bigger \n Bigger')



# import csv
# import  os

# filename = "exampleCSV.txt"
# # if not os.path.exists(filename):
# #     print(f"Creating a file with the name: {filename}")
# #     with open(filename, 'w') as file:
# #         file.write('Item,Material,CostPerUnit\n')
# #         file.write('Wall,Concrete,150\n')
# #         file.write('Floor,Wood,100\n')
# #         file.write('Roof,Tile,w00\n')
# # else:
# #     with open(filename, 'r') as file:
# #         reader = csv.reader(file)
# #         for row in reader:
# #             print(row)


# with open(filename, 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Toilet', 'Gold', '999'])



# import json

# with open('exmapleJSON.json', 'r') as file:
#     # print(file.read())

#     data = json.load(file)
#     print(data)

#     mats = data['materials']
#     for mat in mats:
# #         print(mat)



# def romanToInt(s: str) -> int:
#         roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         result = 0
#         for i in range(len(s)):
#             if i == len(s):
#                 if roman_dict[s[i]] <= roman_dict[s[i-1]]:
#                     result += roman_dict[s[i]]
#                 else:
#                     result -= roman_dict[s[i]]
#             else:
#                 if roman_dict[s[i]] >= roman_dict[s[i+1]]:
#                     result += roman_dict[s[i]]
#                 else:
#                     result -= roman_dict[s[i]]
#         return result

# romanToInt("III")