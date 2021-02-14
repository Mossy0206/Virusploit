
for i in range(1, 101):
    result = i % 3
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i)