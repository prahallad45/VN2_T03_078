# using while loop display numbers 1 to 100

num1 = int(input("enter first number :"))
num2= int(input("enter second number"))

if num1 < num2:
    while num1 <= num2:
        print(num1)
        num1 += 1
else:
    print("enter valid numbers")


# while loop

# print numbers 1 to 10

print("START")
x = 1
while x <= 10:
    print(x)
    x += 1
print("END")


# Display Numbers between any two numbers
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
if x < y:

   while x <= y:
        x += 1
        print(x)
   print("END The While loop")
else:
   print("Enter valid numbers")




