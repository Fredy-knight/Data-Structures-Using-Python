from collections import deque
string = input("Enter the String:")
m=[i.lower() for i in string if i.isalpha()]
queue =deque(m)
while  queue and m :
    if queue.popleft()!=m.pop():
        print(string," is not a palidrome")
        break
else:
    print(string," is  a palindrome")



