class arrayimp:
    def __init__(this):
        this.stack=[]
    def push(this,data):
        this.stack.append(data) 
    def is_empty(this):
        return this.stack is None
    def pop(this):
        if this.is_empty():
            print("The stack went underflow")
            return False
        print(f"The data {this.stack[-1]} is removed")
        this.stack.pop()
    def peek(this):
        return this.stack[-1]
    def display(this):
        print("The stack is : ",this.stack)
if __name__=='__main__':
    i=0
    a=arrayimp()
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
            
    print("The pop operation")
    a.pop()
    print("The peek operation")
    print("The peek value is ",a.peek())
    
    
    
        


    
        
