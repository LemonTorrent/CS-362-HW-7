def FizzBuzz( num ):
    retStatement = ""
    #print (num)
    print()
    for i in range(num):
        if ((i + 1) % 3 == 0):
            print("Fizz")
            retStatement += "Fizz"
        elif ((i + 1) % 5 == 0):
            print("Buzz")
            retStatement += "Buzz"
        else:
            print(i+1)
            retStatement += str(i+1)
        retStatement += " "

    return retStatement
