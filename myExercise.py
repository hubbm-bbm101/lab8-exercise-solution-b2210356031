import sys
content = {}
students = open("student.txt","r+")
student_list = sys.argv[1].split(",")
for line in students:
    content[line.split(":")[0]] = line.split(":")[1]
for item in student_list:
    try:
        print("Name:",item,",","University:",content[item])
    except(KeyError):
        print("No record of {} found!".format(item))

