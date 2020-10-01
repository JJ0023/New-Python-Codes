print("Multiple comment lines skipped by Bishal")

x = int(input("Enter x"))
u = int(input("Enter u"))
y = int(input("Enter y"))
v = int(input("Enter v such that v < u"))

deer1=[]
deer2=[]

a = x;
b = y;

while a < 10001:
    deer1.append(a)
    a = a+u
print(deer1)

while b < 10001:
    deer1.append(b)
    b = b+v
print(deer1)
i = 0
while (True):
    if deer1[i] == deer2[i]:
        print("YES")
        break
    else:
        i = i+1


print("NO")







