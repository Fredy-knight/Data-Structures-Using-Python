class Node:
    def __init__(this,data):
        this.next=None
        this.data=data
class LinkedListimp:
    def __init__(this):
        this.peek = None
    def is_empty(this):
        return this.peek is None
    def  push(this,data):
        new = Node(data)
        new.next = this.peek
        this.peek = new
    def pop(this):
        if this.is_empty():
            print("Stack went underflow!")
            return None
        top = this.peek.data
        this.peek=this.peek.next
        print(f"The poped value is {top}")
    def display(this):
        current= this.peek
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print(None)
a=LinkedListimp()
i=0
hst=int(input("Enter the max value : "))
while True:
    x=input("Enter leave space to end appending:")
    if x=='':
        break
    i+=1
    if i>hst:
        print("The stack went overflow")
        break
    else:
        a.push(int(x))
a.display()
            
print("The pop operation")
a.pop()
a.pop()
a.pop()


            
        
        
     
