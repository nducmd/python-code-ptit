exp = str(input())
lst = list(exp.split())

if int(lst[0]) + int(lst[2]) == int(lst[4]):
    print("YES")
else:
    print("NO")