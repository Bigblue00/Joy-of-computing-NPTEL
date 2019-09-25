a=list(map(int,input().split()))
b=[]
for num in a:
	if num not in b:
		b.append(num)
print(*b,end="")