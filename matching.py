# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Joel Davila
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    s = Stack()
    
    open_braces = "([{"
    close_braces = ")]}"
    braces = {")": "(", "}": "{", "]": "["}

    cleaned_str = ""
    for i in str:
        if i in open_braces or i in close_braces:
            cleaned_str += i

    for i in cleaned_str:
        if i in open_braces:
            s.push(i)
        elif i in close_braces:
            if s.is_empty():
                return False
            top = s.pop()
            if top != braces[i]:
                return False

    return s.is_empty() 

def main():
    print("matcher: ", matcher("[()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

