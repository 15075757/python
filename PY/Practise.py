# name = 'bob'
# age = 30
# weight = 70.5
# is_female = False

# print(name)
# print(type(name))

# x = 10
# y = 3.5

# print (x+y)
# print (x*y)
# print (x/y)
# print (x//y)    
# print (x-y)
# print (x**y)
# print (x%y)

# a = "Human"
# b = 13
# c = 3.14
# is_Integer = True

# print (a)
# print (b)
# print (c)
# print (is_Integer)

# celcius = int(input("Enter temperature in celcius: "))
# fahrenheit = celcius * 9/5 + 32
# print("Temperature in Fahrenheit is: ", fahrenheit)
# print("Temperature in Celsius is: ", round(celcius, 2))
# **tuples**
# coordinates = (10.0, 20.0)
# person = ('alice',25,'engineer')
# single_item = (42,)

# #tuple operations
# print(coordinates[0])
# print(len(person))
# # print(coordinates.append(30.0))  # This will raise an AttributeError

# #sets#
# fruits = {'apple', 'banana', 'cherry'}
# number = {1, 2, 3, 4, 5}

# #set operations
# fruits.add('kiwi')
# fruits.remove('banana')
# fruits.discard('cherry')  # No error if 'grape' not present
# print(fruits)

# set1={1, 2, 3}
# set2={3, 4, 5}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

#Exercise 1. create a system that stores student grades as tuples(name , subject , grade) and uses set to find the unique subjects taken by students. subjects and students

# grades =[
# ('alice', 'math', 90),
# ('bob', 'science', 85),
# ('alice', 'science', 95),
# ('charlie', 'math', 80),
# ('bob', 'math', 88)
# ]

# name = set()
# for grade in grades:
#     name.add(grade[0])
#     print(name)
# print("Unique students: ", name)


# subjects = set()
# for grade in grades:
#     subjects.add(grade[1])
#     print(subjects)
# print("Unique subjects: ", subjects)


# alice_grades = []
# for grade in grades:
#     if grade[0] == 'alice':
#         alice_grades.append((grade[1],grade[2]))
# print("Alice's grades: ", alice_grades)

#dictionary

# student = {
#     "name": "john",
#     "age": 21,
#     "grades":"A",
#     "courses" : ["math", "science"]
    
#     }

# # #accessing and modifying
# # print(student["name"])
# # print(student.get("age"))
# # student["age"] = 22
# # student["emails"] = "john@gmail.com"
# # print(student)  

# # keys = student.keys()
# # values = student.values()
# # items = student.items()

# # print(keys)
# # print(values)
# # print(items)

# #iterating through dictionary
# # for key in student:
# #     print(f"{key} : {student[key]}")

# #nested dictionary

# # company = {
# #     "employees": {
# #         "alice": {"age": 30, "position": "developer" },
# #         "bob": {"age": 25, "position": "designer" },
# #     },
# #     "departments": ["engineering", "design", "marketing"],
# # }

# # print(company["employees"].items())
# # print(company["departments"])

# # Exercises:
# #Create a dictionary called student_records with the following information:

# student_records = {
#     "student_001" :{
#         "name": "John",
#         "age" : 19,
#         "major" : "Computer Science",
#         "grades" : [85, 92, 78]
#     },
#     "student_002" :{
#         "name": "Sarah",
#         "age" : 20,
#         "major" : "Biology",
#         "grades" : [90, 88, 95]
#     },
# }

# print(student_records)

# student_records["student_003"] = {
#     "name": "Mike",
#     "age" : 18,
#     "major" : "Mathematics",    
#     "grades" : [82, 79, 91]
# }

# student_records["student_001"]["age"] = 20

# print(student_records["student_001"])

# #loop through the student_records dictionary in this format: 
# #"Student ID: [id], Name: [name], Major: [major]"

# for student_id in student_records:
#     student = student_records[student_id]
#     print(f"student record : {student}")
#     print(f"Student ID: {student_id},Name: {student['name']},Major: {student['major']}")

#loop
# for i in range(5):
#     print(i)

# for i in range (1,10):
#     print(i)

# for i in range (0,10,2) :
#     print(i)

# #while
# count = 0 
# while count < 5:
#     print(count)
#     count += 1

#lopop control statement

# for i in range (1, 11):
#     if i == 2:
#         continue
#     if i == 8:
#         break
#     print(i)

#nested loop 
