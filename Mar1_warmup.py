# We need to use Conditional statments (IF/ ELSE/ ELIF)

# We need to write a function that has a parameter

# We need to enter number score as an argument

grades = [60,70,80,90]

def gradeBook(gradeScore):
    if gradeScore >= grades[3]:
        print('this student has an A')
    elif gradeScore >= grades[2]:
        print('this student has an B')
    elif gradeScore >= grades[1]:
        print('this student has an C')
    elif gradeScore >= grades[1]:
        print('this student has an D')
    else:
        print('this student has an F')   