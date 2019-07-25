import time;
import sys;
start=time.time();
args=sys.argv;
n1=int(args[1]);
if(n1>1):
    for i in range(2,n1+1):
        if(n1%i==0):
            print(n1,"is not prime number");
            break;
        else:
            print(n1,"is a prime number");
            break;
end=time.time();
print(end);
print(end - start,"ms");
