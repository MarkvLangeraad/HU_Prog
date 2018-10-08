grade= {'Mark': 9, 'Steven': 1, 'Sander': 10, 'Bart': 8, 'Snoepie': 9.4, 'Hans': 9.9, 'Grietje': 7, 'Kees': 8.3}

for students, grades in grade.items():
    if grades >= 9:
        print(students, grades)

