stc=[]
def push_ele():
    if len(stc)==n:
        print("stack is full")
    else:
        element=input("enter element")
        stc.append(element)
        print(stc)

def pop_ele():
    if not stc:
        print("stack is empty,add the elements")
    else:
        stc.pop()
        print(stc)
        
n=int(input("eneter size of stack"))
while True:
    print("select operations 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_ele()
    elif choice==2:
        pop_ele()
    elif choice==3:
        break
    else:
        print("enter the correct operation")
