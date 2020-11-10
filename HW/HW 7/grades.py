
data = {}

def option1():
    print '--Add Student--'
    name = str(raw_input('Enter Name: '))
    grade = str(raw_input('Enter Grade: '))
    data[name] = grade
    print '\nStudent Successfully Added!'
def option2():
    print '--Remove Student--'
    name = str(raw_input('Enter Name: '))
    del data[name]
    print "\nSuccessfully Removed '%s'!" % name
def option3():
    print '--Modify Student Grade--'
    name = str(raw_input('Enter Name: '))
    grade = str(raw_input('Enter Grade: '))
    data[name] = grade
    print "\nSuccessfully Updated '%s'!" % name
def option4():
    print '--Displaying All Students--'
    for x,y in data.items():
        print '%s : %s' % (x.title(), y.title())

    
while True:
    option = int(raw_input(
    """\nSelect an option:
    [1] Add Student Grade
    [2] Remove Student Grade
    [3] Modify Student Grade
    [4] Display All Student Grades
    
Enter Selection: """))
    if option == 1:
        option1()
    if option == 2:
        option2()
    if option == 3:
        option3()
    if option == 4:
        option4()
