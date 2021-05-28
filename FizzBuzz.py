def FizzBuzz( num ):
    retStatement = ""
    print (num)
    for i in range(num):
        print(i+1)
        retStatement += str(i+1)
        retStatement += " "

    return retStatement
