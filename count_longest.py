# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Joel Davila
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    
    if q.is_empty():
        return 0
        
    len=0
    longest_value = 1
    current = None
    last = None

 
    while not q.is_empty():


        print("q is not empty: ",not q.is_empty()) #Not empty
        current = q.deq()
        
        print("current = q.deq(), current = ",current)
        print(last, " != ",current,"? ",last != current)
        
        if last == current:
            len +=1
            if longest_value < len:
                longest_value = len
            
        else :
            len = 1
                
            
        
        # print("count = ",len)
        last = current
        # print("last = current : ", last)

        print("------")

    return longest_value

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))


# Don't run main on import
if __name__ == "__main__":
    main()

