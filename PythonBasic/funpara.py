#coding=utf-8
#!/usr/bin/python
 
# 可写函数说明
def changeme( mylist ,mynum):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   mynum += 1;
   print "函数内取值: ", mynum
   return
 
# 调用changeme函数
mylist = [10,20,30];
mynum = 10;
changeme( mylist ,mynum);
print "函数外取值: ", mylist , mynum
