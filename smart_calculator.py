
# main python proghram
response = ['Welcome to smart calculator', 'My name is MONTY',
            'Thanks for enjoy with me ', 'Sorry ,this is beyond my ability']


# fetching tokens from the text command
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


# calculating LCM
def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


# calculating HCF
def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


# Addition
def add(a, b):
    return a + b


# Subtraction
def sub(a, b):
    return a - b


# Multiplication
def mul(a, b):
    return a * b


# Division
def div(a, b):
    return a / b


# Remainder
def mod(a, b):
    return a % b


# Response to command
# printing - "Thanks for enjoy with me" on exit
def end():
    print(response[2])
    input('press enter key to exit')
    exit()


def myname():
    print(response[1])


def sorry():
    return response[3]


# Operations - performed on the basis of text tokens
operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,
              '+': add, 'SUB': sub, 'SUBTRACT': sub,'SUBTRACTION': sub, 'MINUS': sub,
              'DIFFERENCE': sub, 'LCM': lcm, 'HCF': hcf,
              'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,
              'DIVISION': div, 'DIVIDE': div, 'MOD': mod, '/': div, 'REMAINDER'
              : mod, 'MODULAS': mod}

# commands
commands = {'NAME': myname, 'EXIT': end, 'END': end, 'CLOSE': end}

print('--------------' + response[0] + '------------')
print('--------------' + response[1] + '--------------------')



while True:
    text = str(input("enter your query: "))
    operants = []
    action = 0
    for word in text.split(' '):
        if word.upper() in operations.keys():
            action += 1
            operants.append(word.upper())
            try:
                l = extract_from_text(text)
                if action == 1:
                    r = operations[word.upper()](l[action-1], l[action])
                elif action > 1:
                    r = operations[word.upper()](r, l[action])
                print(f'answer to {word}', r)
            except:
                print("something went wrong")
    print("the final answer is " + str(r))
