n1=(int(input("Enter number1:")));
n2=(int(input("Enter number2:")));

if(n1<n2):
    for i in range(n1,n2+1):
        if(i%2!=0):
            print(i);
else:
    i=n2;
    while(i>=n2):
        print(i);
    i=i+1;
