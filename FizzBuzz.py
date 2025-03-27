#Fizz Buzz
#define a function that takes a number n as an argument
def fizz_buzz(n):
    #iterate from 1 to n
    for i in range(1,n+1):
        #check if i is divisible by 3 and 5
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        #check if i is divisible by 3
        elif i%3==0:
            print("Fizz")
        #check if i is divisible by 5
        elif i%5==0:
            print("Buzz")
        #if i is not divisible by 3 or 5
        else:
            print(f"{i}")

#call the function with the first 1000 numbers
fizz_buzz(1000)

contador=0
