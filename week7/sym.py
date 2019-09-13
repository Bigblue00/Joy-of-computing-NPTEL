n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
x=0
for i in range(n):
	for j in range(n):
		if a[i][j]!=a[j][i]:
			x=+1
if x==0:
	print('YES',end="")
else:
	print('NO',end="")