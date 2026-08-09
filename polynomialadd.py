class Node:
    def __init__(this,co,po):
        this.co= co
        this.po= po
        this.next = None
class Polynomial:
    def __init__(this):
        this.head = None
    def inserting(this,co,po=0):
        new = Node(co,po)
        if this.head is None or this.head.po<po:
            new.next =this.head
            this.head =new
            return
        current = this.head
        while current.next and current.next.po>po:
            current = current.next
        if current.next and current.next.po==po:
            current.next.co+=co
        elif current.po==po:
            current.co+=co
        else:
            new.next=current.next
            current.next=new
    def polyadd(result,poly1,poly2):
        a=poly1.head
        b=poly2.head
        while a and b:
            if a.po==b.po:
                result.inserting(a.co+b.co,a.po)
                a=a.next
                b=b.next
            elif a.po>b.po:
                result.inserting(a.co,a.po)
                a=a.next
            else:
                result.inserting(b.co,b.po)
                b=b.next
            while a:
                result.inserting(a.co,a.po)
                a=a.next
            while b:
                result.inserting(b.co,b.po)
                b=b.next
            return result
    def show(this):
        current  = this.head
        while current:
            print(current.co,"X^",current.po,end="->")
            current =current.next
        print(None)
        return
    
if __name__=='__main__':
    poly1=Polynomial()
    x=0
    y=0
    print ("Enter values of polynomial 1 (enter 'None' to stop):")
    while True:
        x=str(input("Enter coeff:"))
        y=str(input("Enter power:"))
        if not(x and y) :
            break
        poly1.inserting(int(x),int(y))
        
    
    
    print("Polynomial 1 =",end="")
    poly1.show()
    poly2=Polynomial()
    print ("Enter values of polynomial 2 (enter 'None' to stop):")
    while True:
        x=str(input("Enter coeff:"))
        y=str(input("Enter power:"))
        if not(x and y) :
            break
        poly2.inserting(int(x),int(y))
    print("Polynomial 2 =",end="")
    poly2.show()
    result=Polynomial()
    result.polyadd(poly1,poly2)
    print("Additon of two polynomials:",end=" ")
    result.show()
    
    
            
            
        
        
