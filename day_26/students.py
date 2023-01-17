import random
import pandas

names = ["Dante", "Alex", "Maria", "Ana", "Diego"]

students_score = {student:random.randint(1, 100) for student in names}

students_data_frame = pandas.DataFrame(names, students_score)
print(students_data_frame)