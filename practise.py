
import random
import pandas

numbers = [1,2,3]

new_list = []

# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

new_list = [n+2 for n in numbers]
# print(new_list)

name = "Raihan"
new_list1 = [letter for letter in name]
# print(new_list1)

range_list = [num for num in range(1,9)]
# print(range_list)

names = ["raihan", "kabir", "rafsan", "robin"]
short_names = [name.title() for name in names if len(name)<6]
# print(short_names)


names = ["raihan", "kabir", "rafsan", "robin", "rifat"]

student_score = {student : random.randint(10, 100) for student in names}
# print(student_score)

student_data_frame = pandas.DataFrame({
    "student" : list(student_score.keys()),
    "score"   : list(student_score.values())
})
print(student_data_frame)
student_data_frame.to_csv("new_data.csv")

# for (index, row) in student_data_frame.iterrows():
    




