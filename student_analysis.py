import math as m
students_details=[
    ("Alice", ("Math", "Science", "English"), (85, 90, 88)),
    ("Bob", ("Math", "Science", "English"), (78, 82, 80)),
    ("Charlie", ("Math", "Science", "English"), (92, 95, 89)),
    ("Diana", ("Math", "Science", "English"), (70, 75, 72)),
    ("Ethan", ("Math", "Science", "English"), (88, 84, 91))
]
students_dict={}
for student in students_details:
    name=student[0]
    subject=student[1]
    marks=student[2]
    main={}
    for j in range(len(subject)):
        main[subject[j]]=marks[j]
    students_dict[name]=main
#print(students_dict)
for name,details in students_dict.items():
    print("Student's Name : ",name)
    for subject,mark in details.items():
        print("Marks Scored in",subject,"is : ",mark)
    print()
above_80=[]
below_40=[]
for name,details in students_dict.items():
    for subject,mark in details.items():
        if mark>80:
            if name not in above_80:
                above_80.append(name)
        elif mark<40:
            if name not in below_40:
                below_40.append(name)
if len(above_80)>=1:
    print("Above 80 Students..")
    for name in above_80:
        print(name)
    print()
else:
    print("No students have scored above 80..")
    print()
if len(below_40)>=1:
    print("Below 40 Students..")
    for name in below_40:
        print(name)
    print()
else:
    print("No students have scored below 40..")
    print()
subjects=["Math","Science","English"]
for subject in subjects:
     high_scorer=None
     high_mark=-1
     for name,marks in students_dict.items():
        if marks[subject]>high_mark:
            high_scorer=name
            high_mark=marks[subject]
     print(f"{subject} highest mark : {high_scorer} , got {high_mark}")
print()
for name,details in students_dict.items():
    marks=sum(details.values())
    average=m.ceil((marks/3))
    print(f"{name} has scored a total of {marks} and average is {average} %")
    print()
print()
students=["Alice","Bob","Charlie","Diana","Ethan"]
for student in students:
    topper=None
    avg_topper=-1
    for name , marks in students_dict.items():
        avg=m.ceil((sum(marks.values()))/3)
        if avg>avg_topper:
            topper=name
            avg_topper=avg
print(f"{topper} is the topper with {avg_topper} %")
print()
