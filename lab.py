def add(student,att):
    lis = att["present"]
    lis.append(student)

def remove(student,att):
    list = att["present"]
    list.remove(student)


def display(att):
    lis = att["present"]
    print(lis)


def is_present(student,att):
    lis = att["present"]
    x = lis.count(student)
    if(x<=0):
        print("false")
    else:
        print("true")







    


   
     


   



att = {
    "present": [],
}

x = int(input("enter the no. of present student "))
for i in range(0,x):
    name = input("enter the name of student: ")
    add(name,att)

print(att)
print("\n")

y = int(input("enter the no. of  student to remove: "))

for i in range(0,y):
    name = input("enter the name of student: ")
    remove(name,att)

print("\n")
z = (input("enter whether student is present or not: "))
is_present(z,att)

print("\n display  present student")
display(att)
print("\n")

#quick_sort(att)













