# -*-coding:utf8-*-#

import cPickle  
import pylab  
read_file=open('/Users/Fox/Documents/OneDrive/Practice/olivettifaces.pkl','rb')    
faces=cPickle.load(read_file)  
read_file.close()   
img1=faces[1].reshape(57,47)  
pylab.imshow(img1)  
pylab.gray()  
pylab.show()