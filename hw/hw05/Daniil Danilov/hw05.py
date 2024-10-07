############### Task 1 ###############

# Create a list that contains elements of integer type, then use 
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

print("############### Task 1 ###############\n")
l = [7, 10, 20, -24, -57, 1234, 95, 47, 38, -12]
print ("Integer type: ", l)

for i in range(len(l)):
    l[i]=float(l[i])
print ("Floating type" ,l)


############### Task 2 ###############

# Print Fibonacci numbers up to the entered number n, using cycles. 
#(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

print("\n############### Task 2 ###############\n")

n = int(input("Enter your number: "))

a, b = 0, 1

print("Fibonacci numbers up to the", n, ":", end=' ')
while a <= n:
    print(a, end=' ')
    a, b = b, a + b


############### Task 3 ###############

# Write a script that will calculate the factorial of the entered 
# number without using recursion.
# Example:     0!=1,  1!=1,  2!=1*2, 3!= 1*2*3=6,

print("\n\n############### Task 3 ###############\n")
print("\nExample: 0!=1,  1!=1,  2!=1*2, 3!= 1*2*3=6 \n")


n = int(input("Enter a number to calculate in factorial: "))
f = 1 

if n < 0:
    print("You cant use negative numbers for factorial.")
else:
    for i in range(1, n + 1):
        f *= i  

    print("The factorial of", n, "is", f)
