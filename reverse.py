# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Joel Davila
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    stack = Stack([])
    for num in range(q_orig.size()):
        item = q_orig.deq()
        stack.push(item)
    while not stack.is_empty():
        item = stack.pop()
        q_new.enq(item)
        
    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
