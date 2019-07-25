print("Else ia called");
for i in range(5):
    print("YES");
else:
    print("NO");
print("Break is called");
x=10;
while x>=1:
    print('x=',x);
    x=x-1;
    if x==5:
        break;
print("out of loop");
print("Continue is called");
x=0;
while x<10:
    x=x+1;
    if x>5:
        continue;
    print('x=',x);
print("out of loop");
