# Given the names and grades for each student in a Physics class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically
# and print each name on a new line.

py_students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        py_students.append([score, name])

    py_students.sort(key=lambda x: x[0])

    second_lowest = sorted([i for i in py_students if i[0]
                            > py_students[0][0] and i[0] <= py_students[1][0]])

    print("\n".join(sorted([i[1] for i in second_lowest])))



# Sample Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample input (Beria Harsh):
# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21

# Sample input (Shaheen):
# 4
# Rachel
# -50
# Mawer
# -50
# Sheen
# -50
# Shaheen
# 51
