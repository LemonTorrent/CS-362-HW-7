def FizzBuzz( num ):
    retStatement = ""
    #print (num)
    print()
    for i in range(num):
        intStatement = ""
        if ((i + 1) % 3 == 0):
            #print("Fizz")
            intStatement += "Fizz"
        if ((i + 1) % 5 == 0):
            #print("Buzz")
            intStatement += "Buzz"
        if (((i + 1) % 3 != 0) and ((i + 1) % 5 != 0)):
            #print(i+1)
            intStatement += str(i+1)
        print(intStatement)
        retStatement += intStatement
        retStatement += " "

    return retStatement
