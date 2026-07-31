# Random code trial blurps

def devision(a, b):
    return a/b

def floor(a, b):
    return a//b

def modulus(a, b):
    return a%b

num1 = int(input('\nPlease input a negative whole number between -10 and -1:\n\t'))
num2 = int(input('\nPlease input a positive whole number between 1 and 10:\n\t'))

print(f"""\nLet's do some simple maths with {num1} and {num2}.
      \t{num1} / {num2} = {devision(num1,num2)} (devision)
      \t{num1} // {num2} = {floor(num1,num2)} (floor division; rounds DOWN)
      \t{num1} % {num2} = {modulus(num1, num2)} (modulus)""")