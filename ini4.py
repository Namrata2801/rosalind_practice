"""Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively."""

a = int(input("Enter a positive integer: "))
b = int(input("Enter a second positive integer: "))
sum = 0
for i in range(a,b):
    if i % 2 == 1:
        sum = sum + i
print(sum)