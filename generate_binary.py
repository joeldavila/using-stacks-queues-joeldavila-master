# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Joel Davila
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
    numbers = Queue([])
    temp = Queue([])
    temp.enq("1")

    

    for n in range(N):
       value =  temp.deq()
       numbers.enq(value)
    #    value += "0"
       temp.enq(value + "0")

    #    value += "1"
       temp.enq(value + "1")


    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

