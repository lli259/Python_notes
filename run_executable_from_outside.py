# coding: utf-8


'''
1) write and compile c++ code

#include <stdio.h>
#include <stdlib.h>
int main(){
    int a = 10;
    int b = 3;


    int c = a * b;
	printf("%d\n", c);
    return 0;
}

compile it to executable ./calledByPy。
'''
 
 #2) call from python
 #refer: http://www.cnblogs.com/apexchu/p/5015961.html

import commands  
import os  
main = "./calledByPy"  

if os.path.exists(main):  
    rc, out = commands.getstatusoutput(main)  
    print 'rc = %d, \nout = %s' % (rc, out)  
    #or 
    #rc= commands.getoutput(main).split(",") # return values as a string and split it into list
  
print '*'*10  
f = os.popen(main)    #execute and return values as a file.
data = f.readlines()    
f.close()    
print data  
  
print '*'*10  
r_v = os.system(main)  #excuta and return values
print r_v 

#from: https://blog.csdn.net/juanjuan1314/article/details/69666374?utm_source=copy 
