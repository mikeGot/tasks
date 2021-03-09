input_ = int(input())

a = 0
b = 1

while True:
    if b == input_:
        print(True)
        break
    elif b > input_:
        print(False)
        break
    a, b = b, a+b

