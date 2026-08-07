Glad that phrasing clicked. Here's a progression of standalone exercises, each isolating that exact "seen-so-far excludes right now" mechanic, going from simple tracing to writing your own code.

**Exercise 1: Trace only, no coding**
Trace this by hand, writing down the value of running_max before and after each iteration:

def running_max(numbers):
    running_max = None
    for n in numbers:
        if running_max is None or n > running_max:
            print(f"{n} is a new max!")
        else:
            print(f"{n} is not bigger than current max ({running_max})")
        running_max = max(running_max, n) if running_max is not None else n
    return running_max

Trace it with [3, 1, 5, 5, 2]. For each number, ask yourself: "what was running_max before this line even looks at the new number?" Write down what prints for each of the 5 numbers.

# Iteration 0:  running_max = None
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



**Exercise 2: Predict the bug**
Here's a broken version of "find the first repeated number." Someone moved one line and it no longer works correctly:

def first_repeat(numbers):
    seen = set()
    for n in numbers:
        seen.add(n)
        if n in seen:
            return n
    return None

Without fixing it yet — why will this always return the very first number in the list, no matter what? (Hint: think about when n gets added to seen relative to when it gets checked.)

# During the first step of the first iteration, the first value *n* from the list *numbers* is added to the empty set "seen". The subsequent conditional statement will thus always return TRUE and proceed through the rest of the loop, at which point the value of *n* is returned and the loop closes without going through the whole list.


**Exercise 3: Write it yourself — “first duplicate character”**
Write a function first_duplicate_char(text) that returns the first character in a string that has appeared before, or None if there are no repeats.

first_duplicate_char("abca")   # "a" (it appeared at index 0, then again at index 3)
first_duplicate_char("abcd")   # None
first_duplicate_char("xxy")    # "x"

Use the same shape as first_number_seen_twice from earlier. Before you write any code, answer this: for each character, what do you check first, and what do you do second?

# First check: Whether the character appeared previously in this string at an earlier index position (i.e., is it present in the set of seen characters)? If yes, return the duplicate character as an output.
# Second check: If the character has not been seen before, add it to the set of seen characters. 


**Exercise 4: A twist — “seen so far” going the other direction**
This one flips it slightly, to test if you can spot the pattern even when it's not about duplicates. Write is_increasing(numbers), returning True if every number is strictly greater than the one before it.

is_increasing([1, 2, 3, 10])  # True
is_increasing([1, 2, 2, 3])   # False
is_increasing([5])            # True

Ask yourself: what do you need to remember from the previous iteration in order to judge the current number? What should happen if you're on the very first number, when there is no "previous" yet?

Try Exercise 1 first (just tracing, no code) and tell me what you got for each of the 5 numbers. Once that's solid, move to predicting the bug in Exercise 2 before attempting to write Exercises 3 and 4 yourself.

## when a variable's value is fully determined by how you got to a certain line of code (rather than by any actual data), you often don't need the variable at all
# the *return True* at the end, or the *return False* inside the loop, communicates that directly and removes a whole category of potential bugs