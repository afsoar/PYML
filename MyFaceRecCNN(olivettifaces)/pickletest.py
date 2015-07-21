# -*-coding:utf8-*-#

a = [1,2,3]
b = {4:5,6:7}

import cPickle
write_file = open('/Users/Fox/Documents/OneDrive/Practice/cPicklefile','wb')
cPickle.dump(a,write_file,-1)
cPickle.dump(b,write_file,-1)
write_file.close()

read_file = open('/Users/Fox/Documents/OneDrive/Practice/cPicklefile','rb')
a_1 = cPickle.load(read_file)
b_1 = cPickle.load(read_file)
print a,b
read_file.close()