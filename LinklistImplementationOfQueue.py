class Node:
    def __init__(me,data):
        me.data=data
        me.next=None
class queue:
    def __init__(me):
        me.front = None
        me.rear = None
    def is_empty(me):
        return me.front is None
    def enqueue(me,data):
        new=Node(data)
        if me.front is None:
            me.front=me.rear=new
            return
        me.rear.next=new
        me.rear = new
    def dequeue(me):
        if me.front is None:
            return
        data = me.front.data
        me.front=me.front.next
        if me.front is None:
            return None
        return  data
    def display(me):
        if me.front is None:
            return
        temp=me.front
        while temp:
            print(temp.data,end="-")
            temp=temp.next
        print(None)
a=queue()
while True:
    x=int(input("Enter choice for edit queue( 1-enqueue/2-dequeue/3-stop&display):"))
    if x==1:
        print("Enter space to stop enqueueing")
        while True:
            element=input("Enter element to enqueue:")
            if element=="":
                break
            a.enqueue(int(element))
    elif x==2:
        print("Enter space to stop dequeueing")
        while True:
            element = input("Enter '1' dequeue one element:")
            if element=="":
                break
            a.dequeue()
    else:
        print("The elements in the queue are :",end =a.display())
        break

        
            

        
        
