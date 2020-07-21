last_semester_gradebook = [
    ("Politics", 80), ("Latin", 96), ("Dance", 97), ("Architecture", 65)]

subjects = ['Physics', 'Calculus', 'Poetry', 'History']
grades = [98, 97, 85, 88]
subjects.append('Computer Science')
grades.append(100)

gradebook = list(zip(subjects, grades))
gradebook.append(('visual arts', 93))
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
