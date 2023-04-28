# Write a function that uses while, if and continue statements to
# print all the even numbers between 0 and 50. 
def continue_statement():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
              continue
        print(x)
    
# Write a function that takes an integer argument and
# prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def is_prime(number):
    if number <2:
        print("Not a prime")
    for i in range(2,number):
        if number%i==0:
            print("Not a prime")
        else:
            print("PRIME")
is_prime(4)

# Write a function that takes a list of integers as input and 
# prints the sum of all the even numbers in the list.
numbers=[3,4,5,6,7,8,9]
def even_numbers(numbers):
    total=0
    for i in numbers:
        if i%2==0:
            total+=i
    print(total)
even_numbers(numbers)

   
#  Write a function that takes any two integers as input, 
# and prints the sum of all the numbers between the two integers (inclusive) 
# that are divisible by 3.
def divisible_three():
    sum=0
    x=range(10,30)
    for i in x:
        if i%3==0:
            sum+=i
    print(sum)

   
   
