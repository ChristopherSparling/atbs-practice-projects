def collatz(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        num2 = num/2
    else:
        num2 = 3*num+1
    print(int(num2))
    return collatz(num2)

print('Enter a number: ')
while True:
    num = input()
    try:
        num = int(num)
        collatz(num)
        break
    except ValueError:
        print("Provide a Valid Number: ")




