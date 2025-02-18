'''
* * * *
* * * *
* * * *


size = int(input("Enter the size : "))
row = int(input("Enter the row: "))

for i in range(row):
    for j in range(size):
        print("*", end=" ")
    print()'''

"""
Multiplication Table 
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15 
4 8 12 16 20 
"""
"""def mul_table():
    for i in range(1, 6):
        for j in range(1, 6):
            print(i * j,end="\t")
        print()

mul_table()"""

"""def i_j_table():
    for a in range(3):
        for b in range(2):
            print(f"i = {a}, j = {b}",end="\n")
        print()

i_j_table()"""

"""
student 1 average grade = xx.xx
student 2 average grade = xx.xx
student 3 average grade = xx.xx
"""


"""grade = [[45,90,98],
         [92,67,99],
         [79,85,88]
         ]
for stu_index, stu_grade in enumerate(grade):
    total = 0
    for grades in stu_grade:
        total += grades
    average = total/len(stu_grade)
    print(f"student {stu_index + 1} average grade: {average:.3f}")"""

def avg_get():
    avg = []
    while True:
        row = int(input("Enter a number: "))
        if row != -1:
            avg.append(row)
        else:
            print(f"The average is {round(sum(avg)/len(avg),2)}")
            break

avg_get()