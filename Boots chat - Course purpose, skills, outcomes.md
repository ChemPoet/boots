Boots request input:
Can you supply me with a list of the Python skills / topics that we have covered thus far?
I would like to keep record of the topics we have covered in a separate file on my device. I want to practice keep track of what skills I am most and lest comfortable with to make it easier for myself to specify what types of exercise questions I would like to do in the training grounds.Produce the list in a format that I can directly copy-paste into a Markdown file, please? So that the headings, bullets, links, etc., will be preserved when I copy the text over from this interface into my text editor.

Boots output:

# Python Topics and Skills Covered

---

## 1. Python Basics & Fundamentals
*[Learn Python for Beginners](https://www.boot.dev/courses/learn-python-beginners)*

- **Variables & Data Types:** Integers, floats, booleans, strings, and type conversions.
- **Operators & Expressions:** Arithmetic operators, string concatenation, and operator precedence.
- **Functions:** Defining functions, parameters vs. arguments, return values, and multiple return values.
- **Scope:** Global vs. local scope.
- **Testing & Debugging:** Reading stack traces, unit tests, and debugging strategies.
- **Comparisons & Conditionals:** Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`), logical operators (`and`, `or`, `not`), and `if`/`elif`/`else` control flow.
- **Loops:** `for` loops, `range()`, `while` loops, `break`, and `continue`.
- **Data Collections:**
  - **Lists:** Indexing, slicing, appending, popping, list operations, and list iteration.
  - **Dictionaries:** Key-value pairs, accessing, setting, deleting, dictionary iteration, and `.get()`.
  - **Sets:** Set creation, unique elements, membership checks, unions, intersections, and differences.
- **Errors & Exception Handling:** `try`/`except` blocks, catching exceptions, raising custom exceptions.
- **Type Hints:** Type annotations for variables, function arguments, and return types.

---

## 2. Practical Application & Tooling
*[Build a BookBot in Python](https://www.boot.dev/courses/build-bookbot-python)*

- File I/O (`with open(...)`)
- Reading and processing text files
- Character and word counting algorithms
- Structuring small command-line utilities

---

## 3. Object-Oriented Programming (OOP)
*[Learn Object Oriented Programming in Python](https://www.boot.dev/courses/learn-object-oriented-programming-python)*

- **Classes & Objects:** Attributes, methods, `__init__`, and the `self` reference.
- **Clean Code:** Single responsibility principle, readability, and DRY (Don't Repeat Yourself).
- **Encapsulation:** Public vs. private/protected attributes (name mangling with `__`), getter and setter patterns.
- **Abstraction:** Hiding complex implementation details behind simple interfaces.
- **Inheritance:** Base (parent) and derived (child) classes, method overriding, and calling `super()`.
- **Polymorphism:** Method overriding across subclasses, shared interfaces, and duck typing.

---

## 4. Interactive Simulation & Game Loops
*[Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python)*

- Pygame fundamentals
- Game loops and delta time (`dt`)
- Event handling and user input
- Vector math and 2D movement
- Object rendering, collision detection, and sprite management

---

## 5. Functional Programming
*[Learn Functional Programming in Python](https://www.boot.dev/courses/learn-functional-programming-python) (Chapters 1-4)*

- **What is Functional Programming:** Declarative vs. imperative style, avoiding state mutation.
- **First-Class & Higher-Order Functions:**
  - Functions as variables and arguments
  - Returning functions from functions
  - Anonymous functions (`lambda`)
  - Built-in higher-order tools (`map`, `filter`, `reduce`)
- **Pure Functions:**
  - Determinism (same input produces the same output every time)
  - Eliminating side effects
  - Immutability and reference vs. value copying
- **Recursion:**
  - Base cases and recursive steps
  - Call stack mechanics
  - Tracing recursive execution and avoiding infinite recursion


Boots request input:
Please generate a summary statement or paragraph for each of these 5 courses explaining the module's purpose in the learning path and highlighting the key learning objective(s) a student masters by the end of the module.

Boots output:

### 1. Learn Python for Beginners
- **Purpose:** Establishes the foundational syntax, core mental models, and primary data structures of programming using Python. This module equips learners with the essential vocabulary and control-flow mechanisms required to write executable logic and understand procedural programming.
- **Key Objectives:** Master variables, data types, function design, scoping, conditional logic, loops, error handling, type annotations, and core collections (lists, dictionaries, and sets).

---

### 2. Build a BookBot in Python
- **Purpose:** Serves as the first guided project, bridging the gap between isolated browser exercises and end-to-end program execution. It demonstrates how to combine basic algorithmic thinking with system-level operations to build a practical command-line tool.
- **Key Objectives:** Master practical file input/output (I/O), raw text processing, data aggregation, and structuring a multi-file Python script executed locally.

---

### 3. Learn Object-Oriented Programming in Python
- **Purpose:** Introduces the object-oriented paradigm to manage code complexity at scale. This module teaches how to model real-world concepts into software components, enforce boundaries between system parts, and write modular, maintainable architectures.
- **Key Objectives:** Master the four pillars of OOP (Encapsulation, Abstraction, Inheritance, and Polymorphism), class and instance mechanics, state management, and clean code principles such as DRY and Single Responsibility.

---

### 4. Build Asteroids using Python and Pygame
- **Purpose:** Applies object-oriented architecture in an interactive, real-time environment. It challenges learners to handle continuous state changes, physics simulations, and user-driven events, demonstrating how complex systems operate dynamically over time.
- **Key Objectives:** Master game-loop architecture, frame-rate-independent movement using delta time, 2D vector mathematics, collision detection algorithms, and object lifecycle management.

---

### 5. Learn Functional Programming in Python
- **Purpose:** Shifts perspective from imperative and stateful code to a declarative, mathematical style of problem-solving. This module emphasizes code predictability, safety, and reusability by minimizing shared state and unintended side effects.
- **Key Objectives:** Master first-class and higher-order functions (`map`, `filter`, `reduce`), pure function design, immutability, recursion, and advanced compositional techniques like currying, closures, and decorators.
