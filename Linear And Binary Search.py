n = int(input("Enter number of students: "))
rn = []

for i in range(n):
    a = int(input("Enter the roll number: "))
    rn.append(a)

key = int(input("Enter the roll number to check: "))

print("=== Linear Search ===")
print(rn)

f1 = False
t = 0

for i in range(len(rn)):
    if rn[i] == key:
        t = i
        f1 = True
        break

if f1:
    print("The roll number", key, "is found at the index", t)
else:
    print("The roll number is not found!")

print("=== Binary Search ===")
s = sorted(rn)
print(s)

l = 0
h = len(s) - 1
f = False
t = -1

while l <= h:
    mid = (l + h) // 2

    if s[mid] == key:
        f = True
        t = mid
        break
    elif s[mid] > key:
        h = mid - 1
    else:
        l = mid + 1

if f:
    print("The roll number", key, "is found at the index", t,
          "in the sorted list")
else:
    print(key, "is not found!")
