number = input("Enter a number: ")
n = int(number)
sum = 0
for i in range(1, n+1):
   if ( n%3) or (n%5) == 0:
        sum = sum + i
        print(sum)
