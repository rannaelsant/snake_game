import random

names = ["Dante", "Alex", "Maria", "Ana", "Diego"]

students_score = {student:random.randint(1, 100) for student in names}
students_passed = {student:score for (student, score) in students_score.items() if score >= 60}

print(students_score)
print(students_passed)

sentence = "Why learn Python is so very important?"

result = {word:len(word) for word in sentence.split()}
print(result)
# or for word in sentence.split():
#    print(word)


