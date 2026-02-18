#Name : Bob Afwata
# Date : 18/02/2026
# Program to show lists in python
#list of friends
friends = ["Rachel","Pheobe","Ross","Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Tracy","James","Faith","Don","Augustine","Wendy"]

print(len(new_friends))

#new list of students
students = friends + new_friends

print(students)
students.pop()
print(students)
students.insert(5,"Jenny")
print(students)
students.extend("James")
print(students)

students.remove("Joey")
print(students)

new_students = students.copy()
print(new_students)