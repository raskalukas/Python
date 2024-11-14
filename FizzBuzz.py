def FizzBuzz(n,a,b):
    output =""
    for i in range(1,n+1):
        if i % a == 0 and i % b != 0:
            output += "Fizz "
        elif i % b == 0 and i % a != 0:
            output += "Buzz "
        elif i % a == 0 and i % b == 0:
            output += "FizzBuzz "
        else:
            output += str(i) +" "
    print(output)



FizzBuzz(100,3,5)