#1

x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15

print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"] = "Bryant"
print(students)




sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30
print(z)

#2

def iterateDictionary(students):
    for student in students:
        for key, value in student.items():
            print(key, " - ", value, end=' ')
        print()
    

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(iterateDictionary(students)) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
        else:
            print("Key not found in dictionary")


students = [
        {"first_name": "Michael", "last_name": "Jordan",},
        {"first_name": "John", "last_name": "Rosales",},
        {"first_name": "Mark", "last_name": "Guillen",},
        {"first_name": "KB", "last_name": "Tonel",}
]

print(iterateDictionary2("first_name", students))
print(iterateDictionary2("last_name", students))


#4

def printInfo(dojo):

    for value in dojo.values():
        print(len(value))
        print(value)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


