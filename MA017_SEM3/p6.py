import sys;
count=len(sys.argv)-1;
args=sys.argv;
i=1;
sum=0;
avg=0;
max=0;
min=9999999;
while(i<=count):
    sum=int(args[i])+sum;
    avg=int(sum//count);
    if(int(max) < int(args[i])):
        max=args[i];
    if(int(min) > int(args[i])):
        min=args[i];
    i=i+1;
print("Sum is ",sum);
print("Avg is ",avg);
print("Maximum number is ",max);
print("Minimum number is ",min);
