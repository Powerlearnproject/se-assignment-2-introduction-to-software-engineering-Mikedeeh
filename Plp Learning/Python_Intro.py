#Correct Indentation
# age = 18
# if age >= 18:
#     print("You are an Adult")
# elif age > 12:
#     print("You are a teenager")
# else:
#     print("You are a Child")

#List Comprehension
# squares = [x**2 for x in range(10)]
# print(squares)
#For Loop
for i in range(5):
    print(f"i is i")
#While Loop
# count = 0
# while count < 5:
#     print(f"count is {count}")
#     count += 1 
#Function
def add(a,b):
    return a + b
results =add(5, 8)
print(results)
#Functions
#Lambda Function
multiply = lambda x, y: x * y
print(multiply(3,5))