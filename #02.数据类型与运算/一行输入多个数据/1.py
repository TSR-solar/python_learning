a=input().split()
h=input()
h=int(h)

cnt=0
for n in a:
    if h+30>=int(n):
        cnt+=1

print(cnt)