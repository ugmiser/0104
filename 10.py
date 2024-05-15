numbers = input().split()
encountered = set()
for num in numbers:
    if num in encountered:
        print("YES")
    else:
        print("NO")
        encountered.add(num)
