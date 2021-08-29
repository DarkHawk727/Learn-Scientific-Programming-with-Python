import sys

n = sys.argv[1]

try:
   n = int(n)
except ValueError:
   print("User string is not number")

while n > 0:
    if n == 1:
        break
    elif n % 2 == 0:
        n = n/2
        print(int(n), end=', ')
    else:
        n = 3 * n + 1
        print(int(n), end=', ')
