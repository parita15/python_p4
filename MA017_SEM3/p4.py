import sys;
import time;
start=time.time();
args=sys.argv;
n1=int(args[1]);
n2=int(args[2]);

for i in range(n1,n2+1):
    if(i>1):
        for n1 in range(2,i):
            if(i%n1==0):
                break;
            else:
                print(i);
                break;
end=time.time();
print("Execution time:%.2f",(end - start));
