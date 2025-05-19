# Problem 3: Generate odd number series with even/odd logic


a = int(input("Enter value of a: "))
if a % 2 == 0:
    n = a - 1
else:
    n = a
series = [str(2*i+1) for i in range(n)]
print(", ".join(series))
