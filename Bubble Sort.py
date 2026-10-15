n = int(input("Enter the number of subjects : "))
marks = []

for i in range(n):
    mark = int(input("Enter the marks: "))
    marks.append(mark)

for i in range(n - 1):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Marks in ascending order:", marks)
