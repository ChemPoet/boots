
numbers = [3, 1, 5, 5, 2]
text1 = "abca"
text2 = "abcd"
text3 = "xxy"
numbers1 = [1, 2, 3, 10]
numbers2 = [1, 2, 2, 3]
numbers3 = [5]



'''# Exercise 1: Trace only, no coding

def running_max(numbers):
    running_max = None
    for n in numbers:
        if running_max is None or n > running_max:
            print(f"{n} is a new max!")
        else:
            print(f"{n} is not bigger than current max ({running_max})")
        running_max = max(running_max, n) if running_max is not None else n
    return running_max

# Loop Setup:   running_max = None
# NO CURRENT VALUE FOR n BEING PASSED; THUS NO OUTPUT
# Iteration 1:  running_max = 3
# n = 3         3 is a new max!
# Iteration 2:  running_max = 3
# n = 1        1 is not bigger than the current max (3)
# Iteration 3:  running_max = 5
# n = 5         5 is a new max!
# Iteration 4:  running_max = 5
# n = 5         5 is not bigger than the current max (5)
# Iteration 5:  running_max = 5
# n = 2         2 is not bigger than the current max (5)


numbers = [3, 1, 5, 5, 2]
running_max(numbers)
'''

'''# Exercise 2: Predict the bug

def first_repeat(numbers):
    seen = set()
    for n in numbers:
        seen.add(n)
        if n in seen:
            return n
    return None

print(f'{first_repeat(numbers)}')
'''

'''# Exercise 3: Write it yourself — “first duplicate character”

def first_duplicate_char(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        # WILL ONLY RETURN THE FIRST DUPLICATE, THEN TERMINATE
        seen.add(char)
    return None

print(f'{first_duplicate_char(text1)}')
print(f'{first_duplicate_char(text2)}')
print(f'{first_duplicate_char(text3)}')
'''

'''# Exercise 4: A twist — “seen so far” going the other direction

def is_increasing(numbers):
    max_n = None
#    Test = bool()
    
    for n in numbers:
        if max_n is None or n > max_n:
            max_n = n
#            Test = True
        else:
            return False
#    return Test
    return True

"""when a variable's value is fully determined by how you got to a certain line of code (rather than by any actual data), you often don't need the variable at all — the return True at the end, or the return False inside the loop, communicates that directly and removes a whole category of potential bugs"""

print(f'{is_increasing(numbers)}')
print(f'{is_increasing(numbers1)}')
print(f'{is_increasing(numbers2)}')
print(f'{is_increasing(numbers3)}')
'''

Test = bool
print(f'{Test}')
    # VS
test = bool()
print(f'{test}')