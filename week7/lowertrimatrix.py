n=int(input())
a=[list(map(int,input().split())) for i in range(n)];
for i in range(n):
	for j in range(n):
		if j==n-1:
			end=''
		else:
			end=' '
		if(i<j):
			print(0, end=end)
		else:
			print(a[i][j], end=end)
	print()