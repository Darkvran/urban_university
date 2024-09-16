grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = list(map(lambda grades_list: sum(grades_list)/len(grades_list), grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(list(students))

print(dict(zip(student_list, average_grades)))

