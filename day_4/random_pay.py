import random as rd

names_string = input("Give me everybody's names, separate by a comma. ")

names = names_string.split(", ")

num_items = len(names)

random_choice = rd. randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today.")