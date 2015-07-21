# -*-coding:utf8-*-#
#fox cPickle learning

a = [1,2,3]
b = {4:5,6:7}

import cPickle
write_file = open('/Users/Fox/Documents/OneDrive/Practice/cPicklefile','wb')
cPickle.dump(a,write_file,-1)
cPickle.dump(b,write_file,-1)
write_file.close()

read_file = open('/Users/Fox/Documents/OneDrive/Practice/cPicklefile','rb')
c = cPickle.load(read_file)
d = cPickle.load(read_file)
print c
print 'test'
print d
print 'test'
read_file.close()