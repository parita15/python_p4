class String:

    def __init__(self):
        print ("Default constructor is called:");
    
    def __init__(self,st=""):
        print("Peramaterizd constuctor is called:");
        self.str=st;

    def set(self,st=""):
        self.str=st;

    def get(self):
        return(self.str);

    def length(self):
        return(len(self.str));

    def join(self,str1):
       self.str=self.str+str1.str;
    

    def compare(self,str2):
        if(self.str==str2):
            return True;
        else:
           return False;
        
    def reverse(self):
        return self.str[::-1];

    def palindrome(self):
        self.revst=self.str[::-1];
        if self.str==self.revst:
            print("palindrome");
        else:
            print("Not palindrome");
            
    def check_word(self,str3):
        self.strtt=self.str.find(str3.str);
        return self.strtt;

#

s1=String();
print("st=",s1.get());
s2=String("DDU");
print("st2=",s2.get());
print("String Length=",s2.length());
s3=String("Hello ");
s4=String("World");
s5=String("mom");
s3.join(s4);
print("join=",s3.get());
s2.compare(s4);
print("Comapre string:",s2.get());
s5.palindrome();
print("Reverse string is:",s4.reverse());
s6=String();
s6.set("Python programming");
#s7=input("Search word:");
#s7.check_word(s6);
print("word is:",s6.check_word(s2));

