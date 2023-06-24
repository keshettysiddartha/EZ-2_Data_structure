queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("enter element")
        queue.append(element)
        print(queue)

def dequeue():
    if not queue:
        print("queue is empty,add the elements")
    else:
        queue.pop(0)
        print(queue)
        
n=int(input("eneter size of queue"))
while True:
    print("select operations 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter the correct operation")
