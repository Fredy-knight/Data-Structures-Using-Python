class Queue:
    def __init__(me):
        me.queue=[]
        me.size = int(input("Enter the size of the queue:"))
        me.front = -1
        me.rear = -1
    def enqueue(me,value):
        if me.rear == (me.size)-1:
            print("Queue is FULL!!! insertion is not possible!!!!")
            return
        me.rear+=1
        me.queue.append(value)
    def dequeue(me):
        if me.front==me.rear:
            print("Queue is EMPTY")
            return
        me.front+=1
        if me.front==me.rear:
            me.front=me.rear=-1
    def display(me):
        if me.front==me.rear:
            print("Queue is EMPTY!!!")
            return
        i=me.front+1
        while i<=me.rear:
            print(me.queue[i],end="-")
            i+=1
        print(None)
a=Queue()
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
        
