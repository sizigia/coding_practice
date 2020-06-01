if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    n_scores = len(student_marks[query_name])
    average = round(sum(student_marks[query_name]) / n_scores, 2)

print("%00.2f" % average)
